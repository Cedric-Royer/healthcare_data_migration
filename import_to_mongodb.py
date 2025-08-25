import os
import pandas as pd
from pymongo import MongoClient

def import_csv_to_mongodb(csv_path, mongodb_uri, db_name, collection_name):
    """
    Importer les données d'un fichier CSV vers une base MongoDB.

    Paramètres :
        csv_path (str) : chemin local du fichier CSV
        mongodb_uri (str) : URI de connexion MongoDB (ex: "mongodb://localhost:27017/")
        db_name (str) : nom de la base MongoDB
        collection_name (str) : nom de la collection MongoDB où insérer les données

    Fonctionnement :
        - Lecture du CSV avec pandas
        - Nettoyage doublons
        - Conversion des colonnes date en datetime
        - Conversion en dictionnaire JSON
        - Connexion à MongoDB
        - Suppression de la collection existante
        - Insertion des documents
        - Création d’index sur champs utiles
    """
    print("Lecture du fichier CSV...")
    df = pd.read_csv(csv_path)

    print("Nettoyage des doublons...")
    df = df.drop_duplicates()

    # Convertir les dates en datetime
    df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
    df['Discharge Date'] = pd.to_datetime(df['Discharge Date'])

    # Convertir en dict JSON compatible MongoDB
    records = df.to_dict(orient='records')

    print("Connexion à MongoDB...")
    client = MongoClient(mongodb_uri)
    db = client[db_name]
    collection = db[collection_name]

    print("Suppression de la collection (si existante)...")
    collection.drop()

    print(f"Insertion des {len(records)} documents...")
    result = collection.insert_many(records)

    print(f"{len(result.inserted_ids)} documents insérés avec succès.")

    # Création des index
    print("Création des index...")
    collection.create_index('Age')
    collection.create_index('Medical Condition')
    collection.create_index('Date of Admission')
    collection.create_index('Discharge Date')

    print("Migration terminée.")

if __name__ == "__main__":
    # Paramètres lus dans l'environnement, avec valeurs par défaut adaptées à Docker
    chemin_csv = os.environ.get("CHEMIN_CSV", "data/healthcare_dataset.csv")
    uri_mongodb = os.environ.get("MONGODB_URI", "mongodb://localhost:27017/")
    nom_db = os.environ.get("DB_NAME", "data_solu_tech")
    nom_collection = os.environ.get("COLLECTION_NAME", "healthcare_dataset")

    import_csv_to_mongodb(chemin_csv, uri_mongodb, nom_db, nom_collection)
