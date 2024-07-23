from wtforms import Form, StringField, IntegerField, SelectField, validators

class RealtyForm(Form):
    name = StringField('Name', [validators.DataRequired(message="The field 'Name' cannot be empty"), validators.Length(min=1, max=50)])
    property_type = StringField('Type', [validators.DataRequired(message="The field 'Type' cannot be empty")])
    square = IntegerField('Square', [validators.DataRequired(message="The field 'Square' must be an integer")])
    bathrooms = IntegerField('Bathrooms', [validators.DataRequired(message="The field 'Bathrooms' must be an integer")])
    bedrooms = IntegerField('Bedrooms', [validators.DataRequired(message="The field 'Bedrooms' must be an integer")])
    water_supply = StringField('Water Supply', [validators.DataRequired(message="The field 'Water Supply' cannot be empty")])
    electricity = StringField('Electricity', [validators.DataRequired(message="The field 'Electricity' cannot be empty")])
    straits = StringField('Straits', [validators.DataRequired(message="The field 'Straits' cannot be empty")])
    kitchen_squares = IntegerField('Kitchen Square', [validators.DataRequired(message="The field 'Kitchen Square' must be an integer")])
