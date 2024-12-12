from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField, SelectField
from wtforms.validators import DataRequired, ValidationError
from app.models import Admin, Tag

# Flask framework does not provide comprehensive form validation internally. Third-party plugins are needed.
# The official recommendation is a form validation plugin called WTForms.
# WTForms is a form component that supports various web frameworks, primarily used for validating user-requested data.
# WTForms is classified into the following categories by functionality:
# Forms: Mainly used for form validation, field definition, HTML generation, and integrating various validation processes.
# Fields: Primarily responsible for rendering (generating HTML) and data conversion, e.g., account = "zpp".
# Validator: Mainly validates the legitimacy of user input data, such as the Length validator.
# Widgets: HTML plugins that allow users to customize small parts of HTML in the fields.
# Extensions: A rich library of extensions that can be used with other frameworks.

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
    # 1.3 Button
    submit = SubmitField(
        label="Login",
        render_kw={
            'class': 'btn btn-primary btn-block btn-flat'
        }
    )
    # 1.4 Validate whether account exists (field is the account field object)
    def validate_account(self, field):
        # 1.4.1 Get the value of the account input by the user in the text box
        account = field.data
        # 1.4.2 Query the database for the account value
        admin = Admin.query.filter_by(name=account).count()
        # 1.4.3 Check if the account exists
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
            'placeholder': 'Please enter the movie tag name!!!'
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
        description="Movie name",
        render_kw={
            'class': 'form-control',
            'id': 'input_title',
            'placeholder': 'Please enter the title'
        }
    )
    # 3.2 Movie Storage Path (Local Path)
    url = FileField(
        label="Movie File",
        validators=[DataRequired("Please upload a file")],
        description='Movie file'
    )
    # 3.3 Movie Synopsis
    info = TextAreaField(
        label="Movie Synopsis",
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
        validators=[DataRequired("Please upload the movie poster")],
        description="Movie poster"
    )
    # 3.5 Movie Star Rating
    star = SelectField(
        label="Star Rating",
        validators=[DataRequired("Please select a star rating")],
        coerce=int,
        choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')],
        description="Star rating",
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
        validators=[DataRequired("Please enter the region")],
        description='Region',
        render_kw={
            'class': 'form-control',
            'placeholder': "Please enter the region"
        }
    )
    # 3.8 Movie Duration
    length = StringField(
        label="Movie Duration",
        validators=[DataRequired("Duration cannot be empty!!!")],
        description='Movie duration',
        render_kw={
            'class': 'form-control',
            'placeholder': 'Please enter the movie duration!!!'
        }
    )
    # 3.9 Release Date
    release_time = StringField(
        label="Release Date",
        validators=[DataRequired("Release date cannot be empty!!!")],
        description="Release date",
        render_kw={
            'class': 'form-control',
            'placeholder': "Please select the release date",
            'id': 'input_release_time'
        }
    )
    # 3.10 Button
    submit = SubmitField(
        label='Add',
        render_kw={
            'class': 'btn btn-primary'
        }
    )
