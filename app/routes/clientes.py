from flask import Blueprint, jsonify, request
from ..extensions import db
from ..models import Cliente

clientes_bp =  Blueprint("clientes", __name__, url_prefix="/clientes")

@clientes_bp.route("/", methods=["POST"])
def criar_cliente():
    data = request.get_json()
    cliente = Cliente(nome=data["nome"], telefone=data["telefone"])
    db.session.add(cliente)
    db.session.commit()
    return jsonify({"id":cliente.id, 
                    "nome":cliente.nome, 
                    "telefone":cliente.telefone}), 201

@clientes_bp.route("/", methods=["GET"])
def listar_clientes():
    clientes = Cliente.query.all()
    return jsonify([{"id":c.id, 
                     "nome":c.nome, 
                     "telefone":c.telefone} for c in clientes])

@clientes_bp.route("/<int:id>", methods=["GET"])
def buscar_cliente(id):
    try:
        cliente = Cliente.query.get(id)
        if cliente is not None:
            return jsonify({"id":cliente.id,
                            "nome":cliente.nome,
                            "telefone":cliente.telefone,
                            "carros":[{"id": c.id, "modelo": c.modelo, "placa": c.placa} for c in cliente.carros],
                            "agendamentos":[{"id": a.id, "data": a.data.isoformat()} for a in cliente.agendamentos]}),200
        else:
            return jsonify({"Erro":"Cliente não encontrado."}), 404
    except Exception as e:
        return jsonify({"Erro":str(e)}),500

@clientes_bp.route("/<int:id>", methods=["PUT"])
def editar_cliente(id):
    try:
        cliente = Cliente.query.get(id)
        if cliente is not None:
            rq = request.get_json()
            if "nome" in rq:
                cliente.nome = rq["nome"]
            if "telefone" in rq:
                cliente.telefone = rq["telefone"]
            db.session.commit()
            return jsonify({"id": cliente.id,
                            "nome":cliente.nome,
                            "telefone":cliente.telefone,
                            "carros":[{"id": c.id, "modelo": c.modelo, "placa": c.placa} for c in cliente.carros],
                            "agendamentos":[{"id": a.id, "data": a.data.isoformat()} for a in cliente.agendamentos]}),200
        else:
            return jsonify({"Erro":"Cliente não encontrado!"}),404
    except Exception as e:
        return jsonify({"Erro": str(e)}),500
    
@clientes_bp.route("/<int:id>", methods=["DELETE"])
def excluir_cliente(id):
    try:
        cliente = Cliente.query.get(id)
        if cliente is not None:
            db.session.delete(cliente)
            db.session.commit()
            return jsonify({"Mensagem":f"Cliente id {id} excluído com sucesso"}), 200
        else:
            return jsonify({"Erro":"Cliente não encontrado"}), 404
    except Exception as e:
        return jsonify({"Erro": str(e)}),500