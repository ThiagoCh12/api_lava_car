from flask import Blueprint, request, jsonify
from ..extensions import db
from ..models import Carro

carros_bp = Blueprint("carros", __name__)

@carros_bp.route("/", methods=["POST"])
def criar_carro():
    data = request.get_json()
    carro = Carro(modelo=data["modelo"], marca=data["marca"], placa=data["placa"], cliente_id=data["cliente_id"])
    db.session.add(carro)
    db.session.commit()
    return jsonify({"id":carro.id, "modelo":carro.modelo, "placa":carro.placa, "cliente_id":carro.cliente_id}), 201

@carros_bp.route("/", methods=["GET"])
def listar_carros():
    carros = Carro.query.all()
    return jsonify([{"id":c.id, "modelo":c.modelo, "marca":c.marca, "placa":c.placa, "dono_id":c.cliente_id}for c in carros])
