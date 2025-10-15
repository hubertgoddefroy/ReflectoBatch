# ReflectoBatch
Lancer des reconstructions en boucle avec la possibilité de faire sur plusieurs acquisitions différentes et en faisant varier les paramètres Reflecto

Pour utiliser ReflectoBatch : 
1 - Lancer le programme
2 - une fenêtre s'ouvre :
3 - Cliquer sur "Dossier d'acquisition" : sélectionner le dossier contenant le dossier résultat de l'acquisition
4 - Cliquer sur "lise des plaques" : sélectionner un fichier excel qui contient sur la colonne "A" le nom exacte des sous-dossiers à prendre en compte comme étant des acquisitions à traiter, avec en en-tête "plaques"
5 - Cocher "POST" pour reconstruire les imageries POST, de même pour EXPO, on peut reconstruire POST et EXPO
6 - Cliquer sur "Reflecto" : sélectionner le fichier .txt contenant les paamètres réflecto pour lancer la reconstruction. Ces paramètres seront le point de départ des modification s'il y en a 
7 - Cliquer sur "Stat" : sélectionner le fichier Analysis.ini contenant les paramètres statistiques désirés. Dans ce fichier, seuls les paramètres statistiques sont lus
8 - Cliquer sur "Variation des paramètres" : sélectionner le fichier excel contenant les éventuelles valeurs des paramètres à tester. Attention, le fichier doit être au bon format !
9 - Case "colonne = plate-type ?" à cocher si on veut tester différentes conbinaisons bien définies de paramètres et pas toutes les combinaisons possibles par pérmutations
10 - Cliquer sur "Lancer les reconstructions" pour lancer Zyminterne, les reconstructions vont s'enchaîner
