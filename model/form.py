from wtforms import Form, BooleanField, StringField,SelectField,SubmitField,validators

ROLE_CHOICES = [(False,'User'), (True,'Admin')]

class RegistrationForm(Form):
    username     = StringField(
                    'Username', 
                    [validators.Length(min=4, max=25)],
                    render_kw={'class':'form-control'})
    password     = StringField(
                    'Password',
                    [validators.Length(min=6, max=35)],
                    render_kw={'class':'form-control'})
    role         = SelectField(
                    u'Role', 
                    choices=ROLE_CHOICES,
                    coerce=bool,
                    render_kw={'class':'form-control'})
    button       = SubmitField(
                    'Submit',
                    render_kw={'class':'btn btn-primary form-control',
                        'style':"margin-top: 15px;",
                        'type':'submit'})
class LoginForm(Form):
    username     = StringField(
                    'Username', 
                    [validators.Length(min=4, max=25)],
                    render_kw={'class':'form-control'})
    password     = StringField(
                    'Password', 
                    [validators.Length(min=6, max=35)],
                    render_kw={'class':'form-control'})
    button       = SubmitField(
                    'Submit',
                    render_kw={'class':'btn btn-primary form-control',
                        'style':"margin-top: 15px;",
                        'type':'submit'})
                    