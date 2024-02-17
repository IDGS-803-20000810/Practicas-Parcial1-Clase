from wtforms import Form
from wtforms import StringField, SelectField, RadioField, EmailField, IntegerField
from wtforms import validators

class GuardarTradForm(Form):
    ing=StringField('Inglés',[
        validators.DataRequired(message='El campo es requerido')
    ])
    esp=StringField('Español',[
        validators.DataRequired(message='El campo es requerido')
    ])

class TradForm(Form):
    palabra=StringField('Palabra',[
        validators.DataRequired(message='el campo es requerido')
    ])
    idioma=RadioField('Idioma',[
        validators.DataRequired(message='el campo es requerido')
    ],
    choices=[("ingles","Inglés"),("espanol","Español")])
