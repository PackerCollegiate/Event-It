from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, DateField, FileField
from wtforms.fields import DateField, FileField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={'style': 'width: 30ch'},)
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'style': 'width: 30ch'},)
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class EventForm(FlaskForm):
    eventName = StringField('Event Name', validators=[DataRequired()])
    eventDate = DateField('Date', validators=[DataRequired()], id='datepick')
    eventImage = FileField("Event Image",) # validators=[DataRequired(['jpg','jpeg','png'])]
    submit = SubmitField('Create Event')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={'style': 'width: 30ch'},)
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={'style': 'width: 30ch'},)
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'style': 'width: 30ch'},)
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')], render_kw={'style': 'width: 30ch'},)
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')

class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')
    
class BlankForm(FlaskForm):
    pass
    
class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Submit')