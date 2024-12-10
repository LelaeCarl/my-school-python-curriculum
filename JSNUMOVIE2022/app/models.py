"""
app/models.py
"""
from app import db
from datetime import datetime

# 1. Admin Model
class Admin(db.Model):
    # 1.1 Set table name (matches database table name)
    __tablename__ = 'admin'

    # 1.2 Ensure table existence
    table_args = {'useexisting': True}

    # 1.3 Set mappings
    id = db.Column(db.Integer, primary_key=True)  # ID
    name = db.Column(db.String(100), unique=True)  # Unique admin username
    pwd = db.Column(db.String(100))  # Admin password
    is_super = db.Column(db.SmallInteger)  # Super admin flag (0 or 1)
    role_id = db.Column(db.Integer)  # Role ID
    addtime = db.Column(db.DateTime, index=True, default=datetime.now())  # Creation time

    # 1.4 Foreign key relationships
    adminlogs = db.relationship("Adminlog", backref='admin')  # Admin login logs
    oplogs = db.relationship("Oplog", backref='admin')  # Admin operation logs

    # 1.5 Set object representation
    def __repr__(self):
        return f"<Admin {self.name}>"

    # 1.6 Check if passwords match
    def check_pwd(self, userPwd):
        return self.pwd == userPwd

# 2. Admin Login Log Model
class Adminlog(db.Model):
    # 2.1 Set table name
    __tablename__ = 'adminlog'
    # 2.2 Ensure table existence
    table_args = {'useexisting': True}
    # 2.3 Set mappings
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"))  # Foreign key to admin
    ip = db.Column(db.String(100))  # Login IP address
    addtime = db.Column(db.DateTime, index=True, default=datetime.now())  # Log time

    # 2.4 Set object representation
    def __repr__(self):
        return f"<Adminlog {self.id}>"

# 3. Tag Model
class Tag(db.Model):
    # 3.1 Set table name
    __tablename__ = 'tag'
    # 3.2 Ensure table existence
    table_args = {'useexisting': True}
    # 3.3 Set mappings
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True)  # Unique tag name
    addtime = db.Column(db.DateTime, index=True, default=datetime.now())  # Creation time

    # 3.4 Foreign key relationships
    # movies = db.relationship("Movie", backref='tag')  # Uncomment when related model exists

    # Set object representation
    def __repr__(self):
        return f"<Tag {self.name}>"

# 4. Admin Operation Log Model
class Oplog(db.Model):
    __tablename__ = 'oplog'
    table_args = {'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"))  # Foreign key to admin
    ip = db.Column(db.String(100))  # IP address
    reason = db.Column(db.String(100))  # Operation reason
    addtime = db.Column(db.DateTime, index=True, default=datetime.now())  # Log time

    # Set object representation
    def __repr__(self):
        return f"<Oplog {self.id}>"
