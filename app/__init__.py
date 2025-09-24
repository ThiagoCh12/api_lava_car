from flask import Flask
from .extensions import db
from .models import Cliente, Carro, Agendamento
from .routes.clientes import clientes_bp
from .routes.carros import carros_bp
from .routes.agendamentos import agendamentos_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.DevConfig")

    db.init_app(app)

    app.register_blueprint(clientes_bp, url_prefix="/clientes")
    app.register_blueprint(carros_bp, url_prefix="/carros")
    app.register_blueprint(agendamentos_bp, url_prefix="/agendamentos")

    @app.route("/")
    def home():
        return "API DO LAVA JATO RODANDO!"
    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)

