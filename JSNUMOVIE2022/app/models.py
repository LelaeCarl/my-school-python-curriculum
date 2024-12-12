from app import db
from datetime import datetime

# 1. Administrator
class Admin(db.Model):
    # 1.1 Set table name (database table name matches)
    __tablename__ = 'admin'

    # 1.2 Ensure the table exists
    table_args = {'useexisting': True}

    # 1.3 Set mappings
    id = db.Column(db.Integer, primary_key=True)  # ID
    name = db.Column(db.String(100), unique=True)  # Administrator account (unique)
    pwd = db.Column(db.String(100))  # Administrator password
    is_super = db.Column(db.SmallInteger)  # Is it an administrator (0 or 1)
    role_id = db.Column(db.Integer)  # Role ID
    addtime = db.Column(db.DateTime, index=True, default=datetime.now())

    # 1.4 Foreign key associations
    # Administrator login logs
    adminlogs = db.relationship("Adminlog", backref='admin')
    # Administrator operation logs
    oplogs = db.relationship("Oplog", backref='admin')

    # 1.5 Set object properties
    def __repr__(self):
        return "<Admin %r>" % self.name

    # 1.6 Check if the password matches
    def check_pwd(self, userPwd):
        return self.pwd == userPwd

# 2. Administrator login logs
class Adminlog(db.Model):
    # 2.1 Set table name
    __tablename__ = 'adminlog'
    # 2.2 Ensure the table exists
    table_args = {'useexisting': True}
    # 2.3 Set mappings
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"))
    ip = db.Column(db.String(100))  # Login IP address
    addtime = db.Column(db.DateTime, index=True, default=datetime.now())

    # 2.4 Set return value
    def __repr__(self):
        return "<Adminlog %r>" % self.id

# 3. Tag table
class Tag(db.Model):
    # 3.1 Set table name
    __tablename__ = 'tag'
    # 3.2 Ensure the table exists
    table_args = {'useexisting': True}
    # 3.3 Set mappings
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now())

    # 3.4 Set foreign key associations
    movies = db.relationship("Movie", backref='tag')

    # Return attribute value
    def __repr__(self):
        return "<Tag %r>" % self.name

# 4. Administrator operation logs
class Oplog(db.Model):
    __tablename__ = 'oplog'
    table_args = {'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"))
    ip = db.Column(db.String(100))
    reason = db.Column(db.String(100))  # Operation reason
    addtime = db.Column(db.DateTime, index=True, default=datetime.now())

    def __repr__(self):
        return "<Oplog %r>" % self.id

# 5. Movie table
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
    addtime = db.Column(db.DateTime, index=True, default=datetime.now())

    # Foreign key associations for comments and collections
    # comments = db.relationship("Comment", backref='movie')
    # moviecols = db.relationship("Moviecol", backref='movie')

    def __repr__(self):
        return "<Movie %r>" % self.title

# 6. Preview table
class Preview(db.Model):
    __tablename__ = 'preview'
    table_args = {'useexisting':True}
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255),unique=True)
    logo = db.Column(db.String(255),unique=True)
    addtime = db.Column(db.DateTime,index=True,
                        default=datetime.now())
    def __repr__(self):
        return "<Preview %r>"%self.title