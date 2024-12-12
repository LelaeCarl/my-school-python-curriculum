'''
Forms
The Flask framework does not provide comprehensive form validation internally; a third-party plugin is needed.
The officially recommended plugin for form validation is WTForms.
WTForms is a form component that supports multiple web frameworks, primarily used to validate data from user requests.
WTForms categorizes functionalities as follows:

Forms: Primarily used for form validation, field definitions, HTML generation, and integrating various validation processes.
Fields: Responsible for rendering (generating HTML) and data conversion, e.g., zpp ===> account = "zpp".
Validators: Primarily used to validate the legality of user input, such as the Length validator.
Widgets: HTML plugins allowing customization of small parts of HTML within fields through a dictionary.
Extensions: Rich libraries for integration with other frameworks.

Break for 20 minutes. Class resumes at 15:25.
'''

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField, SelectField
from wtforms.validators import DataRequired, ValidationError
from app.models import Admin, Tag

# 1. Admin Login Form
class LoginForm(FlaskForm):
    # 1.1 Account
    account = StringField(
        label="Account",
        validators=[DataRequired("Account cannot be empty!!!")],
        description="Admin account",
        render_kw={
            'class': 'form-control',
            'placeholder': "Enter admin account"
        }
    )
    # 1.2 Password
    pwd = PasswordField(
        label="Password:",
        validators=[DataRequired("Password cannot be empty!!")],
        description="Admin password",
        render_kw={
            'class': 'form-control',
            'placeholder': "Enter user password"
        }
    )
    # 1.3 Submit button
    submit = SubmitField(
        label="Login",
        render_kw={
            'class': 'btn btn-primary btn-block btn-flat'
        }
    )
    # 1.4 Validate if account exists (field is the account input field object)
    def validate_account(self, field):
        # 1.4.1 Get the value of the account entered by the user
        account = field.data
        # 1.4.2 Query the database for the account
        admin = Admin.query.filter_by(name=account).count()
        # 1.4.3 Check if it exists
        if admin == 0:
            raise ValidationError("Account does not exist!!!!")

# 2. Tag Form
class TagForm(FlaskForm):
    name = StringField(
        label='Movie Tag',
        validators=[DataRequired('Tag name cannot be empty!!!!')],
        description='Tag for the movie',
        render_kw={
            'class': 'form-control',
            'id': 'input_name',
            'placeholder': 'Enter movie tag name!!!'
        }
    )
    submit = SubmitField(
        label="Add",
        render_kw={'class': 'btn btn-primary'}
    )

# 3. Movie Form
class MovieForm(FlaskForm):
    # 3.1 Movie Title
    title = StringField(
        label="Title",
        validators=[DataRequired("Title cannot be empty!!!")],
        description="Movie title",
        render_kw={
            'class': 'form-control',
            'id': 'input_title',
            'placeholder': 'Enter title'
        }
    )
    # 3.2 Movie File Path (local path)
    url = FileField(
        label="Movie File",
        validators=[DataRequired("Please upload a file")],
        description='Movie file'
    )
    # 3.3 Movie Synopsis
    info = TextAreaField(
        label="Synopsis",
        validators=[DataRequired("Synopsis cannot be empty")],
        description="Movie synopsis",
        render_kw={
            'class': 'form-control',
            'rows': 10
        }
    )
    # 3.4 Movie Poster
    logo = FileField(
        label="Movie Poster",
        validators=[DataRequired("Please upload a movie poster")],
        description="Movie poster"
    )
    # 3.5 Movie Rating
    star = SelectField(
        label="Rating",
        validators=[DataRequired("Please select a rating")],
        coerce=int,
        choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')],
        description="Rating",
        render_kw={
            'class': 'form-control'
        }
    )
    # 3.6 Movie Tag
    tag_id = SelectField(
        label="Tag",
        validators=[DataRequired("Please select a movie tag")],
        coerce=int,
        choices=[(v.id, v.name) for v in Tag.query.all()],
        description='Movie tag',
        render_kw={
            'class': 'form-control'
        }
    )
    # 3.7 Region
    area = StringField(
        label="Region",
        validators=[DataRequired("Enter a region")],
        description='Region',
        render_kw={
            'class': 'form-control',
            'placeholder': "Enter region"
        }
    )
    # 3.8 Movie Duration
    length = StringField(
        label="Duration",
        validators=[DataRequired("Duration cannot be empty!!!")],
        description='Movie duration',
        render_kw={
            'class': 'form-control',
            'placeholder': 'Enter movie duration!!!'
        }
    )
    # 3.9 Release Date
    release_time = StringField(
        label="Release Date",
        validators=[DataRequired("Release date cannot be empty!!!")],
        description="Release date",
        render_kw={
            'class': 'form-control',
            'placeholder': "Select release date",
            'id': 'input_release_time'
        }
    )
    # 3.10 Submit Button
    submit = SubmitField(
        label='Add',
        render_kw={
            'class': 'btn btn-primary'
        }
    )

# 4. Preview Form
class PreviewForm(FlaskForm):
    title = StringField(
        label="Preview Title",
        validators=[DataRequired("Preview title cannot be empty!!!")],
        description="Title for the preview of the upcoming movie",
        render_kw={
            'class': 'form-control',
            'placeholder': 'Enter preview title'
        }
    )
    logo = FileField(
        label='Preview Poster',
        validators=[DataRequired('Preview poster cannot be empty')],
        description='Preview poster'
    )
    submit = SubmitField(
        label='Add Preview',
        render_kw={
            'class': 'btn btn-primary'
        }
    )
