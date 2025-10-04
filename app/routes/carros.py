from flask import Blueprint, request, jsonify
from ..extensions import db
from ..models import Carro

carros_bp = Blueprint("carros", __name__, url_prefix="/carros")

@carros_bp.route("/", methods=["POST"])
def criar_carro():
    data = request.get_json()
    carro = Carro(modelo=data["modelo"], marca=data["marca"], placa=data["placa"], cliente_id=data["cliente_id"])
    db.session.add(carro)
    db.session.commit()
    return jsonify({"id":carro.id, 
                    "modelo":carro.modelo, 
                    "marca":carro.marca, 
                    "placa":carro.placa, 
                    "cliente_id":carro.cliente_id}), 201

@carros_bp.route("/", methods=["GET"])
def listar_carros():
    carros = Carro.query.all()
    return jsonify([{"id":c.id, 
                     "modelo":c.modelo, 
                     "marca":c.marca, 
                     "placa":c.placa, 
                     "cliente_id":c.cliente_id}for c in carros]), 200

@carros_bp.route("/<int:id>", methods=["GET"])
def buscar_carro(id):
    try:
        carro = Carro.query.get(id)
        if carro is not None:
            return jsonify({"id":carro.id, 
                            "modelo":carro.modelo, 
                            "marca":carro.marca, 
                            "placa":carro.placa, 
                            "cliente_id":carro.cliente_id}), 200
        else:
            return jsonify({"Erro": "Carro não encontrado"}), 404 
    except Exception as e:
        return jsonify({"Erro": str(e)}), 500

@carros_bp.route("/<int:id>", methods=["PUT"])
def editar_carro(id):
    try:
        carro = Carro.query.get(id)
        if carro is not None:
            rq = request.get_json()
            if "modelo" in rq:
                carro.modelo = rq["modelo"]
            if "marca" in rq:
                carro.marca = rq["marca"]
            if "placa" in rq:
                carro.placa = rq["placa"]
            db.session.commit()
            return jsonify({"id":carro.id, 
                            "modelo":carro.modelo, 
                            "marca":carro.marca, 
                            "placa":carro.placa, 
                            "cliente_id":carro.cliente_id}), 200
        else:
            return jsonify({"Erro":"Carro não encontrado"}), 404 
    except Exception as e:
        return jsonify({"Erro":str(e)}),500

@carros_bp.route("/<int:id>", methods=["DELETE"])
def excluir_carro(id):
    try:
        carro = Carro.query.get(id)
        if carro is not None:
            db.session.delete(carro)
            db.session.commit()
            return jsonify({"Mensagem":f"Carro id {id} excluído com sucesso!"}),200
        else:
            return jsonify({"Erro":"Carro não encontrado"}), 404
    except Exception as e:
        return jsonify({"Erro": str(e)}),500