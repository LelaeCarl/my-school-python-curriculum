"""
Main Entry Point for the Movie Management System Project
"""
from flask_script import Manager
# Import the app instance from the JSNUMovie2022/app package
from app import app

# 1. Create a Manager object with the app instance
MG = Manager(app)

# 2. Run the manager to start the application
if __name__ == '__main__':
    MG.run()
