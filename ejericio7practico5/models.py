from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Usuarios(db.Model):
    DNI = db.Column(db.Integer, primary_key=True)
    Clave = db.Column(db.String(100), nullable=False)
    Tipo = db.Column(db.String(50), nullable=False)
    pedidos = db.relationship('Pedidos', backref='usuarios')

class Pedidos(db.Model):
    NumPedido = db.Column(db.Integer, primary_key=True)
    Fecha = db.Column(db.Date, nullable=False)
    Total = db.Column(db.Float, nullable=False)
    Cobrado = db.Column(db.Boolean, nullable=False)
    Observacion = db.Column(db.Text)
    DNIMozo = db.Column(db.Integer, db.ForeignKey('usuarios.DNI'))
    Mesa = db.Column(db.Integer, nullable=False)
    Item = db.relationship('ItemsPedidos', backref='pedidos', cascade='all, delete-orphan', lazy='dynamic')

class Productos(db.Model):
    NumProducto = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(30), nullable=False)
    PrecioUnitario = db.Column(db.Float, nullable=False)
    Item = db.relationship('ItemsPedidos', backref='productos', cascade='all, delete-orphan', lazy='dynamic')

class ItemsPedidos(db.Model):
    __tablename__= 'ItemsPedidos'
    NumItem = db.Column(db.Integer, primary_key=True)
    NumPedido = db.Column(db.Integer, db.ForeignKey('pedidos.NumPedido'))
    NumProducto = db.Column(db.Integer, db.ForeignKey('productos.NumProducto'))
    Precio = db.Column(db.Float, nullable=False)
    Estado = db.Column(db.String(20), nullable=False)
