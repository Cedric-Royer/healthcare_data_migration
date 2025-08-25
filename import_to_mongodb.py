import os
from pathlib import Path
import pandas as pd
from pymongo import MongoClient


def import_csv_to_mongodb(csv_path, mongodb_uri, db_name, collection_name):
    base_path = Path(__file__).parent.resolve()
    abs_csv_path = (base_path / csv_path).resolve()

    print(f"Lecture du fichier CSV: {abs_csv_path}")
    df = pd.read_csv(abs_csv_path)

    df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
    df['Discharge Date'] = pd.to_datetime(df['Discharge Date'])

    records = df.to_dict(orient='records')

    client = MongoClient(mongodb_uri)
    try:
        db = client[db_name]
        collection = db[collection_name]
        collection.drop()
        print(f"Insertion des {len(records)} documents...")
        result = collection.insert_many(records)
        print(f"{len(result.inserted_ids)} documents insérés avec succès.")

        collection.create_index('Age')
        collection.create_index('Medical Condition')
        collection.create_index('Date of Admission')
        collection.create_index('Discharge Date')

        print("Migration terminée.")
    finally:
        client.close()


if __name__ == "__main__":
    chemin_csv = os.environ.get("CHEMIN_CSV", "data/healthcare_dataset.csv")
    uri_mongodb = os.environ.get("MONGODB_URI", "mongodb://localhost:27017/")
    nom_db = os.environ.get("DB_NAME", "data_solu_tech")
    nom_collection = os.environ.get("COLLECTION_NAME", "healthcare_dataset")

    import_csv_to_mongodb(chemin_csv, uri_mongodb, nom_db, nom_collection)
