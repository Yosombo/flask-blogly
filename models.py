from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    img_url = db.Column(db.String, nullable=False, default='https://www.google.com/search?q=user+img&rlz=1C5CHFA_enUS823US823&sxsrf=ALeKk00LpMUM2TapAkiyhlCOPT-YHtfs3g:1626244279674&tbm=isch&source=iu&ictx=1&fir=AUgEVRbKL9g9DM%252Ci1aaIre6F5SwWM%252C_&vet=1&usg=AI4_-kS52RayCd-rUFURJ0rKFTh6Y6_30Q&sa=X&ved=2ahUKEwj_he6E-OHxAhVTnJ4KHfLgB-4Q9QF6BAgVEAE&biw=1066&bih=985#imgrc=AUgEVRbKL9g9DM')

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
