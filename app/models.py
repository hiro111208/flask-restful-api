from app import db, app, ma
from sqlalchemy import Column, Integer, String, Float


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(100), unique=True)
    password = Column(String(100))


class Planet(db.Model):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    type = Column(String(100))
    home_star = Column(String(100))
    mass = Column(Float)
    radius = Column(Float)
    distance = Column(Float)


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'password')


class PlanetSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'type', 'home_star',
                  'mass', 'radius', 'distance')


user_schema = UserSchema()
users_schema = UserSchema(many=True)

planet_schema = PlanetSchema()
planets_schema = PlanetSchema(many=True)


@app.cli.command('/db_create')
def db_create():
    db.create_all()
    print('Database created!')


@app.cli.command('/db_drop')
def db_drop():
    db.drop_all()
    print('Database dropped!')


@app.cli.command('/db_seed')
def db_seed():
    mercury = Planet(
        name='Mercury',
        type='Class D',
        home_star='Sol',
        mass=3.258e23,
        radius=1516,
        distance=35.98e6
    )

    venus = Planet(
        name='Venus',
        type='Class K',
        home_star='Sol',
        mass=4.867e24,
        radius=3760,
        distance=67.24e6
    )

    earth = Planet(
        name='Earth',
        type='Class M',
        home_star='Sol',
        mass=5.972e24,
        radius=3959,
        distance=92.96e6
    )

    db.session.add(mercury)
    db.session.add(venus)
    db.session.add(earth)

    test_user = User(
        first_name='William',
        last_name='Herschel',
        email='test@test.com',
        password='password'
    )

    db.session.add(test_user)
    db.session.commit()
    print('Database seeded!')
