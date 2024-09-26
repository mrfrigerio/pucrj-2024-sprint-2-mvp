from flask import request, jsonify
from flask_openapi3 import OpenAPI, Info, Tag
from pydantic import ValidationError
from urllib.parse import unquote
from models import db, Parameter
from schemas import AddParameterSchema, DeleteParameterSchema
from flask_cors import CORS
import pickle

info = Info(title="Heart Disease API", version="1.0.0")
app = OpenAPI(__name__, info=info)

parameters_tag = Tag(
    name="Parâmetros Clínicos",
    description="Cadastro de Parâmetros Clínicos de Pacientes para Inferência de Possibilidade de Doença Cardíaca",
)

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:////{app.root_path}/database/heart.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
CORS(app)

db.init_app(app)

with app.app_context():
    db.create_all()


@app.get("/api/parameter", tags=[parameters_tag])
def get_parameters():
    """Get all parameters"""
    parameters = Parameter.query.all()
    parameters_list = [
        {
            "id": p.id,
            "name": p.name,  # Nome do paciente
            "age": p.age,  # Idade
            "sex": p.sex,  # Sexo: 1 para masculino, 0 para feminino
            "cp": p.cp,  # tipo de dor torácica Valor 0: angina típica Valor 1: angina atípica Valor 2: dor não anginosa Valor 3: assintomática
            "trestbps": p.trestbps,  # Pressão arterial em repouso
            "chol": p.chol,  # Colesterol sérico
            "fbs": p.fbs,  # Glicemia de jejum
            "restecg": p.restecg,  # Resultados do eletrocardiograma em repouso
            "thalach": p.thalach,  # Frequência cardíaca máxima
            "exang": p.exang,  # Angina induzida por exercício
            "oldpeak": p.oldpeak,  # Depressão do ST induzida por exercício
            "slope": p.slope,  # Inclinação do segmento ST
            "ca": p.ca,  # Número de vasos principais coloridos por fluoroscopia
            "thal": p.thal,  # Tipo de talassemia
            "target": p.target,  # Presença de doença cardíaca
        }
        for p in parameters
    ]

    return jsonify(parameters_list)


@app.post("/api/parameter", tags=[parameters_tag])
def add_parameters(body: AddParameterSchema):
    """Add a new parameter"""
    with open("cart_classifier.pkl", "rb") as pickle_in:
        classifier = pickle.load(pickle_in)
        try:

            data = Parameter(**request.json)
        except ValidationError as e:
            return jsonify(e.errors()), 400

        new_parameter = Parameter(
            age=data.age,
            name=data.name,
            sex=data.sex,
            cp=data.cp,
            trestbps=data.trestbps,
            chol=data.chol,
            fbs=data.fbs,
            restecg=data.restecg,
            thalach=data.thalach,
            exang=data.exang,
            oldpeak=data.oldpeak,
            slope=data.slope,
            ca=data.ca,
            thal=data.thal,
            target=classifier.predict(  # Resultado previsto pelo classificador
                [
                    [
                        data.age,
                        data.sex,
                        data.cp,
                        data.trestbps,
                        data.chol,
                        data.fbs,
                        data.restecg,
                        data.thalach,
                        data.exang,
                        data.oldpeak,
                        data.slope,
                        data.ca,
                        data.thal,
                    ]
                ]
            )[0],
        )

        db.session.add(new_parameter)
        db.session.commit()
        return jsonify({"message": "Patient added successfully"}), 201


@app.delete("/api/parameter/<int:parameter_id>", tags=[parameters_tag])
def delete_capture(path: DeleteParameterSchema):
    """Delete a Patient parameters by ID"""
    print(path.parameter_id)
    capture = Parameter.query.get(path.parameter_id)
    if capture:
        db.session.delete(capture)
        db.session.commit()
        return jsonify({"message": "Patient parameters deleted successfully"}), 200
    else:
        return jsonify({"message": "Patient not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
