from flask_wtf import FlaskForm, CSRFProtect
from flask_wtf.form import _Auto
from wtforms import FieldList, FloatField, FormField, StringField, PasswordField, TextAreaField, SelectField, SubmitField, EmailField, TelField, URLField, validators
from wtforms.validators import DataRequired

class SignUpForm(FlaskForm):
    id = StringField('Username', validators=[DataRequired()])
    description = StringField('Business Description', validators=[DataRequired()])
    representative_name = StringField('Representative Name', validators=[DataRequired()])
    email = EmailField('Contact Email', validators=[DataRequired()])
    phone = TelField('Phone Number', validators=[DataRequired()])
    address = StringField('Business Address', validators=[DataRequired()])
    city = StringField('City of Operations', validators=[DataRequired()])
    state = StringField('State of Operations', validators=[DataRequired()])
    website = URLField('Company Website', validators=[DataRequired()])
    passwd = PasswordField('Password', validators=[DataRequired()])
    passwd_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Confirm')

class LoginForm(FlaskForm):
    id = StringField('Username', validators=[DataRequired()])
    passwd = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Confirm')

class CreateOffer(FlaskForm):
    # code should be auto generated (?)
    description = StringField('Description', validators=[DataRequired()])
    year = StringField('Year', validators=[DataRequired()])
    productType = StringField("Type", validators=[DataRequired()])
    brand = StringField("Brand", validators=[DataRequired()])
    price = FloatField("Price", validators=[DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = StringField('Write your comment here.', validators=[DataRequired()])
    stars = SelectField("Star Rating", choices=[(1, "1 - Bad"), (2, "2 - Fair"), (3, "3 - Good"), (4, "4 - Great"), (5, "5 - Excellent")])
    comment = StringField('Write Your Comment here', validators=[DataRequired()])
    submit = SubmitField('Confirm')

class ReplyForm(FlaskForm):
    comment =StringField('Write your comment here.', validators=[DataRequired()])
    submit = SubmitField('Confirm')
