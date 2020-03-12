#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Il faut télécharger ça pour générer la nouvelle liste
# https://github.com/othmanus/algeria-cities

import pandas

wilayas = pandas.read_csv("algeria-cities/csv/wilayas.csv")

communes = pandas.read_csv("algeria-cities/csv/communes.csv")

communes = pandas.merge(left=communes, right=wilayas,
                            how="left", left_on="wilaya_id", right_on="id")

communes["Adresse"] = communes["nom_x"] + ", " + communes["nom_y"]

communes = communes.filter(["Adresse", "code_postal"])

communes.rename(columns={"code_postal": "CodePostal"}, inplace=True)

communes.to_csv("./adresses.csv", index=False)

print(communes)
