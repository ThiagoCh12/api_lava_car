from flask import Blueprint, jsonify, request
from ..extensions import db
from ..models import Cliente

clientes_bp =  Blueprint("clientes", __name__)

@clientes_bp.route("/", methods=["POST"])
def criar_cliente():
    data = request.get_json()
    cliente = Cliente(nome=data["nome"], telefone=data["telefone"])
    db.session.add(cliente)
    db.session.commit()

    return jsonify({"id":cliente.id, "nome":cliente.nome, "telefone":cliente.telefone}), 201

@clientes_bp.route("/", methods=["GET"])
def listar_clientes():
    clientes = Cliente.query.all()
    return jsonify([{"id":c.id, "nome":c.nome, "telefone":c.telefone} for c in clientes])