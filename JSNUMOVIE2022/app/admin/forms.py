'''
forms
The Flask framework does not provide comprehensive form validation internally, and requires third-party plugins to handle it.
A recommended form validation plugin is WTForms.
WTForms is a form component that supports multiple web frameworks and is primarily used for validating user-requested data.
WTForms is categorized by function into the following categories:
Forms: Primarily used for form validation, field definitions, HTML generation, and grouping various validation processes together.
Fields: Mainly responsible for rendering (generating HTML) and data conversion.
Validator: Mainly validates the legitimacy of user-inputted data, such as Length validator for length checks.
Widgets: HTML plugins that allow users to customize small HTML components in fields through this dictionary.
Extensions: A rich library of extensions that can be combined with other frameworks.
'''


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, FileField
from wtforms.validators import DataRequired, ValidationError
# 1. Administrator login form
from app.models import Admin, Tag


class LoginForm(FlaskForm):
    # 1.1 Account
    account = StringField(
        label="Account",
        validators=[DataRequired("Account cannot be empty!!!")],
        description="Administrator account",
        render_kw={
            'class': 'form-control',
            'placeholder': "Please enter the administrator account"
        }
    )
    # 1.2 Password
    pwd = PasswordField(
        label="Password:",
        validators=[DataRequired("Password cannot be empty!!")],
        description="Administrator password",
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

    # 1.4 Check if account data exists (field is the account file object)
    def validate_account(self, field):
        # 1.4.1 Get the account value, which is the value entered by the user in the text box
        account = field.data
        # 1.4.2 Query the data based on the account
        admin = Admin.query.filter_by(name=account).count()
        # 1.4.3 Check if it's empty
        if admin == 0:
            raise ValidationError("Account does not exist！！！！")


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

# 3. Movie form
class MovieForm(FlaskForm):
    # 3.1 Movie title
    title = StringField(
        label="Movie Title",
        validators=[DataRequired("Movie title cannot be empty！！！")],
        description="Movie name",
        render_kw={
            'class': 'form-control',
            'id': 'input_title',
            'placeholder': 'Please enter the movie title'
        }
    )
    # 3.2 Movie storage path (local path)
    url = FileField(
        label="Movie File",
        validators=[DataRequired("Please upload a file")],
        description='Movie file'
    )
    # 3.3 Movie summary
    info = TextAreaField(
        label="Movie Summary",
        validators=[DataRequired("Summary cannot be empty")],
        description="Movie summary",
        render_kw={
            'class': 'form-control',
            'rows': 10
        }
    )
    # 3.4 Movie poster
    logo = FileField(
        label="Movie Poster",
        validators=[DataRequired("Please upload a movie poster")],
        description="Movie poster"
    )
    # 3.5 Movie star rating
    star = SelectField(
        label="Star Rating",
        validators=[DataRequired("Please select a star rating")],
        coerce=int,
        choices=[(1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars')],
        description="Star rating",
        render_kw={
            'class': 'form-control'
        }
    )
    # 3.6 Movie tag
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
    # 3.8 Movie duration
    length = StringField(
        label="Movie Duration",
        validators=[DataRequired("Duration cannot be empty!!!")],
        description='Movie duration',
        render_kw={
            'class': 'form-control',
            'placeholder': 'Please enter the movie duration!!!'
        }
    )
    # 3.9 Release time
    release_time = StringField(
        label="Release Time",
        validators=[DataRequired("Release time cannot be empty!!!")],
        description="Release time",
        render_kw={
            'class': 'form-control',
            'placeholder': "Please select the release time",
            'id': 'input_release_time',
        }
    )
    # 3.10 Button
    submit = SubmitField(
        label='Add',
        render_kw={
            'class': 'btn btn-primary'
        }
    )

# 4. Preview form
class PreviewForm(FlaskForm):
    title = StringField(
        label="Preview Title",
        validators=[DataRequired("Preview title cannot be empty!!")],
        description="Preview title of upcoming movie",
        render_kw={
            'class': 'form-control',
            'placeholder': 'Please enter the preview title'
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

# 5. Permission form
class AuthForm(FlaskForm):
    name = StringField(
        label="Permission Name",
        validators=[DataRequired("Permission name cannot be empty!!")],
        description="Permission name",
        render_kw={
            'class': 'form-control',
            'placeholder': 'Please enter the permission name'
        }
    )
    url = StringField(
        label="Permission URL",
        validators=[DataRequired("Permission URL cannot be empty!!")],
        description="Permission URL",
        render_kw={
            'class': 'form-control',
            'placeholder': 'Please enter the permission URL'
        }
    )
    submit = SubmitField(
        label='Add Permission',
        render_kw={
            'class': 'btn btn-primary'
        }
    )
