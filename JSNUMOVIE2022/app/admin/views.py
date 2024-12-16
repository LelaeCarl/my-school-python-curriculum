'''
app/admin/views.py
'''
import os.path
import stat
import uuid
import datetime

from werkzeug.utils import secure_filename

from . import admin
from flask import render_template,flash,redirect,url_for,session,request
from app.admin.forms import LoginForm, TagForm, MovieForm, PreviewForm, AuthForm
from app import db # app.__init__.py中的变量
from app.models import Admin, Tag, Oplog, Movie, Preview, User, Comment, Moviecol, Userlog, Auth
from app.models import Adminlog
from app import app



# 1.登录模块功能实现
@admin.route("/login/",methods=['GET','POST'])
def login():
    # 1.1 获取登录表单
    form = LoginForm()
    # 1.2 判断表单是否提交(post)
    if form.validate_on_submit():
        # 1.3 获取表单数据(account,pwd)
        data = form.data
        # 1.4 根据account查询是否有此用户
        # name数据库表Admin表中字段名 name
        # data是表单数据值,字典类型 key值是LoginForm表单中的变量
        admin = Admin.query.filter_by(
                    name=data['account']).first()
        # 1.5 判断是否为空 或者 密码是否一致
        if admin == None or not admin.check_pwd(data['pwd']):
            # 1.5.1 通过Flask发送错误信息
            flash("用户名或密码错误",'err')
            # 1.5.2 重定向请求
            return redirect(url_for('admin.login'))
        # 1.6 用户名和密码一致情况下则将数据保存到session
        session['admin'] = data['account']
        session['admin_id'] = admin.id

        # 1.7 设置管理员登录日志(管理员的id,管理员登录ip地址,登录时间)
        adminlog = Adminlog(
             admin_id = admin.id,
             ip = request.remote_addr
        )
        # 1.8 数据库添加管理员登录日志
        db.session.add(adminlog)
        db.session.commit()

        # 1.9 重定向到主页
        return redirect(url_for('admin.index'))

    return render_template("admin/login.html", form=form)

# 2.后台管理系统首页  /
@admin.route("/")
def index():
    return render_template("admin/index.html")

# 3.标签管理-添加标签
@admin.route("/tag_add/",methods=['GET','POST'])
def tag_add():
    # 3.1 获取Tag表单
    form = TagForm()
    # 3.2 判断是否点击表单提交按钮
    if form.validate_on_submit():
        # 3.3 获取表单数据
        data = form.data
        # 3.4 根据标签名称查找统计标签
        tag = Tag.query.filter_by(name=data['name']).count()
        # 3.5 判断是否存在
        if tag == 1:
            flash("电影标签已存在,不可重复!!!",'err')
            return redirect(url_for("admin.tag_add"))
        # 3.6 设置taq模型(设置实体类)
        tag = Tag(name=data['name'])
        # 3.7 设置session添加
        db.session.add(tag)
        db.session.commit()
        # 3.8 设置oploq模型
        oplog = Oplog(
            admin_id = session['admin_id'],
            ip = request.remote_addr,
            reason = '添加标签%s'%data['name']
        )
        # 3.9 添加管理员操作日志
        db.session.add(oplog)
        db.session.commit()
        # 3.10 添加成功 弹出框品示
        flash("标签添加成功","ok")
        redirect(url_for ("admin.tag_add"))
    return render_template("admin/tag_add.html",form=form)

# 4.标签管理-标签列表
@admin.route("/tag_list/<int:page>/",methods=['GET'])
def tag_list(page=None):
    # 4.1 无页码的情况
    if page is None:
        page = 1
    # 4.2 有页码的情况(当前页码以及每页显示的数量)
    page_data = Tag.query.order_by(Tag.addtime)\
        .paginate(page=page,per_page=5)
    # 4.3 返回页面
    return  render_template("admin/tag_list.html",
                            page_data=page_data)

# 5.标签管理-标签编辑
@admin.route("/tag_edit/<int:id>",methods=['GET','POST'])
def tag_edit(id=None):
    # 5.1获取表单
    form = TagForm()
    # 5.2 根据id获取标签对象
    tag = Tag.query.get_or_404(id)
    # 5.3 修改表单中的按钮名称
    form.submit.label.text = "修改"
    # 5.4 判断修改按钮是否点击
    if form.validate_on_submit():
        # 5.5 获取表单数据
        data = form.data
        # 5.6查询修改标签数据是否已存在
        tag_count = Tag.query.filter_by(name=data['name'])\
                    .count()
        # 5.7 判断(名称不一致 且 已经存在的标签)
        if tag.name != data['name'] and \
            tag_count == 1:
            flash("标签已存在!!!",'err')
            return redirect(url_for("admin.tag edit", id=tag.id))
        # 5.8 将表单中的数据进行修改
        tag.name = data['name']
        # 5.9 数据库的数据修改(add是覆盖)
        db.session.add(tag)
        db.session.commit()
        # 5.10 提示框
        flash("标签已经修改成功啦!!!",'ok')
        # 5.11 重定向到编辑页面
        redirect(url_for ("admin.tag_edit",id=tag.id))
    return render_template("admin/tag_edit.html",
                            form = form, tag = tag)

# 6.标签管理-标签删除
@admin.route("/tag_del/<int:id>",methods=['GET'])
def tag_del(id=None):
    # 6.1 根据id查询标签数据
    tag = Tag.query.filter_by(id=id).first_or_404()
    # 6.2 根据标签对象删除
    db.session.delete(tag)
    db.session.commit()
    # 6.3 提示框
    flash(f"标签<<<{tag.name}>>>删除成功",'ok')
    # 6.4 重定向请求
    return redirect(url_for('admin.tag_list',page=1))

# 7.电影管理-电影添加
@admin.route("/movie_add/",methods=['GET','POST'])
def movie_add():
    # 7.1获取电影表单
    form = MovieForm()
    # 7.2判断是否提交
    if form.validate_on_submit():
        # 7.3 获取表单数据
        data = form.data
        # 7.4 处理电影文件以及logo上传
        file_url = secure_filename(form.url.data.filename)
        file_logo = secure_filename(form.logo.data.filename)
        # 7.5 判断uploads是否存在static/uploads/下是否存在
        if not os.path.exists(app.config['UP_DIR']):
            # 7.5.1创建目录
            os.mkdir(app.config['UP_DIR'])
            # 7.5.2修改目录权限
            os.chmod(app.config['UP_DIR',stat.S_IRWXU])
        # 7.6更改路径已经名称等zpp.wav
        url = chang_filename(file_url)
        logo = chang_filename(file_logo)
        # 7.7保存数据到form表达中
        form.url.data.save(app.config['UP_DIR']+url)
        form.logo.data.save(app.config['UP_DIR']+logo)
        # 7.8设置模型对象数据
        movie = Movie(
            title=data['title'],
            url=url,
            info=data['info'],
            logo=logo,
            star=int(data['star']),
            playnum=0,
            commentnum=0,
            tag_id=int(data['tag_id']),
            area=data['area'],
            release_time=data['release_time'],
            length=data['length']
        )
        # 7.9添加数据
        db.session.add(movie)
        db.session.commit()
        # 7.10弹出框
        flash("添加电影成功啦啦啦！！！",'ok')
        # 7.11 重定向
        return redirect(url_for("admin.movie_add"))

    return render_template("admin/movie_add.html",
                           form=form)

# 8.电影管理-电影列表
@admin.route("/movie_list/<int:page>",methods=['GET'])
def movie_list(page=None):
    #8.1 判断page是否有值
    if page is None:
        page = 1
    #8.2 进行关联查询
    page_data = Movie.query.join(Tag).filter(
        Tag.id == Movie.tag_id
    ).order_by(
        Movie.addtime.desc()
    ).paginate(page=page,per_page=5)
    #8.3 返回movie list.html
    return render_template("admin/movie_list.html",
                            page_data=page_data)

# 9.电影管理-电影编辑
@admin.route("/movie_edit/<int:id>",methods=['GET','POST'])
def movie_edit(id=None):
    # 9.1 获取电影表单
    form = MovieForm()
    # 9.2 读取url,logo非空验证为空,编辑不修改的时候，不会验证报错
    form.url.validators = []
    form.logo.validators = []
    # 9.3 根据id查询数据
    movie = Movie.query.get_or_404(int(id))
    # 9.4 判断请求的类型
    if request.method == "GET":
        # 9.4.1 设置info,tag_id,star数据
        form.info.data = movie.info
        form.tag_id.data = movie.tag_id
        form.star.data = movie.star
    # 9.5 表单是否提交
    if form.validate_on_submit():
        # 9.6 获取表单数据
        data = form.data
        # 9.7 根据表单名称查询数据库是否存在
        movie_count = Movie.query.filter_by(
                title=data['title']).count()
        # 9.8判断电影名称是否存在以及电影名称是否修改
        if movie_count == 1 and \
                movie.title != data['title']:
            # 9.8.1 提示框
            flash("片名已经存在!!!",'err')
            return redirect(url_for("admin.movie_edit",id=id))
        # 9.9 创建目录
        if not os.path.exists(app.config['UP_DIR']):
            os.mkdir(app.config['UP_DIR'])
            os.chmod(app.config['UP_DIR'], stat.S_IRWXU)

        # 9.10上传新的视频文件
        if form.url.data != "":
            # 9.10.1 删除原有的视频文件
            os.remove(app.config['UP_DIR'] + movie.url)
            # 9.10.2 上传新的视频文件
            file_url = secure_filename(form.url.data.filename)
            # 9.10.3 修改新的视频文件的名称
            movie.url = chang_filename(file_url)
            # 9.10.4 将新的视频文件名称保存到form表单中
            form.url.data.save(app.config['UP_DIR'] + movie.url)
        # 9.11 上传海报
        if form.logo.data != "":
            # 9.11.1 删除原有图片文件
            os.remove(app.config['UP_DIR'] + movie.logo)
            # 9.11.2 上传图片文件
            file_logo =secure_filename(form.logo.data.filename)
            # 9.11.3 修改上传图片的文件名称
            movie.logo = chang_filename(file_logo)
            # 9.11.4 保存新的图片文件名称到表单中
            form.logo.data.save(app.config['UP_DIR']+movie.logo)
        # 9.13 设置其他的数据信息
        movie.star = data['star']
        movie.tag_id = data['tag_id']
        movie.info = data['info']
        movie.title = data['title']
        movie.area = data['area']
        movie.length = data['length']
        movie.release_time = data['release_time']
        # 9.14 数据提交
        db.session.add(movie)
        db.session.commit()
        # 9.15 提示框
        flash("修改电影成功!!!!",'ok')
        return redirect(url_for ("admin.movie_edit", id=id))


    return render_template("admin/movie_edit.html",
                           form=form,movie=movie)

# 10.电影管理-电影删除
@admin.route("/movie_del/<int:id>",methods=['GET'])
def movie_del(id=None):
    # 10.1 查看电影是否存在
    movie = Movie.query.get_or_404(id)
    # 10.2 删除电影
    if not movie is None:
        # 10.2.1 删除文件以及海报
        os.remove(app.config['UP_DIR'] + movie.url)
        os.remove(app.config['UP_DIR'] + movie.logo)
        # 10.2.2 删除电影对象
        db.session.delete(movie)
        db.session.commit()
        # 10.2.3 提示框
        flash(f"电影<<<{movie.title}删除成功",'ok')
        # 10.2.4 重定向
        return redirect(url_for("admin.movie_list", page=1))

# 11. 预告管理-预告添加
@admin.route("/preview_add/",methods=['GET','POST'])
def preview_add():
    # 11.1 获取报告表单
    form = PreviewForm()
    # 11.2 判断是否点击按钮
    if form.validate_on_submit():
        # 11.3 获取表单数据
        data = form.data
        # 11.4 处理L0G0
        file_logo = secure_filename(form.logo.data.filename)
        # 11.5 判断uploads是否存在
        if not os.path.exists(app.config['UP_DIR']):
            # 11.5.1 创建目录
            os.mkdir(app.config['UP_DIR'])
            # 11.5.2 设置目录权限
            os.chmod(app.config['UP_DIR'],stat.S_IRWXU)
        # 11.6 修改Logo的名称
        new_logo = chang_filename(file_logo)
        # 11.7 保存数据
        form.logo.data.save(app.config['UP_DIR'] + new_logo)
        # 11.8 设置模型
        preview = Preview(
            title = data['title'],
            logo = new_logo,
            addtime = datetime.datetime.now()
        )
        # 11.9 添加数据
        db.session.add(preview)
        db.session.commit()
        # 11.10 弹出框
        flash("添加预告成功啦!!!!",'ok')
        # 11.11 重定向
        return redirect(url_for("admin.preview_add"))
    return render_template("admin/preview_add.html",
                            form = form)

# 12.预告管理-预告列表
@admin.route("/preview_list/<int:page>",methods=['GET','POST'])
def preview_list(page=None):
    # 12.1 判断page是否有值
    if page is None:
        page = 1
    #12.2 根据添加时间排序的分页数据
    page_data= Preview.query.order_by(
        Preview.addtime.desc()
    ).paginate(page=page,per_page=3)
    # 12.3 返回页面
    return render_template("admin/preview_list.html",
                            page_data=page_data)

# 13.预告管理-预告编辑
@admin.route("/preview_edit/<int:id>/",methods=['GET','POST'])
def preview_edit(id=None):
    # 13.1 获取预告表单
    form = PreviewForm()
    # 13.2 设置logo验证器为空
    form.logo.validators =[]
    # 13.3 根据id查询预告
    preview = Preview.query.get_or_404(int(id))
    # 13.4 判断请求类型
    if request.method == 'GET':
        # 13.4.1 将预告名称设置到表单中
        form.title.data = preview.title
    # 13.5 判断表单提交
    if form.validate_on_submit():
        # 13.6 获取表单数据
        data = form.data
        # 13.7 根据表单数据查询是否存在
        preview_count = Preview.query.filter_by(
                    title=data['title']).count()
        # 13.8 判断是否已经存在
        if preview_count == 1 and \
            preview.title != data['title']:
            flash("预告名称已存在",'err')
            return redirect(url_for('admin.preview_edit', id=id))
        # 13.9 创建目录
        if not os.path.exists(app.config['UP_DIR']):
            # 13.9.1 创建目录
            os.mkdir(app.config['UP_DIR'])
            # 13.9.2 设置目录权限
            os.chmod(app.config['UP_DIR'], stat.S_IRWXU)

        # 13.10 上传图片
        if form.logo.data != "":
            # 13.10.1 删除原有的图片
            os.remove(app.config['UP_DIR'] + preview.logo)
            # 13.10.2 上传新的文件
            file_logo = secure_filename(form.logo.data.filename)
            # 13.10.3 修改名称
            preview.logo = chang_filename(file_logo)
            # 13.10.4 保存新的数据
            form.logo.data.save(
                app.config['UP_DIR'] + preview.logo)

        # 13.11 设置其他的数据
        preview.title = data['title']
        # 13.12 数据提交修改
        db.session.add(preview)
        db.session.commit()
        # 13.13 弹出框
        flash("修改预告成功","ok")
        # 13.14 重定向
        return redirect(url_for('admin.preview_edit', id=id))

    return render_template("admin/preview_edit.html",
                             form=form, preview=preview)

# 14.预告管理-预告删除
@admin.route("/preview_del/<int:id>",methods=['GET'])
def preview_del(id=None):
    # 14.1 查看是否存在该预告
    preview = Preview.query.get_or_404(id)
    # 14.2 删除预告
    if not preview is None:
        # 14.3 删除预告海报
        os.remove(app.config['UP_DIR']+preview.logo)
        # 14.4 删除预告对象
        db.session.delete(preview)
        db.session.commit()
        # 14.5 提示框
        flash(f"<<<{preview.title}>>>删除成功!!!",'ok')
        return redirect(url_for("admin.preview_list",page=1))

# 15.会员管理-会员列表
@admin.route("user_list/<int:page>",methods = ['GET'])
def user_list(page=None):
    # 15.1判断page是否有值
    if page is None:
        page = 1
    # 15.2 根据添加时间分页数据
    page_data = User.query.order_by(
        User.addtime.desc()
    ).paginate(page=page,per_page=5)
    # 15.3 返回user_list.html
    return render_template("admin/user_list.html",
                           page_data=page_data)

# 16.会员管理-会员查看
@admin.route("user_view/<int:id>",methods = ['GET'])
def user_view(id=None):
    # 16.1 获取fp参数
    form_page = request.args.get("fp")
    # 16.2 判断fp是否有值
    if not form_page:
        form_page = 1
    # 16.3 根据id查询数据
    user = User.query.get_or_404(int(id))
    # 16.4 返回视图
    return render_template("admin/user_view.html",
                           user = user,
                           form_page = form_page)

# 17.会员管理-会员删除
@admin.route("user_del/<int:id>",methods = ['GET'])
def user_del(id=None):
    # 17.1 删除当前页
    form_page = int(request.args.get("fp")) - 1
    # 17.2 判断是否存在
    if not form_page:
        form_page = 1
    # 17.3 通过id查询数据
    user =User.query.get_or_404(int(id))
    # 17.4 判断头像是否存在
    if os.path.exists(app.config['FC_DIR']+user.face):
        os.remove(app.config['FC_DIR']+user.face)
    # 17.5 删除用户数据
    db.session.delete(user)
    db.session.commit()
    # 17.6 弹出框
    flash("删除会员成功！！！",'ok')
    return redirect(url_for('admin.user_list',page=form_page))

# 18.评论管理-评论列表
@admin.route("comment_list/<int:page>",methods = ['GET'])
def comment_list(page=None):
    # 18.1 判断page是否为None
    if page is None:
        page  = 1
    # 18.2 多表单关联查询
    page_data = Comment.query.join(Movie).join(User).filter(
        Movie.id == Comment.movie_id,
        User.id == Comment.user_id
    ).order_by(Comment.addtime.desc())\
    .paginate(page=page,per_page = 1)
    return render_template("admin/comment_list.html",
                           page_data=page_data)

# 19.评论管理-评论删除
@admin.route("comment_del/<int:id>",methods = ['GET'])
def comment_del(id=None):
    # 17.1 删除当前页
    form_page = int(request.args.get("fp")) - 1
    # 17.2 判断是否存在
    if not form_page:
        form_page = 1
    # 17.3 通过id查询数据
    comment =Comment.query.get_or_404(int(id))
    # 17.5 删除用户数据
    db.session.delete(comment)
    db.session.commit()
    # 17.6 弹出框
    flash("删除评论成功！！！",'ok')
    return redirect(url_for('admin.comment_list',page=form_page))

# 20.收藏管理-收藏列表
@admin.route("moviecol_list/<int:page>",methods = ['GET'])
def moviecol_list(page=None):
    # 18.1 判断page是否为None
    if page is None:
        page  = 1
    # 18.2 多表单关联查询
    page_data = Moviecol.query.join(Movie).join(User).filter(
        Movie.id == Moviecol.movie_id,
        User.id == Moviecol.user_id
    ).order_by(Moviecol.addtime.desc())\
    .paginate(page=page,per_page = 3)
    return render_template("admin/moviecol_list.html",
                           page_data=page_data)

# 21.收藏管理-收藏删除
@admin.route("moviecol_del/<int:id>",methods = ['GET'])
def moviecol_del(id=None):
    # 17.1 删除当前页
    form_page = int(request.args.get("fp")) - 1
    # 17.2 判断是否存在
    if not form_page:
        form_page = 1
    # 17.3 通过id查询数据
    moviecol =Moviecol.query.get_or_404(int(id))
    # 17.5 删除用户数据
    db.session.delete(moviecol)
    db.session.commit()
    # 17.6 弹出框
    flash("删除评论成功！！！",'ok')
    return redirect(url_for('admin.moviecol_list',page=form_page))

# 22.日志管理-会员登录日志列表
@admin.route("userlog_list/<int:page>",methods = ['GET'])
def userlog_list(page=None):
    # 18.1 判断page是否为None
    if page is None:
        page  = 1
    # 18.2 多表单关联查询
    page_data = Userlog.query.join(User).filter(
        User.id == Userlog.user_id
    ).order_by(Userlog.addtime.desc())\
    .paginate(page=page,per_page = 5)
    return render_template("admin/userlog_list.html",
                           page_data=page_data)

# 22.日志管理-管理员登录日志列表
@admin.route("adminlog_list/<int:page>",methods = ['GET'])
def adminlog_list(page=None):
    # 18.1 判断page是否为None
    if page is None:
        page  = 1
    # 18.2 多表单关联查询
    page_data = Adminlog.query.join(Admin).filter(
        Admin.id == Adminlog.admin_id
    ).order_by(Adminlog.addtime.desc())\
    .paginate(page=page,per_page = 5)
    return render_template("admin/adminlog_list.html",
                           page_data=page_data)

# 23.日志管理-管理员操作日志列表
@admin.route("oplog_list/<int:page>",methods = ['GET'])
def oplog_list(page=None):
    # 18.1 判断page是否为None
    if page is None:
        page  = 1
    # 18.2 多表单关联查询
    page_data = Oplog.query.join(Admin).filter(
        Admin.id == Oplog.admin_id
    ).order_by(Oplog.addtime.desc())\
    .paginate(page=page,per_page = 5)
    return render_template("admin/oplog_list.html",
                           page_data=page_data)

# 24. 权限管理-权限添加
@admin.route("/auth_add/",methods=['GET','POST'])
def auth_add():
    # 11.1 获取报告表单
    form = AuthForm()
    # 11.2 判断是否点击按钮
    if form.validate_on_submit():
        # 11.3 获取表单数据
        data = form.data
        auth = Auth.query.filter_by(name=data['name']).count()
        # 3.5 判断是否存在
        if auth == 1:
            flash("权限名称已存在,不可重复!!!"'err')
            return redirect(url_for ("admin.auth_add"))
        # 11.8 设置模型
        auth = Auth(
            name = data['name'],
            url = data['url'],
            addtime = datetime.datetime.now()
        )
        # 11.9 添加数据
        db.session.add(auth)
        db.session.commit()
        # 11.10 弹出框
        flash("添加权限成功啦!!!!",'ok')
        # 11.11 重定向
        return redirect(url_for("admin.auth_add"))
    return render_template("admin/auth_add.html",
                            form = form)

# 25.权限管理-权限列表
@admin.route("/auth_list/<int:page>/",methods=['GET'])
def auth_list(page=None):
    # 4.1 无页码的情况
    if page is None:
        page = 1
    # 4.2 有页码的情况(当前页码以及每页显示的数量)
    page_data = Auth.query.order_by(Auth.addtime)\
        .paginate(page=page,per_page=5)
    # 4.3 返回页面
    return  render_template("admin/auth_list.html",
                            page_data=page_data)



# 修改文件名称
def chang_filename(filename):
    # 1.截取文件信息
    fileInfo = os.path.splitext(filename)
    # 2.生成新的文件名 20241211091736
    filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S")\
                +str(uuid.uuid4().hex)+fileInfo[-1]

    return filename
