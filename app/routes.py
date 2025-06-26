from flask import render_template, request
from app import app, db
from app.models import User

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')

        user = User(name=name, city=city, hobby=hobby, age=int(age))
        db.session.add(user)
        db.session.commit()

    users = User.query.order_by(User.id.desc()).all()  # последние сверху
    return render_template('form.html', users=users)


