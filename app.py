from flask import Flask, render_template, request, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'super_secret_key'  # Обязательно для сессий

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'submissions' not in session:
        session['submissions'] = []

    if request.method == 'POST':
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')
        timestamp = datetime.now().strftime('%d.%m.%Y %H:%M:%S')

        submission = {
            'name': name,
            'city': city,
            'hobby': hobby,
            'age': age,
            'timestamp': timestamp
        }

        session['submissions'].append(submission)
        session.modified = True

    # Показываем самые свежие записи сверху
    reversed_submissions = session['submissions'][::-1]

    return render_template('index.html', submissions=reversed_submissions)

if __name__ == '__main__':
    app.run(debug=True)