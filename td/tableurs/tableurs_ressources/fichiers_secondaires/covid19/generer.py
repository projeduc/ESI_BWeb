#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import numpy
import pandas

covid19 = pandas.read_csv("COVID19_line_list_data.csv")

donnees = pandas.DataFrame()

etats_tab = numpy.array(["hospitalisé", "mort", "rétabli"])

donnees["date"] = covid19["reporting date"]
donnees["pays"] = covid19["country"]
donnees["sex"] = covid19["gender"]
donnees["age"] = covid19["age"]

covid19["death"] = (covid19["death"] != "0").astype(int)
covid19["recovered"] = (covid19["recovered"] != "0").astype(int)

etat = etats_tab[(covid19["death"] + covid19["recovered"] * 2).tolist()]
donnees["état"] = etat

donnees = donnees.loc[donnees["pays"].isin(["Singapore", "China", "South Korea"])]

donnees.to_excel("./covid19_analyse.xlsx", index=False)
