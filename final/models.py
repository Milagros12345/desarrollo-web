from flask_sqlalchemy import SQLAlchemy 
from werkzeug.security import generate_password_hash,check_password_hash
import datetime
db = SQLAlchemy()

class participante(db.Model):
    __tablename__ = "participantes"
    dni = db.Column(db.String(8), primary_key=True, nullable=False)
    nombre = db.Column(db.String(30), nullable=False)
    apellido_p = db.Column(db.String(20), nullable=False)
    apellido_m = db.Column(db.String(20), nullable=False)
    categoria=db.Column(db.String(20), nullable=False)
    email=db.Column(db.String(60),nullable=False)
    evento=db.Column(db.Integer, db.ForeignKey('eventos.id'))

class evento(db.Model):
    __tablename__ = "eventos"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    ubicacion = db.Column(db.String(40), nullable=False)
    fecha= db.Column(db.String(10), nullable=False)
    hora = db.Column(db.String(8), nullable=False)
    monto=db.Column(db.Float(10),nullable=False)
    

tags = db.Table('inscritos',
    db.Column('id_e', db.Integer, db.ForeignKey('eventos.id'), primary_key=True),
    db.Column('id_p', db.String, db.ForeignKey('participantes.dni'), primary_key=True),
    db.Column('fecha',db.String(10), nullable=False),
    db.Column('monto',db.Float(10), nullable =False)
    
)

class User(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)

