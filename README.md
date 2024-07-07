# association-danse


# Gestion de l'Association Sportive - POC

## Description
Ce Proof of Concept (POC) a été développé pour démontrer les fonctionnalités de base d'un système de gestion pour une association sportive. Le système permet la gestion des adhérents, des événements, ainsi que le suivi de la présence à ces événements.

## Fonctionnalités
- **Inscription et gestion des adhérents** : Permet aux adhérents de s'inscrire et de mettre à jour leurs informations personnelles.
- **Gestion des événements** : Création et gestion des événements, incluant les inscriptions et la gestion des places.
- **Suivi de la présence** : Enregistrement de la présence des adhérents aux différents événements.
- **Dashboard** : Un tableau de bord pour visualiser les statistiques clés concernant les adhérents et les événements.

## Technologies Utilisées
- **Backend** : Python avec le framework Flask
- **Frontend** : HTML, CSS, JavaScript
- **Base de données** : SQLite (fichier Json pour le POC)

## Installation
Pour installer et exécuter ce POC, suivez les étapes suivantes :

1. **Cloner le dépôt Git** :
   ```bash
   git clone git@github.com:loanieurt/association-danse.git
   ```
2. **Installer les dépendances** :
   Assurez-vous d'avoir Python3 installé, puis exécutez :
   ```bash
   pip install Flask
   ```
3. **Démarrer le serveur** :
   ```bash
   python3 app.py
   ```
   Le serveur démarrera et sera accessible à l'adresse `http://localhost:5000/`.

## Utilisation
Après avoir démarré le serveur, ouvrez votre navigateur à l'adresse indiquée pour commencer à utiliser l'application. Vous pouvez naviguer à travers les différentes sections via la barre de navigation pour accéder aux fonctionnalités offertes.
