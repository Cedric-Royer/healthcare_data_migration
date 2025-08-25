import os
import pytest
import pandas as pd
from pymongo import MongoClient
from pathlib import Path


@pytest.fixture(scope="module")
def data_loaded():
    """
    Charge les données depuis un fichier CSV et une base de données MongoDB,
    puis renvoie les deux DataFrames pour comparaison.
    """
    base_path = Path(__file__).parent.resolve()
    csv_path = os.environ.get("CHEMIN_CSV", "data/healthcare_dataset.csv")
    abs_csv_path = (base_path / csv_path).resolve()
    df_before = pd.read_csv(abs_csv_path)

    mongodb_uri = os.environ.get("MONGODB_URI", "mongodb://localhost:27017/")
    db_name = os.environ.get("DB_NAME", "data_solu_tech")
    collection_name = os.environ.get("COLLECTION_NAME", "healthcare_dataset")

    client = MongoClient(mongodb_uri)
    db = client[db_name]
    collection = db[collection_name]
    cursor = collection.find()
    df_after = pd.DataFrame(list(cursor))
    client.close()

    return df_before, df_after


def test_row_count(data_loaded):
    df_before, df_after = data_loaded
    assert len(df_before) == len(df_after), f"Nombre de lignes doit être identique"


def test_column_names(data_loaded):
    df_before, df_after = data_loaded
    before_cols = set(df_before.columns)
    after_cols = set(df_after.columns) - {'_id'}
    assert before_cols == after_cols, "Colonnes du CSV et MongoDB doivent correspondre"


def test_no_duplicates(data_loaded):
    _, df_after = data_loaded
    duplicates = df_after.duplicated().sum()
    assert duplicates == 0, f"Pas de doublons attendus, mais trouvé : {duplicates}"


def test_no_missing_values(data_loaded):
    _, df_after = data_loaded
    missing_values_count = df_after.isnull().sum().sum()
    assert missing_values_count == 0, f"Aucune valeur manquante attendue, mais trouvé {missing_values_count}"