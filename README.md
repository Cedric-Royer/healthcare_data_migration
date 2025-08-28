# Migration CSV vers MongoDB

## Description

Ce projet contient un script Python `import_to_mongodb.py` permettant de migrer un fichier CSV vers une base de données MongoDB.

Le script :
- lit le CSV avec pandas,
- convertit les colonnes de dates au bon format,
- insère les données dans MongoDB,
- crée des index pertinents pour optimiser les requêtes.

## Prérequis

- MongoDB installé et démarré localement (par défaut sur `mongodb://localhost:27017/`)
- Python 3
- Modules Python (installés via `requirements.txt`)

## Installation

Cloner le dépôt :
```sh
git clone https://github.com/Cedric-Royer/healthcare_data_migration.git
cd healthcare_data_migration
```

## Structure du dépôt

- `import_to_mongodb.py` : script Python de migration CSV → MongoDB
- `data/healthcare_dataset.csv` : fichier CSV source inclus
- `test_data_validation` : comparaison des données CSV / Mongo sans migration de données
- `requirements.txt` : dépendances Python à installer


## Utilisation

1. S’assurer que MongoDB tourne localement (`mongodb://localhost:27017/`).
2. Lancer le script d’import :
```sh
python import_to_mongodb.py
```
3. Vérifier les données importées dans MongoDB :
```sh
pytest -v test_data_validation.py
```