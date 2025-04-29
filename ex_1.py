import json
import csv
import xml.etree.ElementTree as ET
import statistics
import os


class AgregateurDonnees:
    def __init__(self):
        self.donnees = []  # liste pour stocker toutes les données

    def lire_csv(self, chemin_fichier):
        try:
            with open(chemin_fichier, newline='', encoding='utf-8') as csvfile:
                lecteur = csv.DictReader(csvfile)
                for ligne in lecteur:
                    etudiant = {
                        "nom": f"{ligne['prenom']} {ligne['nom']}",
                        "age": int(ligne['age']),
                        "maths": float(ligne['mathematiques']),
                        "physique": float(ligne['physique']),
                        "informatique": float(ligne['informatique'])
                    }
                    self.donnees.append(etudiant)
        except FileNotFoundError:
            print(f"Erreur : Fichier {chemin_fichier} introuvable.")
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier CSV : {e}")

    def lire_json(self, chemin_fichier):
        try:
            with open(chemin_fichier, encoding='utf-8') as jsonfile:
                data = json.load(jsonfile)
                for etu in data:
                    etudiant = {
                        "nom": etu["nom_complet"],
                        "age": int(etu["age"]),
                        "maths": float(etu["notes"]["maths"]),
                        "physique": float(etu["notes"]["physique"]),
                        "informatique": float(etu["notes"]["info"])
                    }
                    self.donnees.append(etudiant)
        except FileNotFoundError:
            print(f"Erreur : Fichier {chemin_fichier} introuvable.")
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier JSON : {e}")

    def lire_xml(self, chemin_fichier):
        try:
            tree = ET.parse(chemin_fichier)
            root = tree.getroot()
            for etu in root.findall('etudiant'):
                nom = etu.find('prenom').text + " " + etu.find('nom').text
                age = int(etu.find('age').text)
                notes = {"maths": 0, "physique": 0, "informatique": 0}
                for matiere in etu.find('resultats').findall('matiere'):
                    nom_matiere = matiere.attrib['nom']
                    note = float(matiere.text)
                    if nom_matiere == "mathematiques":
                        notes["maths"] = note
                    elif nom_matiere == "physique":
                        notes["physique"] = note
                    elif nom_matiere == "informatique":
                        notes["informatique"] = note
                etudiant = {
                    "nom": nom,
                    "age": age,
                    "maths": notes["maths"],
                    "physique": notes["physique"],
                    "informatique": notes["informatique"]
                }
                self.donnees.append(etudiant)
        except FileNotFoundError:
            print(f"Erreur : Fichier {chemin_fichier} introuvable.")
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier XML : {e}")

    def calculer_statistiques(self):
        if not self.donnees:
            print("Aucune donnée disponible pour calculer les statistiques.")
            return None

        stats = {}

        # Notes
        for matiere in ['maths', 'physique', 'informatique']:
            notes = [etu[matiere] for etu in self.donnees if matiere in etu]
            if notes:
                stats[matiere] = {
                    "moyenne": round(statistics.mean(notes), 2),
                    "mediane": round(statistics.median(notes), 2),
                    "ecart_type": round(statistics.stdev(notes), 2) if len(notes) > 1 else 0
                }

        # Répartition par âge
        tranches_age = {"18-19": 0, "20-21": 0, "22+": 0}
        for etu in self.donnees:
            age = etu["age"]
            if 18 <= age <= 19:
                tranches_age["18-19"] += 1
            elif 20 <= age <= 21:
                tranches_age["20-21"] += 1
            else:
                tranches_age["22+"] += 1
        stats["repartition_ages"] = tranches_age

        # Meilleurs étudiants (moyenne générale)
        for etu in self.donnees:
            etu["moyenne"] = (etu["maths"] + etu["physique"] + etu["informatique"]) / 3

        meilleurs = sorted(self.donnees, key=lambda x: x["moyenne"], reverse=True)[:3]
        stats["meilleurs_etudiants"] = [(etu["nom"], round(etu["moyenne"], 2)) for etu in meilleurs]

        return stats

    def sauvegarder_resultats(self, nom_fichier):
        stats = self.calculer_statistiques()
        if stats is None:
            return

        try:
            with open(nom_fichier, 'w', encoding='utf-8') as f:
                for matiere in ['maths', 'physique', 'informatique']:
                    f.write(f"Statistiques pour {matiere}:\n")
                    for cle, val in stats[matiere].items():
                        f.write(f"  {cle.capitalize()}: {val}\n")
                    f.write("\n")

                f.write("Répartition par tranche d'âge:\n")
                for tranche, count in stats["repartition_ages"].items():
                    f.write(f"  {tranche} ans: {count} étudiants\n")
                f.write("\n")

                f.write("Top 3 des meilleurs étudiants:\n")
                for nom, moyenne in stats["meilleurs_etudiants"]:
                    f.write(f"  {nom} avec une moyenne de {moyenne}\n")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde des résultats : {e}")





agregateur = AgregateurDonnees()
agregateur.lire_csv("etudiants.csv")
agregateur.lire_json("etudiants.json")
agregateur.lire_xml("etudiants.xml")

stats = agregateur.calculer_statistiques()
if stats:
    for matiere, info in stats.items():
        print(f"{matiere}:", info)

agregateur.sauvegarder_resultats("resultats.txt")
