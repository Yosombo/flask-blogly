from unittest import TestCase

from app import app
from models import db, User

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_TEST'
app.config['SQLALCHEMY_ECHO'] = False
app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']
db.drop_all()
db.create_all()


class User_views_Testcase(TestCase):
    def setUp(self):
        User.query.delete()
        user = User(first_name="Amar", last_name="Tsog")

        db.session.add(user)
        db.session.commit()
        self.user_id = user.id

    def tearDown(self):
        db.session.rollback()

    def test_root(self):
        with app.test_client() as client:

            resp = client.get("/", follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertAlmostEqual(resp.status_code, 200)
            self.assertIn(
                '<a href="/users/new"><button class="main_btn">Add a user</button></a>', html)

    def test_users(self):
        with app.test_client() as client:

            resp = client.get("/users")
            html = resp.get_data(as_text=True)

            self.assertAlmostEqual(resp.status_code, 200)
            self.assertIn(
                '>Amar Tsog</a>', html)

    def test_users_new(self):
        with app.test_client() as client:

            resp = client.get("/users/new")
            html = resp.get_data(as_text=True)

            self.assertAlmostEqual(resp.status_code, 200)
            self.assertIn(
                '<form action="/users/new" method="POST">', html)

    def test_users_new_post(self):
        with app.test_client() as client:
            user = User(first_name="Anny", last_name="Kim")

            db.session.add(user)
            db.session.commit()
            resp = client.get("/users", follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertAlmostEqual(resp.status_code, 200)
            self.assertIn("Anny Kim", html)

    def test_users_edit(self):
        with app.test_client() as client:
            user = User.query.filter(User.first_name == "Amar").one()
            user.first_name = "Gerel"
            db.session.commit()
            resp = client.get("/users", follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertAlmostEqual(resp.status_code, 200)
            self.assertIn("Gerel Tsog", html)
