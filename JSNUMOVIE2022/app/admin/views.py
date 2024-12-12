import os
import stat

from . import admin
from flask import render_template, flash, redirect, url_for, session, request
from app.admin.forms import LoginForm, TagForm, MovieForm
from app import db  # Variable from app.__init__.py
from app.models import Admin, Adminlog, Tag, Oplog, Movie
from werkzeug.utils import secure_filename
from app import app
import uuid
from datetime import datetime

# 1. Login module functionality
@admin.route("/login/", methods=['GET', 'POST'])
def login():
    # 1.1 Retrieve login form
    form = LoginForm()
    # 1.2 Check if the form is submitted (POST)
    if form.validate_on_submit():
        # 1.3 Get form data (account, pwd)
        data = form.data
        # 1.4 Query user by account
        admin = Admin.query.filter_by(name=data['account']).first()
        # 1.5 Check if user exists and password matches
        if admin is None or not admin.check_pwd(data['pwd']):
            flash("Invalid username or password", 'err')
            return redirect(url_for('admin.login'))
        # 1.6 Save user data to session
        session['admin'] = data['account']
        session['admin_id'] = admin.id

        # 1.7 Log admin login details
        adminlog = Adminlog(
            admin_id=admin.id,
            ip=request.remote_addr
        )
        db.session.add(adminlog)
        db.session.commit()

        # 1.8 Redirect to homepage
        return redirect(url_for('admin.index'))

    return render_template("admin/login.html", form=form)

# 2. Admin system homepage
@admin.route("/")
def index():
    return render_template("admin/index.html")

# 3. Add tag
@admin.route("/tag_add/", methods=['GET', 'POST'])
def tag_add():
    form = TagForm()
    if form.validate_on_submit():
        data = form.data
        tag = Tag.query.filter_by(name=data['name']).count()
        if tag == 1:
            flash("Movie tag already exists, cannot be duplicated!", 'err')
            return redirect(url_for("admin.tag_add"))
        tag = Tag(name=data['name'])
        db.session.add(tag)
        db.session.commit()
        oplog = Oplog(
            admin_id=session['admin_id'],
            ip=request.remote_addr,
            reason=f'Added tag {data["name"]}'
        )
        db.session.add(oplog)
        db.session.commit()
        flash("Tag added successfully", "ok")
        redirect(url_for("admin.tag_add"))
    return render_template("admin/tag_add.html", form=form)

# 4. Tag list
@admin.route("/tag_list/<int:page>/", methods=['GET'])
def tag_list(page=None):
    if page is None:
        page = 1
    page_data = Tag.query.order_by(Tag.addtime)\
                .paginate(page=page, per_page=5)
    return render_template("admin/tag_list.html", page_data=page_data)

# 5. Edit tag
@admin.route("/tag_edit/<int:id>", methods=['GET', 'POST'])
def tag_edit(id=None):
    form = TagForm()
    tag = Tag.query.get_or_404(id)
    form.submit.label.text = "Modify"
    if form.validate_on_submit():
        data = form.data
        tag_count = Tag.query.filter_by(name=data['name']).count()
        if tag.name != data['name'] and tag_count == 1:
            flash("Tag already exists!", 'err')
            return redirect(url_for("admin.tag_edit", id=tag.id))
        tag.name = data['name']
        db.session.add(tag)
        db.session.commit()
        flash("Tag successfully modified!", 'ok')
        redirect(url_for("admin.tag_edit", id=tag.id))
    return render_template("admin/tag_edit.html", form=form, tag=tag)

# 6. Delete tag
@admin.route("/tag_del/<int:id>", methods=['GET'])
def tag_del(id=None):
    tag = Tag.query.filter_by(id=id).first_or_404()
    db.session.delete(tag)
    db.session.commit()
    flash(f"Tag <<<{tag.name}>>> deleted successfully", 'ok')
    return redirect(url_for('admin.tag_list', page=1))

# 7. Add movie
@admin.route("/movie_add/", methods=['GET', 'POST'])
def movie_add():
    form = MovieForm()
    if form.validate_on_submit():
        data = form.data
        file_url = secure_filename(form.url.data.filename)
        file_logo = secure_filename(form.logo.data.filename)
        if not os.path.exists(app.config['UP_DIR']):
            os.mkdir(app.config['UP_DIR'])
            os.chmod(app.config['UP_DIR'], stat.S_IRWXU)
        url = chang_filename(file_url)
        logo = chang_filename(file_logo)
        form.url.data.save(app.config['UP_DIR'] + url)
        form.logo.data.save(app.config['UP_DIR'] + logo)
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
        db.session.add(movie)
        db.session.commit()
        flash("Movie added successfully!", 'ok')
        return redirect(url_for("admin.movie_add"))

    return render_template("admin/movie_add.html", form=form)

# 8. Movie list
@admin.route("/movie_list/<int:page>", methods=['GET'])
def movie_list(page=None):
    if page is None:
        page = 1
    page_data = Movie.query.join(Tag).filter(
        Tag.id == Movie.tag_id
    ).order_by(
        Movie.addtime.desc()
    ).paginate(page=page, per_page=5)
    return render_template("admin/movie_list.html", page_data=page_data)

# 9. Edit movie
@admin.route("/movie_edit/<int:id>", methods=['GET', 'POST'])
def movie_edit(id=None):
    form = MovieForm()
    form.url.validators = []
    form.logo.validators = []
    movie = Movie.query.get_or_404(int(id))
    if request.method == "GET":
        form.info.data = movie.info
        form.tag_id.data = movie.tag_id
        form.star.data = movie.star
    if form.validate_on_submit():
        data = form.data
        movie_count = Movie.query.filter_by(title=data['title']).count()
        if movie_count == 1 and movie.title != data['title']:
            flash("Movie name already exists!", 'err')
            return redirect(url_for("admin.movie_edit", id=id))
        if not os.path.exists(app.config['UP_DIR']):
            os.mkdir(app.config['UP_DIR'])
            os.chmod(app.config['UP_DIR'], stat.S_IRWXU)

        if form.url.data != "":
            os.remove(app.config['UP_DIR'] + movie.url)
            file_url = secure_filename(form.url.data.filename)
            movie.url = chang_filename(file_url)
            form.url.data.save(app.config['UP_DIR'] + movie.url)
        if form.logo.data != "":
            os.remove(app.config['UP_DIR'] + movie.logo)
            file_logo = secure_filename(form.logo.data.filename)
            movie.logo = chang_filename(file_logo)
            form.logo.data.save(app.config['UP_DIR'] + movie.logo)
        movie.star = data['star']
        movie.tag_id = data['tag_id']
        movie.info = data['info']
        movie.title = data['title']
        movie.area = data['area']
        movie.length = data['length']
        movie.release_time = data['release_time']
        db.session.add(movie)
        db.session.commit()
        flash("Movie successfully modified!", 'ok')
        return redirect(url_for("admin.movie_edit", id=id))

    return render_template("admin/movie_edit.html", form=form, movie=movie)

# 10.Movie Management - Movie Deletion
@admin.route("/movie_del/<int:id>/",methods=['GET'])
def movie_del(id=None):
    # 10.1 Check if the movie exists
    movie = Movie.query.get_or_404(id)
    # 10.2 Delete the movie
    if not movie is None:
        # 10.2.1 Delete the file and poster
        os.remove(app.config['UP_DIR']+movie.url)
        os.remove(app.config['UP_DIR']+movie.logo)
        # 10.2.2 Delete the movie object
        db.session.delete(movie)
        db.session.commit()
        # 10.2.3 Flash message
        flash(f"Movie <<<{movie.title} successfully deleted",'ok')
        # 10.2.4 Redirect
        return redirect(url_for("admin.movie_list",page=1))

# Change file name
def chang_filename(filename):
    # 1. Extract file information D:/movie/ZhanLang.wav
    fileInfo = os.path.splitext(filename)
    # 2. Generate a new file name 20241211091736ix23.wav
    filename = datetime.now().strftime("%Y%m%d%H%M%S")\
                +str(uuid.uuid4().hex)+fileInfo[-1]
    return filename

