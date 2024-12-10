'''
forms
The Flask framework does not provide comprehensive form validation internally, so third-party plugins are needed to handle this.
A recommended form validation plugin is WTForms.
WTForms is a form component that supports multiple web frameworks and is mainly used for validating user-submitted data.
WTForms is categorized by functionality into the following categories:
Forms: Mainly used for form validation, field definitions, HTML generation, and grouping various validation processes together.
Fields: Responsible for rendering (generating HTML) and data transformation (e.g., zpp ==> account = "zpp").
Validator: Primarily validates the legality of user input data, such as Length validator for length validation.
Widgets: HTML plugins that allow users to customize small HTML parts in fields through this dictionary.
Extensions: Rich extension libraries that can be combined with other frameworks.

Break time for practice - 20 minutes. Class resumes at 15:25.
'''
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.models import Admin

# 1. Admin Login Form
class LoginForm(FlaskForm):
    # 1.1 Account
    account = StringField(
        label="Account",
        validators=[DataRequired("Account cannot be empty!!!")],
        description="Admin account",
        render_kw={
            'class': 'form-control',
            'placeholder': "Please enter the admin account"
        }
    )
    # 1.2 Password
    pwd = PasswordField(
        label="Password:",
        validators=[DataRequired("Password cannot be empty!!")],
        description="Admin password",
        render_kw={
            'class': 'form-control',
            'placeholder': "Please enter the user password"
        }
    )
    # 1.3 Submit Button
    submit = SubmitField(
        label="Login",
        render_kw={
            'class': 'btn btn-primary btn-block btn-flat'
        }
    )
    # 1.4 Validate if the account exists (field is the account file object)
    def validate_account(self, field):
        # 1.4.1 Get the account value from user input
        account = field.data
        # 1.4.2 Query the database for the account
        admin = Admin.query.filter_by(name=account).count()
        # 1.4.3 Check if the account exists
        if admin == 0:
            raise ValidationError("Account does not exist!!!!")

# 2. Tag Form
class TagForm(FlaskForm):
    name = StringField(
        label='Movie Tag',
        validators=[DataRequired('Tag name cannot be empty!!!!')],
        description='Movie tag',
        render_kw={
            'class': 'form-control',
            'id': 'input_name',
            'placeholder': 'Please enter the movie tag name!!!'
        }
    )
    submit = SubmitField(
        label="Add",
        render_kw={'class': 'btn btn-primary'}
    )
