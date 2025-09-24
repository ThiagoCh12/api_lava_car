from flask import Blueprint, request, jsonify
from ..extensions import db
from ..models import Agendamento

agendamentos_bp = Blueprint("agendamentos", __name__)

@agendamentos_bp.route("/", methods=["POST"])
def criar_agendamento():
    rq = request.get_json()
    agendamento = Agendamento(data=rq["data"], cliente_id=rq["cliente_id"])
    db.session.add(agendamento)
    db.session.commit()

    return jsonify({"id":agendamento.id, 
                    "data":str(agendamento.data), 
                    "cliente_id":agendamento.cliente_id
    }), 201

@agendamentos_bp.route("/", methods=["GET"])
def listar_agendamentos():
    agendamentos = Agendamento.query.all()
    return jsonify([{"id":a.id, "data":str(a.data), "cliente_id":a.cliente_id}for a in agendamentos])

@agendamentos_bp.route("/<int:id>", methods=["GET"])
def obter_agendamento(id):
    agendamento = Agendamento.query.get_or_404(id)
    return jsonify({
        "id": agendamento.id,
        "data": str(agendamento.data),
        "cliente_id": agendamento.cliente_id
    })

@agendamentos_bp.route("/<int:id>", methods=["PUT"])
def atualizar_agendamento(id):
    rq = request.get_json()
    agendamento = Agendamento.query.get_or_404(id)

    if "data" in rq:
        agendamento.data = rq["data"]
    if "cliente_id" in rq:
        agendamento.cliente_id = rq["cliente_id"]

    db.session.commit()
    return jsonify({
        "id": agendamento.id,
        "data": str(agendamento.data),
        "cliente_id": agendamento.cliente_id
    })

@agendamentos_bp.route("/<int:id>", methods=["DELETE"])
def deletar_agendamento(id):
    agendamento = Agendamento.query.get_or_404(id)
    db.session.delete(agendamento)
    db.session.commit()
    return jsonify({"mensagem": f"Agendamento {id} deletado com sucesso"})
