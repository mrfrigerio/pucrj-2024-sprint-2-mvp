from flask import request, jsonify
from flask_openapi3 import OpenAPI, Info, Tag
from pydantic import ValidationError
from urllib.parse import unquote
from models import db, Capture
from schemas import CaptureSchema, DeleteCaptureSchema
import requests
from flask_cors import CORS

info = Info(title="Pokedex API", version="1.0.0")
app = OpenAPI(__name__, info=info)

capture_tag = Tag(name="Capturas", description="Cadastro de Pokemons Capturados")
pokeapi_tag = Tag(name="PokeAPI", description="Busca a lista de Pokemons da PokeAPI")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"sqlite:////{app.root_path}/database/pokedex.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
CORS(app)

db.init_app(app)

with app.app_context():
    db.create_all()


@app.get("/api/pokemons", tags=[pokeapi_tag])
def get_pokemons():
    response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
    return jsonify(response.json()["results"])


@app.post("/api/captures", tags=[capture_tag])
def add_capture(body: CaptureSchema):
    """Add a new capture"""
    try:
        data = Capture(**request.json)
    except ValidationError as e:
        return jsonify(e.errors()), 400

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{data.pokemon_name}")
    if response.status_code != 200:
        return jsonify({"error": "Pokemon not found"}), 404

    pokemon_data = response.json()
    new_capture = Capture(
        trainer_name=data.trainer_name,
        capture_date=data.capture_date,
        pokemon_name=data.pokemon_name,
        pokemon_image=pokemon_data["sprites"]["front_default"],
    )
    db.session.add(new_capture)
    db.session.commit()
    return jsonify({"message": "Capture added successfully"}), 201


@app.get("/api/captures", tags=[capture_tag])
def get_captures():
    """Get all captures"""
    captures = Capture.query.all()
    captures_list = [
        {
            "id": c.id,
            "trainer_name": c.trainer_name,
            "capture_date": c.capture_date,
            "pokemon_name": c.pokemon_name,
            "pokemon_image": c.pokemon_image,
        }
        for c in captures
    ]
    return jsonify(captures_list)


@app.delete("/api/captures/<int:capture_id>", tags=[capture_tag])
def delete_capture(path: DeleteCaptureSchema):
    """Delete a capture by ID"""
    print(path.capture_id)
    capture = Capture.query.get(path.capture_id)
    if capture:
        db.session.delete(capture)
        db.session.commit()
        return jsonify({"message": "Capture deleted successfully"}), 200
    else:
        return jsonify({"message": "Capture not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
