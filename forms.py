from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class FeedbackForm(FlaskForm):
    name = StringField('Ваше ім\'я', validators=[DataRequired(), Length(max=50)])
    rating = SelectField('Оцінка', choices=[('5', '5 - Відмінно'), ('4', '4 - Добре'), ('3', '3 - Задовільно'), ('2', '2 - Погано'), ('1', '1 - Жахливо')], validators=[DataRequired()])
    comment = TextAreaField('Коментар', validators=[DataRequired(), Length(max=500)])
    submit = SubmitField('Надіслати')
