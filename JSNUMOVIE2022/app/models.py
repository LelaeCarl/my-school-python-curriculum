'''
app/models.py
'''
from werkzeug.security import check_password_hash

from app import db
from datetime import datetime
# 1.管理员
class Admin(db.Model):
    # 1.1 设置表格名称(数据库表名一致)
    __tablename__ = 'admin'

    # 1.2 表格是否存在
    table_args = {'useexisting':True}

    # 1.3 设置映射
    id = db.Column(db.Integer,primary_key=True) # 编号
    name = db.Column(db.String(100),unique=True) # 管理员账号
    pwd = db.Column(db.String(100)) # 管理员密码
    is_super = db.Column(db.SmallInteger) # 是否为管理员 0,1
    role_id = db.Column(db.Integer)# 角色
    addtime = db.Column(db.DateTime,index=True,
                        default=datetime.now())

    # 1.4 外键关联
    # 管理员登录日志
    adminlogs = db.relationship("Adminlog",backref='admin')
    # 管理员操作日志
    oplogs = db.relationship("Oplog",backref='admin')

    # 1.5 设置对象属性
    def __repr__(self):
        return "<Admin %r>"%self.name

    # 1.6 检查密码是否一致
    def check_pwd(self,userPwd):
        return self.pwd == userPwd
# 2.管理员操作日志模型
class Adminlog(db.Model):
    # 2.1 设置表格名称
    __tablename__ = 'adminlog'
    # 1.2 表格是否存在
    table_args = {'useexisting': True}
    # 2.3 表格字段
    id = db.Column(db.Integer,primary_key=True)  # 日志编号
    admin_id = db.Column(db.Integer,db.ForeignKey("admin.id"))  # 外键，关联管理员表
    ip = db.Column(db.String(100))  # 操作时的 IP 地址
    addtime = db.Column(db.DateTime,index=True,
                        default=datetime.now()) # 操作时间，默认为当前时间
    # 1.5 设置对象属性
    def __repr__(self):
        return "<Adminlog %r>"%self.id

class Tag(db.Model):
    # 3.1 设置表格名称
    __tablename__= 'tag'
    # 3.2 判断是否存在
    table_args = {'useexisting':True}
    # 3.3 设置映射关系
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(10),unique=True)
    addtime = db.Column(db.DateTime,index=True,
                        default=datetime.now())

    # 3.4 设置外键关联
    movies = db.relationship("Movie",backref='tag')

    # 返回属性值
    def __repr__(self):
        return "<Tag %r>"%self.name

# 4.管理员操作日志
class Oplog(db.Model):
    __tablename__='oplog'
    table_args = {'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer,db.ForeignKey("admin.id"))
    ip = db.Column(db.String(100))
    reason = db.Column(db.String(100))  # 操作原因
    addtime = db.Column(db.DateTime,index=True,
                        default=datetime.now())

    def __repr__(self):
        return "<Oplog %r>"%self.id

# 5.电影表
class Movie(db.Model):
    __tablename__ = 'movie'
    table_args = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    url = db.Column(db.String(255), unique=True)
    info = db.Column(db.Text)
    logo = db.Column(db.String(255), unique=True)
    star = db.Column(db.SmallInteger)
    playnum = db.Column(db.BigInteger)
    commentnum = db.Column(db.BigInteger)

    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
    area = db.Column(db.String(255))
    release_time = db.Column(db.Date)
    length = db.Column(db.String(100))
    addtime = db.Column(db.DateTime,index=True,
                        default = datetime.now())

    # 评论和收藏表的外键关联
    comments = db.relationship("Comment",backref='movie')
    moviecols = db.relationship("Moviecol",backref='movie')

    def __repr__(self):
        return "<Movie %r>"%self.title

# 6.预告表
class Preview(db.Model):
    __tablename__= 'preview'
    table_args ={'useexisting':True}
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255),unique=True)
    logo = db.Column(db.String(255),unique=True)
    addtime = db.Column(db.DateTime,index=True,
                        default=datetime.now())
    def __repr__(self):
        return "<Preview %r>"%self.title

# 7.会员表
class User(db.Model):
    __tablename__ ='user'
    table_args = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    pwd = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    phone = db.Column(db.String(255), unique=True)
    info = db.Column(db.Text) # 简介
    face = db.Column(db.String(255), unique=True)
    addtime = db.Column(db.DateTime,index = True,
                        default=datetime.now())
    uuid = db.Column(db.String(255),unique=True)

    #外键关联
    comments = db.relationship("Comment",backref = 'user')
    moviecols = db.relationship("Moviecol", backref='user')
    userlogs = db.relationship("Userlog", backref='user')

    def __repr__(self):
        return "<User %r>"%self.name
    def check_pwd(self,userPwd):
        return  userPwd == self.pwd or \
            check_password_hash(self.pwd,userPwd)

# 8.评论表
class Comment(db.Model):
    __tablename__ = 'comment'
    table_args = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    movie_id = db.Column(db.Integer,db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    addtime = db.Column(db.DateTime, index=True,
                        default=datetime.now())

    def __repr__(self):
        return "<Comment %r>" % self.id

# 9.收藏表
class Moviecol(db.Model):
    __tablename__ = 'moviecol'
    table_args = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer,db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    addtime = db.Column(db.DateTime, index=True,
                        default=datetime.now())

    def __repr__(self):
        return "<Moviecol %r>" % self.id

# 10.会员登录日志
class Userlog(db.Model):
    __tablename__='userlog'
    table_args = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"))
    ip = db.Column(db.String(100))
    addtime = db.Column(db.DateTime,index=True,
                        default=datetime.now())

    def __repr__(self):
        return "<userlog %r>"%self.id

# 11.权限列表
class Auth(db.Model):
    __tablename__='Auth'
    table_args = {'useexisting': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),unique=True)
    url = db.Column(db.String(255), unique=True)
    addtime = db.Column(db.DateTime,index=True,
                        default=datetime.now())

    def __repr__(self):
        return "<userlog %r>"%self.id



