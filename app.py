from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config["SECRET_KEY"] = "12345679"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)


connect_db(app)
db.create_all()


@app.route('/')
def show_home():
    return redirect('/users')


@app.route('/users')
def show_users():
    users = User.query.order_by(User.first_name).all()
    return render_template('users.html', users=users)


@app.route('/users/new')
def add_user():
    users = User.query.all()
    return render_template('add_user.html')


@app.route('/users/new', methods=["POST"])
def post_user():
    if request.form["first_name"] != '' and request.form["first_name"] != '':
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        img_url = request.form["img_url"]
        new_user = User(first_name=first_name,
                        last_name=last_name, img_url=img_url)
        db.session.add(new_user)
        db.session.commit()
    return redirect('/users')


@app.route('/users/<int:user_id>')
def show_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user.html', user=user)


@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    user = User.query.get(user_id)

    return render_template('edit_user.html', user=user)


@app.route('/users/<int:user_id>/edit', methods=['POST'])
def post_edited_user(user_id):
    if request.form["first_name"] != '' and request.form["first_name"] != '':
        user = User.query.filter(User.id == user_id).one()
        user.first_name = request.form["first_name"]
        user.last_name = request.form["last_name"]
        user.img_url = request.form["img_url"]
        db.session.commit()
    return redirect(f'/users/{user_id}')


@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    User.query.filter(User.id == user_id).delete()
    db.session.commit()
    return redirect('/users')
