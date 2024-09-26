from pydantic import BaseModel


# Schema de exemplo
class AddParameterSchema(BaseModel):
    name: str = "Maria da Silva"  # Nome do paciente
    age: float = 50  # Idade
    sex: float = 0  # Sexo: 1 para masculino, 0 para feminino
    cp: float = (
        0  # tipo de dor torácica Valor 0: angina típica Valor 1: angina atípica Valor 2: dor não anginosa Valor 3: assintomática
    )
    trestbps: float = 110  # Pressão arterial em repouso
    chol: float = 254  # Colesterol sérico em mg/dl
    fbs: float = 0  # Glicemia de jejum > 120 mg/dl (1 = verdadeiro; 0 = falso)
    restecg: float = 0  # Resultados do eletrocardiograma em repouso (0-2)
    thalach: float = 159  # Frequência cardíaca máxima alcançada
    exang: float = 0  # Angina induzida por exercício (1 = sim; 0 = não)
    oldpeak: float = 0.0  # Depressão do ST induzida por exercício em relação ao repouso
    slope: float = 2  # Inclinação do segmento ST no pico do exercício (0-2)
    ca: float = 0  # Número de vasos principais (0-3) coloridos por fluoroscopia
    thal: float = (
        2  # Tipo de talassemia (1 = normal; 2 = defeito fixo; 3 = defeito reversível)
    )


class DeleteParameterSchema(BaseModel):
    parameter_id: int = 1
