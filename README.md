# Eco-Stock API

## Description

**Eco-Stock** est une API REST développée avec **Django** et **Django REST Framework** pour la gestion de stocks alimentaires.

L'objectif principal de cette API est de permettre à une startup spécialisée dans la logistique du don alimentaire de gérer ses entrepôts, ses produits alimentaires ainsi que les transferts de produits entre entrepôts, tout en sécurisant l'accès aux données grâce à l'authentification JWT.

---

# Fonctionnalités

L'API permet de :

* Gérer les entrepôts (CRUD complet)
* Gérer les produits alimentaires (CRUD complet)
* Associer un produit à un entrepôt (relation 1-N)
* Transférer un produit vers un autre entrepôt
* Auditer un entrepôt (nombre total de produits)
* Authentifier les utilisateurs avec JWT
* Protéger les opérations de modification du stock

---

# Technologies utilisées

* Python 3
* Django
* Django REST Framework
* Simple JWT
* SQLite (par défaut)
* Git
* Postman ou Insomnia (pour les tests)

---

# Structure du projet

```text
Eco-Stock/
│
├── manage.py
├── requirements.txt
├── db.sqlite3
│
├── ecostock/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── stock/
    ├── admin.py
    ├── apps.py
    ├── migrations/
    ├── models.py
    ├── serializers.py
    ├── urls.py
    ├── views.py
    ├── tests.py
    └── __init__.py
```

---

# Installation

## 1. Cloner le projet

```bash
git clone https://github.com/votre-utilisateur/eco-stock.git
```

ou télécharger le projet puis se placer dans son dossier.

---

## 2. Créer un environnement virtuel

### Windows

```bash
python -m venv venv
```

### Linux / macOS

```bash
python3 -m venv venv
```

---

## 3. Activer l'environnement virtuel

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

# Configuration

## Appliquer les migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Créer un superutilisateur

```bash
python manage.py createsuperuser
```

Suivre ensuite les instructions affichées dans le terminal.

---

# Lancer le serveur

```bash
python manage.py runserver
```

L'API sera accessible à l'adresse :

```text
http://127.0.0.1:8000/
```

---

# Authentification JWT

## Obtenir un token

**POST**

```text
/api/token/
```

Exemple de corps JSON :

```json
{
    "username": "admin",
    "password": "mot_de_passe"
}
```

Réponse :

```json
{
    "refresh": "...",
    "access": "..."
}
```

---

## Rafraîchir un token

**POST**

```text
/api/token/refresh/
```

Corps :

```json
{
    "refresh": "..."
}
```

---

# Authentification des requêtes

Pour accéder aux routes protégées, ajouter l'en-tête HTTP suivant :

```text
Authorization: Bearer votre_access_token
```

---

# Endpoints de l'API

## Warehouses

 Méthode E       Endpoint                  Description           
 ------- ---------------------  ---------------------- 
 GET      /api/warehouses/       Liste des entrepôts    
 POST     /api/warehouses/       Créer un entrepôt      
 GET      /api/warehouses/{id}/  Détail d'un entrepôt   
 PUT      /api/warehouses/{id}/  Modifier un entrepôt   
 PATCH    /api/warehouses/{id}/  Modifier partiellement 
 DELETE   /api/warehouses/{id}/  Supprimer un entrepôt  

---

## Produits

 Méthode    Endpoint             Description            
-------  -------------------  ---------------------- 
 GET      /api/products/       Liste des produits     
 POST     /api/products/       Créer un produit       
 GET      /api/products/{id}/  Détail d'un produit    
 PUT      /api/products/{id}/  Modifier un produit    
 PATCH    /api/products/{id}/  Modifier partiellement
 DELETE   /api/products/{id}/  Supprimer un produit

---

## Actions métier

### Déplacer un produit

**POST**

```text
/api/products/{id}/move/
```

Exemple :

```json
{
    "warehouse": 2
}
```

Cette action transfère un produit vers un autre entrepôt si celui-ci n'est pas périmé.

---

### Audit d'un entrepôt

**GET**

```text
/api/warehouses/{id}/audit/
```

Réponse :

```json
{
    "warehouse": "Entrepôt Dakar",
    "total_products": 15
}
```

---

# Codes HTTP utilisés

 Code      Signification               
----  --------------------------- 
 200       Requête réussie             
 201       Ressource créée             
 204     Ressource supprimée         
 400   Requête invalide
 401   Utilisateur non authentifié 
 403   Accès interdit              
 404   Ressource introuvable

---

# Tests

Les tests de l'API peuvent être réalisés avec :

* Postman
* Insomnia

Tester notamment :

* le CRUD des entrepôts ;
* le CRUD des produits ;
* l'authentification JWT ;
* le transfert d'un produit ;
* l'audit d'un entrepôt.

---

# Bonnes pratiques

* Utiliser un environnement virtuel Python.
* Effectuer les migrations avant le premier lancement.
* Protéger les routes sensibles avec JWT.
* Versionner le projet avec Git.
* Documenter chaque évolution importante du projet.

---

# Auteur

Projet réalisé dans le cadre d'un exercice de développement d'une API REST avec **Django REST Framework**.

**Nom du projet :** Eco-Stock


