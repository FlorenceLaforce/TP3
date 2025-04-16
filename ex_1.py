import os
import json
import csv
import xml.etree.ElementTree as ET


class AgregateurDonnees:
    def __init__(self):
        self.donnees = []

    def lire_json(self):
        data = {"nom": "Gracia Sophie", "age": 20, "notes": [12, 18, 13],
                }
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
        with open(f"data.json", "r") as f:
            data_lue = json.load(f)
            print(data_lue["nom"])

    def lire_csv(self):
        with open('etudiants.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['nom', 'prenom', 'age', 'mathematiques', 'pysique', 'Informatique'])
            writer.writerow(['Dupont', 'Marie', '19', '16.5', '14.75', '18'])
            writer.writerow(['Martin', 'Thomas', '20', '12', '13.5', '15.25'])
            writer.writerow(['Leroy', 'Emma', '18', '17.5', '16', '14'])
            writer.writerow(['Petit', 'Lucas', '19', '9', '11', '13.75'])

        with open('etudiants.csv', 'r') as f:
            reader = csv.reader(f)
            for ligne in reader:
                print(ligne)

    def lire_xml(self):
        pass

    def calculer_statistiques(self):
        pass

    def sauvergarder_resultats(self):
        pass

def main():
    choix = input('Quel type de fichier voulez-vous lire ?'
                  '1: .json'
                  '2: .csv'
                  '3: .xml')



if __name__ == '__main__':
    main()