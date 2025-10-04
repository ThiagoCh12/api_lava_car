from flask import Blueprint, request, jsonify
from ..extensions import db
from ..models import Agendamento

agendamentos_bp = Blueprint("agendamentos", __name__, url_prefix="/agendamentos")

@agendamentos_bp.route("/", methods=["POST"])
def criar_agendamento():
    try:
        rq = request.get_json()
        agendamento = Agendamento(data=rq["data"], cliente_id=rq["cliente_id"])
        db.session.add(agendamento)
        db.session.commit()
        return jsonify({
            "id": agendamento.id,
            "data": agendamento.data.isoformat(),
            "cliente_id": agendamento.cliente_id}), 201
    except Exception as e:
        return jsonify({"Erro": str(e)}), 500

@agendamentos_bp.route("/", methods=["GET"])
def listar_agendamentos():
    try:
        agendamentos = Agendamento.query.all()
        return jsonify([{
            "id": a.id,
            "data": a.data.isoformat(),
            "cliente_id": a.cliente_id} for a in agendamentos]), 200
    except Exception as e:
        return jsonify({"Erro": str(e)}), 500

@agendamentos_bp.route("/<int:id>", methods=["GET"])
def buscar_agendamento(id):
    try:
        agendamento = Agendamento.query.get(id)
        if agendamento is not None:
            return jsonify({
                "id": agendamento.id,
                "data": agendamento.data.isoformat(),
                "cliente_id": agendamento.cliente_id}), 200
        else:
            return jsonify({"Erro": "Agendamento não encontrado"}), 404
    except Exception as e:
        return jsonify({"Erro": str(e)}), 500

@agendamentos_bp.route("/<int:id>", methods=["PUT"])
def editar_agendamento(id):
    try:
        rq = request.get_json()
        agendamento = Agendamento.query.get(id)
        if agendamento is not None:
            if "data" in rq:
                agendamento.data = rq["data"]
            if "cliente_id" in rq:
                agendamento.cliente_id = rq["cliente_id"]
            db.session.commit()
            return jsonify({
                "id": agendamento.id,
                "data": agendamento.data.isoformat(),
                "cliente_id": agendamento.cliente_id}), 200
        else:
            return jsonify({"Erro": "Agendamento não encontrado"}), 404
    except Exception as e:
        return jsonify({"Erro": str(e)}), 500

@agendamentos_bp.route("/<int:id>", methods=["DELETE"])
def excluir_agendamento(id):
    try:
        agendamento = Agendamento.query.get(id)
        if agendamento is not None:
            db.session.delete(agendamento)
            db.session.commit()
            return jsonify({"Mensagem": f"Agendamento id {id} deletado com sucesso"}), 200
        else:
            return jsonify({"Erro": "Agendamento não encontrado"}), 404
    except Exception as e:
        return jsonify({"Erro": str(e)}), 500
