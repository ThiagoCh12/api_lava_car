from .extensions import db

class Agendamento(db.Model):
    __tablename__ = "agendamentos"

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey("clientes.id"), nullable=False)

class Carro(db.Model):
    __tablename__ = "carros"

    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(100), nullable=False)
    marca = db.Column(db.String(30), nullable=False)
    placa = db.Column(db.String(10), nullable=False)

    cliente_id = db.Column(db.Integer, db.ForeignKey("clientes.id"), nullable=False)

class Cliente(db.Model):
    __tablename__ = "clientes"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)

    carros = db.relationship("Carro", backref="dono", lazy=True, cascade="all, delete-orphan")
    agendamentos = db.relationship("Agendamento", backref="cliente", lazy=True, cascade="all, delete-orphan")




