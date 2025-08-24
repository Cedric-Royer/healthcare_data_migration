# Migration CSV vers MongoDB

## Description

Ce projet contient un script Python `import_to_mongodb.py` permettant de migrer un fichier CSV local vers une base de données MongoDB locale.

Le script :
- lit le CSV avec pandas,
- nettoie les doublons,
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

## Utilisation

1. Modifier la variable `chemin_csv` dans le script Python pour pointer vers le fichier CSV local.  
2. S’assurer que MongoDB tourne localement (`mongodb://localhost:27017/`).  
3. Lancer le script pour importer les données :
```sh
python import_to_mongodb.py
```