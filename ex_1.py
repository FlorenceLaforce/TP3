import os
import json
import csv
import xml.etree.ElementTree as ET


class AgregateurDonnees:
    def __init__(self):
        self.donnees = []

    def lire_json(self):
        data = [{"nom": "Gracia Sophie", "age": 20, "notes": {"maths": 15,"physique": 12.5, "info": 16.25}},
                {"nom": "Bernard Antoine", "age": 19, "notes": {"maths": 13.5,"physique": 14, "info": 12}},
                {"nom": "Moreau Julie", "age": 21, "notes": {"maths": 18,"physique": 17.5, "info": 19}}
                ]
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
            with open(f"data.json", "r") as f:
                data_lue = json.load(f)
                for personne in data_lue:
                    print(f"Nom : {personne['nom']}")
                    print(f"Âge : {personne['age']}")
                    print("Notes :")
                    for matiere, note in personne['notes'].items():
                        print(f"\t{matiere.capitalize()} : {note}")

    def lire_csv(self):
        with open('etudiants.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['nom', 'prenom', 'age', 'maths', 'pysique', 'info'])
            writer.writerow(['Dupont', 'Marie', '19', '16.5', '14.75', '18'])
            writer.writerow(['Martin', 'Thomas', '20', '12', '13.5', '15.25'])
            writer.writerow(['Leroy', 'Emma', '18', '17.5', '16', '14'])
            writer.writerow(['Petit', 'Lucas', '19', '9', '11', '13.75'])

        with open('etudiants.csv', 'r') as f:
            reader = csv.reader(f)
            for ligne in reader:
                print(ligne)

    def lire_xml(self):
        root = ET.Element('etudiants')

        tree = ET.ElementTree(root)
        tree.write('data.xml')


    def calculer_statistiques(self):
        pass

    def sauvergarder_resultats(self):
        pass

def main():
    pass



if __name__ == '__main__':
    main()
