'''
app/admin/__init.py
'''

from flask import Blueprint
#set the blueprint for the current module, called admin
admin = Blueprint("admin",__name__)
#127.0.0.1:500/admin/login

#set the view management file for the current blueprint
import app.admin.views
