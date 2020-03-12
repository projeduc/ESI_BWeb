#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import random
import numpy
import pandas

FEMELLE_NBR = 10 # Nombre des filles
MALE_NBR = 10 # nombre des garçons
ESI_NBR = 12 #Nombre des étudiants de l'ESI
ALL_NBR = FEMELLE_NBR + MALE_NBR # nombre total des étudiants
NONESI_NBR = ALL_NBR - ESI_NBR # nombre des étudiants hors ESI

NIVEAU = ["1CP", "2CP", "1CS", "2CS", "3CS"]

EXPER = ["Débutant", "Intermédiaire", "Avancé"]

TYPE = ["Introduction à la programmation", "C", "C#", "Java", "Javascript", "Python"]

# Une fonction qui lit une liste en utilisant le chemin (chaine de caractères)
# Elle retourne un nombre aléatoire des éléments de cette liste
def selectionner_aleatoirement(chemin_liste, nombre):
    # Lire la liste des prénoms des garçons
    with open(chemin_liste) as f:
        liste = f.read().splitlines()
    return random.choices(liste, k=nombre)

# Liste aléatoire des garçons
maleListe = selectionner_aleatoirement("male.csv", MALE_NBR)
# Créer une liste de "M." avec une taille de MALE_NBR
maleTitre = ["M."] * MALE_NBR
# Concaténer les deux listes en une matrice de pandas
maleListe = pandas.DataFrame({"Titre": maleTitre,
                                "Prenom": maleListe})
#print(maleListe)

# Liste aléatoire des filles
femelleListe = selectionner_aleatoirement("femelle.csv", MALE_NBR)
# Créer une liste de "Mme" "Mlle" aléatoirement avec une taille de FEMELLE_NBR
femelleTitre = random.choices(["Mme", "Mlle"], k=FEMELLE_NBR)
femelleListe = pandas.DataFrame({"Titre": femelleTitre,
                                "Prenom": femelleListe})
#print(femelleListe)

#concaténer les listes des garçons et des filles
etudiants = pandas.concat([maleListe, femelleListe])
#print(etudiants)

noms_liste = selectionner_aleatoirement("noms.csv", ALL_NBR)
etudiants["Nom"] = pandas.Series(noms_liste).values

liste_univ = selectionner_aleatoirement("nomUniv.csv", NONESI_NBR)
liste_niveaux = random.choices(NIVEAU, k=ESI_NBR)
liste_niveaux = liste_niveaux + liste_univ
#print(liste_niveaux)
random.shuffle(liste_niveaux)
#print(len(liste_niveaux))
#print(liste_univ)
etudiants["NiveauUniv"] = pandas.Series(liste_niveaux).values
#print(etudiants)

etudiants = etudiants.iloc[numpy.random.permutation(len(etudiants))]

liste_exper = random.choices(EXPER, k=ALL_NBR)
etudiants["Experience"] = pandas.Series(liste_exper).values

liste_type = random.choices(TYPE, k=ALL_NBR)
etudiants["Type"] = pandas.Series(liste_type).values

adresses = pandas.read_csv("adresses.csv")

# mélanger les adresses
adresses = adresses.iloc[numpy.random.permutation(len(adresses))]
# choisir les premiers
adresses = adresses.head(ALL_NBR)

etudiants["Adresse"] = adresses["Adresse"].values
etudiants["CodePostal"] = adresses["CodePostal"].values

ordre = ["Titre", "Nom", "Prenom", "Adresse", "CodePostal", "NiveauUniv", "Type", "Experience"]
etudiants = etudiants.reindex(ordre, axis=1)

etudiants.to_excel("./formtion.xlsx", index=False)
print(etudiants)
