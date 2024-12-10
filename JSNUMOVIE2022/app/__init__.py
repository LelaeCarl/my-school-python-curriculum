"""
app/__init__.py
"""
import os
# 1. Import Flask framework and render_template to read view files
from flask import Flask, render_template
# 2. Import database connection module
from flask_sqlalchemy import SQLAlchemy
# 3. Import caching module from Flask framework
from flask_redis import FlaskRedis

# Author Information
__author__ = "zpp"

"""
1. Set Project Name
   Instantiate the Flask framework
"""
app = Flask(__name__)  # Instantiate Flask

"""
2. Database Connection Settings
2.1 Configure MySQL connection parameters
    mysql+mysqlconnector => MySQL database + MySQL driver module
    root:mysql => Username and password
    127.0.0.1:3306 => IP address and port
    movie => Database name
"""
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql+pymysql://root:sagemovie@127.0.0.1:3306/movie'
# 2.2 Enable object modification signals in SQLAlchemy
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

"""
3. Configure Project Caching
"""
# 3.1 Set caching URL
app.config['REDIS_URL'] = "redis://127.0.0.1:6379/0"

# 3.2 Set secret key
app.config['SECRET_KEY'] = 'sagemovie'

# 3.3 Configure backend upload directory
# Example: D:/PycharmProjects/JSNUMovie2022/app/static/uploads/zpp.wav
app.config['UP_DIR'] = \
    os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'static/uploads/'
    )

# 3.4 Configure frontend upload directory
app.config['FC_DIR'] = \
    os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'static/uploads/user/'
    )

"""
4. Enable DEBUG Mode
"""
app.debug = False

"""
5. Database Connection Variable
   Associate the database driver with the Flask object
"""
db = SQLAlchemy(app)

"""
6. Cache Mechanism Variable
"""
rd = FlaskRedis(app)

"""
7. Configure Blueprints
   Similar to web.xml for mapping routes
"""
# 7.1 Import blueprint for admin (backend management)
from app.admin import admin as admin_blueprint

# 7.2 Register blueprint for routing
# Example:
# 127.0.0.1:5000/admin => Redirects to admin system
# 127.0.0.1:5000/home => Redirects to display system
app.register_blueprint(admin_blueprint, url_prefix='/admin')
