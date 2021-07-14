from unittest import TestCase

from app import app
from models import db, User

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_TEST'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()


class User_Model_TestCase(TestCase):
    def setUp(self):
        User.query.delete()

    def tearDown(self):
        db.session.rollback()

    def test_full_name(self):
        user = User(first_name="Amar", last_name="Tsog")
        self.assertEquals(user.get_full_name, "Amar Tsog")

    def test_default_img_url(self):
        user = User(first_name="Amar", last_name="Tsog")
        db.session.add(user)
        db.session.commit()
        self.assertEquals(user.img_url, "https://www.google.com/search?q=user+img&rlz=1C5CHFA_enUS823US823&sxsrf=ALeKk00LpMUM2TapAkiyhlCOPT-YHtfs3g:1626244279674&tbm=isch&source=iu&ictx=1&fir=AUgEVRbKL9g9DM%252Ci1aaIre6F5SwWM%252C_&vet=1&usg=AI4_-kS52RayCd-rUFURJ0rKFTh6Y6_30Q&sa=X&ved=2ahUKEwj_he6E-OHxAhVTnJ4KHfLgB-4Q9QF6BAgVEAE&biw=1066&bih=985#imgrc=AUgEVRbKL9g9DM")
