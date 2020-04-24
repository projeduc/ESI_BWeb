#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import random
import numpy
import pandas

FEMELLE_NBR = 100 # Nombre des filles
MALE_NBR = 100 # nombre des garçons
ESI_NBR = 150 #Nombre des étudiants de l'ESI
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

# Concaténer les deux listes en une matrice de pandas
maleListe = pandas.DataFrame({"Prenom": maleListe})
#print(maleListe)

# Liste aléatoire des filles
femelleListe = selectionner_aleatoirement("femelle.csv", FEMELLE_NBR)
femelleListe = pandas.DataFrame({"Prenom": femelleListe})
#print(femelleListe)

#concaténer les listes des garçons et des filles
etudiants = pandas.concat([maleListe, femelleListe])
#print(etudiants)

noms_liste = selectionner_aleatoirement("noms.csv", ALL_NBR)
etudiants["Nom"] = pandas.Series(noms_liste).values

liste_univ = selectionner_aleatoirement("nomUniv.csv", NONESI_NBR) + ["École nationale supérieure d'informatique d'Alger"] * ESI_NBR
liste_niveaux = [""] * NONESI_NBR + random.choices(NIVEAU, k=ESI_NBR)

msk = numpy.random.permutation(len(etudiants))
liste_univ = numpy.array(liste_univ)[msk]
liste_niveaux = numpy.array(liste_niveaux)[msk]

etudiants["Univ"] = pandas.Series(liste_univ).values
etudiants["Niveaux"] = pandas.Series(liste_niveaux).values
#print(etudiants)

etudiants = etudiants.iloc[numpy.random.permutation(len(etudiants))]

liste_exper = random.choices(EXPER, k=ALL_NBR)
etudiants["Experience"] = pandas.Series(liste_exper).values

liste_type = random.choices(TYPE, k=ALL_NBR)
etudiants["Type"] = pandas.Series(liste_type).values

adresses = pandas.read_csv("wilaya.csv")

etudiants["Wilaya"] = random.choices(adresses["nom"].values, k=ALL_NBR)

etudiants["Note"] = (numpy.array(random.choices(range(500, 2001, 25), k=ALL_NBR))/100.).tolist()

ordre = ["Nom", "Prenom", "Wilaya", "Univ", "Niveaux", "Type", "Experience", "Note"]
etudiants = etudiants.reindex(ordre, axis=1)

etudiants.to_excel("./participants_analyse.xlsx", index=False)
print(etudiants)
