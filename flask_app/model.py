from wtforms import Form, FloatField, validators
from math import pi

class InputForm(Form):
    userID = FloatField(
        label='User Id: ',
        validators=[validators.InputRequired("Plase enter your user id")])
    signatureURL = FloatField(
        label='', default="",
        validators=[validators.InputRequired("Give Signature Path: ")])
    