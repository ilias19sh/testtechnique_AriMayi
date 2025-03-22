# Application de Recrutement - Django REST API

## Description

Cette application permet la gestion des recrutements en mettant en relation des recruteurs et des candidats à travers des offres d'emploi. L'API est développée en Django avec Django REST Framework.

## Fonctionnalités

- **Gestion des candidats** : Ajouter, modifier, supprimer et consulter les candidats.
- **Gestion des recruteurs** : Ajouter, modifier, supprimer et consulter les recruteurs.
- **Gestion des offres d'emploi** : Création et gestion des offres d'emploi associées à un recruteur.
- **Association candidat/offre** : Les candidats peuvent postuler à plusieurs offres.

## Installation

1. Cloner le projet :

   ```sh
   git clone https://github.com/ilias19sh/testtechnique_AriMayi.git
   cd repository
   ```

2. Créer un environnement virtuel et l'activer :

   ```sh
   python -m venv venv
   source venv/bin/activate  # Sur Mac/Linux
   venv\Scripts\activate  # Sur Windows
   ```

3. Installer les dépendances :

   ```sh
   pip install -r requirements.txt
   ```

4. Appliquer les migrations :

   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Lancer le serveur :

   ```sh
   python manage.py runserver
   ```

## Utilisation de l'API

- **Endpoint principal** : `http://127.0.0.1:8000/api/`
- **Candidats** : `http://127.0.0.1:8000/api/candidates/`
- **Recruteurs** : `http://127.0.0.1:8000/api/recruiter/`
- **Offres d'emploi** : `http://127.0.0.1:8000/api/offer/`

### Exemple de requête POST pour ajouter un candidat

```json
{
    "first_name": "Ilias",
    "last_name": "Hanfaoui",
    "email": "ilias.hanfaoui3@gmail.com",
    "experience": "4 mois en développement informatique"
}
```

## Diagrammes

### Diagramme des classes et des cas d'utilisation

[https://drive.google.com/file/d/102C9B0N4ow5UTqW7x\_zNZrnBB87I5AVa/view?usp=sharing](https://drive.google.com/file/d/102C9B0N4ow5UTqW7x_zNZrnBB87I5AVa/view?usp=sharing)

## Auteur

- Nom : Ilias Hanfaoui
- Email : [ilias.hanfaoui3@gmail.com](mailto\:ilias.hanfaoui3@gmail.com)
