import pickle
import pandas as pd
from sklearn.metrics import accuracy_score


def test_cart_model():
    # Carregando o dataset
    dataset = pd.read_csv("heart_dataset_test.csv", delimiter=",")
    array = dataset.values
    X_test = array[:, 0:13]
    y_test = array[:, 13]
    # Carregando o modelo CART
    with open("cart_classifier.pkl", "rb") as pickle_in:
        classifier = pickle.load(pickle_in)
        # Obtendo as métricas de acurácia do model
        # # Estimativa da acurácia no conjunto de teste
        predictions = classifier.predict(X_test)
        cart_accuracy = accuracy_score(y_test, predictions)
        print(
            f"Acurácia do modelo CART: {cart_accuracy}"
        )  # Imprime apenas em caso de falha no teste
        assert cart_accuracy >= 0.78
