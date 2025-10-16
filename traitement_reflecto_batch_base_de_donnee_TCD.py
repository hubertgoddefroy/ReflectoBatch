import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import subprocess
import os
import pandas as pd
import numpy as np
import itertools
import sys
import time
import threading

chemin_hasta_la_data = 'expo\\reconstruction_free_7_%_MOYPOND\\Synthese\\synthese_interferometric_data.csv'  # A modifier pour agglomérer d'autres fichiers


def selection_dossier_acquisitions():
    global chemin_dossier_acquisitions
    dossier_selectionne = filedialog.askdirectory()
    chemin_dossier_acquisitions = dossier_selectionne
    if chemin_dossier_acquisitions != '':
        bouton_dossier_lot['bg'] = 'green'


def selection_fichier_liste_plaques():
    global liste_plaques_csv
    fichier_selectionne = filedialog.askopenfilename(title="Liste des plaques", filetypes=[("Fichiers excel", "*.xlsx"),
                                                                                           ("Tous les fichiers",
                                                                                            "*.*")])
    liste_plaques_csv = fichier_selectionne
    if liste_plaques_csv != '':
        bouton_liste_plaques['bg'] = 'green'


def constitution_BDD():
    threading.Thread(target=creation_BDD(chemin_dossier_acquisitions, liste_plaques_csv, chemin_hasta_la_data,
                                         chemin_dossier_acquisitions)).start()


def creation_BDD(chemin_dossier_acquisitions, liste_plaques_csv, chemin_hasta_la_data, chemin_enregistrement):
    BDD = []
    liste_acquisitions = pd.read_excel(liste_plaques_csv)
    liste_acquisitions = np.array(liste_acquisitions)
    print(liste_acquisitions)
    for acquisition in range(len(liste_acquisitions)):
        position = liste_acquisitions[acquisition][0].find('SC')
        repeta = liste_acquisitions[acquisition][0][-2:]
        print('répéta = ', repeta)
        chemin_synthese_interf_data = chemin_dossier_acquisitions + '\\' + liste_acquisitions[acquisition][
            0] + '\\' + chemin_hasta_la_data
        print(chemin_synthese_interf_data)
        epaisseurs_acquisition = pd.read_csv(chemin_synthese_interf_data).to_numpy()
        arr_split = np.asarray([str(elem).split(";") for elem in epaisseurs_acquisition])
        for i in range(len(arr_split)):
            BDD.append([liste_acquisitions[acquisition][0][position:position + 19], repeta, arr_split[i, 0][2:],
                        float(arr_split[i, 4])])  # ajuster le +20 en +19 s'il s'agit de "Cas"
    BDD = np.asarray(BDD)
    df = pd.DataFrame(BDD)
    df.to_excel(chemin_dossier_acquisitions + '\\BDD.xlsx', index=False, header=False)


# fenêtre Tkinter
fenetre = tk.Tk()
fenetre.title("base de données")
fenetre.geometry("300x500")

# listes de tous les boutons
bouton_dossier_lot = tk.Button(fenetre, text="Dossier d'acquisition", command=selection_dossier_acquisitions)
bouton_dossier_lot.pack(pady=20)
bouton_liste_plaques = tk.Button(fenetre, text="liste des plaques", command=selection_fichier_liste_plaques)
bouton_liste_plaques.pack(pady=20)
bouton_constitution_BDD = tk.Button(fenetre, text="créer la BDD", bg="red", command=constitution_BDD)
bouton_constitution_BDD.pack(pady=20)

# Lancer la boucle principale Tkinter
fenetre.mainloop()