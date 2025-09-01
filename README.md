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

Cloner le dépôt et se positionner dans le dossier :

```sh
git clone https://github.com/Cedric-Royer/healthcare_data_migration.git
cd healthcare_data_migration
```

---

## Lancement du projet avec Docker Compose

1. Nettoyer les anciens conteneurs et volumes (optionnel)

```sh
docker-compose down -v
docker volume prune
```

2. Construire et lancer les conteneurs

```sh
docker-compose up --build
```

---

## Vérification

### Accéder au shell MongoDB dans le conteneur

```sh
docker exec -it mongodb mongosh
```

Exemples de commandes MongoDB dans `mongosh` :

```sh
show dbs
use data_solu_tech
show collections
db.healthcare_dataset.find().pretty()
```

## Utilisation local sans docker :

1. S’assurer que MongoDB tourne localement (`mongodb://localhost:27017/`).
2. Lancer le script d’import :

```sh
python import_to_mongodb.py
```

3. Vérifier les données importées dans MongoDB :

```sh
pytest -v test_data_validation.py
```

## Structure du dépôt

- `import_to_mongodb.py` : script Python de migration CSV → MongoDB
- `data/healthcare_dataset.csv` : fichier CSV source inclus
- `test_data_validation` : comparaison des données CSV / Mongo sans migration de données
- `requirements.txt` : dépendances Python à installer
- `docker-compose.yml` : définition des services Docker (MongoDB, migration)
- `Dockerfile` : instructions pour construire l’image Docker du service migration
