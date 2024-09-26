from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Parameter(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Identificador
    name = db.Column(db.String(300), nullable=False)  # Nome do paciente
    age = db.Column(db.Float, nullable=False)  # Idade
    sex = db.Column(db.Float, nullable=False)  # Sexo (1 = masculino; 0 = feminino)
    cp = db.Column(
        db.Float, nullable=False
    )  # tipo de dor torácica Valor 0: angina típica Valor 1: angina atípica Valor 2: dor não anginosa Valor 3: assintomática
    trestbps = db.Column(db.Float, nullable=False)  # Pressão arterial em repouso
    chol = db.Column(db.Float, nullable=False)  # Colesterol
    fbs = db.Column(db.Float, nullable=False)  # Glicemia de jejum
    restecg = db.Column(
        db.Float, nullable=False
    )  # Resultados do eletrocardiograma em repouso
    thalach = db.Column(
        db.Float, nullable=False
    )  # Frequência cardíaca máxima alcançada
    exang = db.Column(
        db.Float, nullable=False
    )  # Angina induzida por exercício (1 = sim; 0 = não)
    oldpeak = db.Column(
        db.Float, nullable=False
    )  # Depressão do ST induzida por exercício em relação ao repouso
    slope = db.Column(
        db.Float, nullable=False
    )  # Inclinação do segmento ST no pico do exercício
    ca = db.Column(
        db.Float, nullable=False
    )  # Número de vasos principais (0-3) coloridos por fluoroscopia
    thal = db.Column(db.Float, nullable=False)  # Tipo de talassemia
    target = db.Column(
        db.Integer, nullable=False
    )  # Presença de doença cardíaca (1 = sim; 0 = não)
