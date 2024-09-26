from flask import request, jsonify
from flask_openapi3 import OpenAPI, Info, Tag
from pydantic import ValidationError
from urllib.parse import unquote
from models import db, Parameter
from schemas import AddParameterSchema, DeleteParameterSchema
from flask_cors import CORS

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
            "patient_name": p.patient_name,
            "pregnancies": p.pregnancies,
            "glucose": p.glucose,
            "blood_pressure": p.blood_pressure,
            "skin_thickness": p.skin_thickness,
            "insulin": p.insulin,
            "bmi": p.bmi,
            "diabetes_pedigree_function": p.diabetes_pedigree_function,
            "age": p.age,
        }
        for p in parameters
    ]
    return jsonify(parameters_list)


@app.post("/api/parameter", tags=[parameters_tag])
def add_capture(body: AddParameterSchema):
    """Add a new parameter"""
    try:
        data = Parameter(**request.json)
    except ValidationError as e:
        return jsonify(e.errors()), 400

    new_parameter = Parameter(
        patient_name=data.patient_name,
        pregnancies=data.pregnancies,
        glucose=data.glucose,
        blood_pressure=data.blood_pressure,
        skin_thickness=data.skin_thickness,
        insulin=data.insulin,
        bmi=data.bmi,
        diabetes_pedigree_function=data.diabetes_pedigree_function,
        age=data.age,
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
