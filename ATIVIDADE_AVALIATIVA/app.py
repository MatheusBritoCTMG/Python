# Cenário: A - Locadora
import os

from flask import Flask

from controllers import dashboard_bp, locadora_bp
from models import ClienteLocadora, Locacao, Veiculo, db


def popular_dados(app):
    """Insere dados iniciais se o banco estiver vazio."""
    with app.app_context():
        if ClienteLocadora.query.count() > 0:
            return

        clientes = [
            ClienteLocadora(nome="Ana Silva", cpf="111.222.333-44", cnh="12345678900"),
            ClienteLocadora(nome="Bruno Costa", cpf="555.666.777-88", cnh="98765432100"),
        ]
        veiculos = [
            Veiculo(placa="ABC-1D23", modelo="Fiat Argo", diaria=120.0),
            Veiculo(placa="XYZ-9K87", modelo="Hyundai HB20", diaria=135.0),
        ]
        db.session.add_all(clientes + veiculos)
        db.session.commit()
        print("✅ Dados iniciais inseridos!")


def criar_app():
    app = Flask(
        __name__,
        template_folder="views/templates",
        static_folder="views/static",
    )

    pasta = os.path.abspath(os.path.dirname(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        pasta, "locadora.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

   
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(locadora_bp)   

    with app.app_context():
        db.create_all()

    return app


app = criar_app()
popular_dados(app)

if __name__ == "__main__":
    app.run(debug=True)
