from models import User, db
from app import app

db.drop_all()
db.create_all()

User.query.delete()

puje = User(first_name='Puje',
            last_name='Gana')
db.session.add(puje)
soyo = User(first_name='Soyo',
            last_name='Enk')
db.session.add(soyo)
amar = User(first_name='Amar',
            last_name='Tsog')
db.session.add(amar)
anny = User(first_name='Anny',
            last_name='Amar')
db.session.add(anny)
db.session.commit()
