from wtforms import Form
from wtforms import SelectField, RadioField

class FormResistencia(Form):
    valores = [
        (0, 'Negro'),
        (1, 'Cafe'),
        (2, 'Rojo'),
        (3, 'Naranja'),
        (4, 'Amarillo'),
        (5, 'Verde'), 
        (6, 'Azul'),
        (7, 'Violeta'),
        (8, 'Gris'),
        (9, 'Blanco'),
        ]
    
    tolerancias = [
        (5, 'Oro'), 
        (10, 'Plata')
        ]

    color1 = SelectField('Color 1', choices=valores)
    color2 = SelectField('Color 2', choices=valores)
    color3 = SelectField('Color 3', choices=valores)
    tolerancia = RadioField('Tolerancia', choices=tolerancias, default=5)
