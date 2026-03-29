#  :rocket: VLSM Calculator & Visualizer

⸻

##  :pushpin: Description

Ce projet est une application interactive développée en Python avec Streamlit permettant de calculer automatiquement un plan d’adressage IPv4 en utilisant la méthode VLSM (Variable Length Subnet Mask).

L’utilisateur entre un réseau de base ainsi que les besoins en hôtes, et l’application génère automatiquement :
    •    les sous-réseaux optimisés
    •    les plages d’adresses IP
    •    les masques associés
    •    les adresses de broadcast

Une visualisation claire du découpage réseau est également proposée.

⸻

##  :dart: Objectifs
    •    Comprendre et appliquer le VLSM
    •    Automatiser un calcul souvent fait à la main en TD
    •    Visualiser concrètement le découpage d’un réseau
    •    Transformer un concept théorique en application interactive

⸻

## :gear: Fonctionnalités

:white_check_mark: Entrée d’un réseau de base (ex: 192.168.1.0/24)
:white_check_mark: Ajout dynamique de sous-réseaux
:white_check_mark: Calcul automatique VLSM
:white_check_mark: Génération d’un tableau complet :
    •    CIDR
    •    Masque
    •    Adresse réseau
    •    Première / dernière IP
    •    Broadcast

##  :white_check_mark: Visualisation graphique du découpage réseau

⸻

##  :desktop: Aperçu

Exemple :

Réseau de base : 172.16.100.0/24

Sous-réseaux :
- 50 hôtes
- 20 hôtes
- 10 hôtes
- 2 hôtes

Résultat :
    •    /26 → 172.16.100.0
    •    /27 → 172.16.100.64
    •    /28 → 172.16.100.96
    •    /30 → 172.16.100.112

⸻

##  :tools: Technologies utilisées
    •    Python :snake:
    •    Streamlit :art:
    •    Pandas :bar_chart:
    •    ipaddress (librairie standard)

⸻

##  :rocket: Installation
    1.    Cloner le projet :

git clone https://github.com/AmZzPYJS/vlsm-calculator.git
cd vlsm-calculator

    2.    Installer les dépendances :

pip install streamlit pandas

    3.    Lancer l’application :

streamlit run app.py


⸻

##  :books: Concepts utilisés
    •    Subnetting IPv4
    •    VLSM (Variable Length Subnet Mask)
    •    CIDR
    •    Calcul des plages IP
    •    Broadcast / Network Address
