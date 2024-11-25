from flask import Flask, render_template, redirect, url_for, request
from forms import FeedbackForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

reviews = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        reviews.append({
            'name': form.name.data,
            'rating': form.rating.data,
            'comment': form.comment.data
        })
        return redirect(url_for('reviews'))
    return render_template('feedback.html', form=form)

@app.route('/reviews')
def reviews_page():
    return render_template('reviews.html', reviews=reviews)

if __name__ == '__main__':
    app.run(debug=True)
