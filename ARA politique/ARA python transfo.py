#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 13:53:03 2021

@author: noe
"""
import pandas as pd
pd.set_option('display.max_columns', None)
data = pd.read_csv("/Users/noe/Desktop/CNAM/Carto/Projet géo/ARA connexion.csv", sep = ";")
print(data.head())

newData = pd.DataFrame(columns = ["dpt", "techno_maj", "débit_maj", "pourcentage_bas_debit"])

for i in data["CODE_DEP"].unique() :
    
    currentVille = data[data["CODE_DEP"] == i]
    currentTech  = currentVille['code_techno'].value_counts().idxmax()
    currentDeb   = currentVille['classe_debit_descendant'].value_counts().idxmax()
    debits       = currentVille['classe_debit_descendant'].value_counts()
    nb_bas_debit = 0
    
    if "INEL" in debits.index :
        nb_bas_debit += debits["INEL"]
    
    if "HD05" in debits.index :
        nb_bas_debit += debits["HD05"]
    
    nb_lignes = currentVille.shape[0]
    
    pourcentage = nb_bas_debit/nb_lignes*100
    
    newRow = {"dpt" : int(i), "techno_maj" : currentTech, "débit_maj" : currentDeb, "pourcentage_bas_debit" : int(round(pourcentage))}
    
    newData = newData.append(newRow, ignore_index=True)
    
#print(data['code_techno'].value_counts().idxmax())
print(newData.head())

newData.to_csv("/Users/noe/Desktop/CNAM/Carto/Projet géo/ARA Connexion par dept.csv", sep = ";")
