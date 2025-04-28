import string
import random
import time


class MotDePasse:
    def __init__(self, valeur: str):
        if not isinstance(valeur, str):
            raise TypeError("La valeur doit être une chaîne de caractères.")
        self.__valeur = valeur
        self.__longueur = len(valeur)
        self.__score_securite = 0

    def valeur(self):
        return self.__valeur

    def longueur(self):
        return self.__longueur

    def score_securite(self):
        return self.__score_securite

    def contient_minuscules(self) -> bool:
        return any(i.islower() for i in self.__valeur)

    def contient_majuscules(self) -> bool:
        return any(i.isupper() for i in self.__valeur)

    def contient_chiffre(self) -> bool:
        return any(i.isdigit() for i in self.__valeur)

    def contient_symbole(self) -> bool:
        symbole = ": !@#$%^&*()-_+=[]{}|:;',.<>?/"
        return any(i in symbole for i in self.__valeur)

    def calculer_score(self) -> int:
        score = 0
        if self.__longueur <= 4:
            score += 10
        elif 5 <= self.__longueur <= 7:
            score += 25
        elif self.__longueur <= 8:
            score += 50

        if self.contient_minuscules():
            score += 12,5
        if self.contient_majuscules():
            score += 12,5
        if self.contient_chiffre():
            score += 12,5
        if self.contient_symbole():
            score += 12,5

        self.__score_securite = 0 <= score <= 100
        return score

    def suggerer_amelioration(self):
        suggestion = []
        if self.__longueur < 8:
            suggestion.append("Vous devriez augmenter la longueur du mot de passe")
        if not self.contient_minuscules():
            suggestion.append("Vous devriez ajouter des minuscules")
        if not self.contient_majuscules():
            suggestion.append("Vous devriez ajouter des majuscules")
        if not self.contient_chiffre():
            suggestion.append("Vous devriez ajouter des chiffres")
        if not self.contient_symbole():
            suggestion.append("Vous devriez ajouter des des symboles, comme '!@#$%^&*()-_+=[]{}|:;',.<>?/'")


    def tester_force_brute(self, caracteres_connus = 0, max_tentatives = 10000):
        if not isinstance(caracteres_connus, int) or not isinstance(max_tentatives, int):
            raise TypeError("Les paramètres doivent être des entiers.")


        alphabet = string.ascii_letters + string.digits
        connues = self.__valeur[:caracteres_connus]
        inconnues = self.__valeur[caracteres_connus:]

        tentatives = 0
        trouve = False
        debut = time.time()

        while tentatives < max_tentatives:
            tentative = ''.join(random.choices(alphabet, k=len(inconnues)))
            if tentative == inconnues:
                trouve = True
                break
            tentatives += 1

        fin = time.time()
        temps_ecoule = fin - debut
        return trouve, tentatives, temps_ecoule



    def estimer_temps_cassage(self):
        N = 0
        if self.contient_minuscules():
            N += 26
        if self.contient_majuscules():
            N += 26
        if self.contient_chiffre():
            N += 10
        if self.contient_symbole():
            N += 32

        combinaison = N**self.__longueur
        temps_secondes = combinaison/1000000000

        if temps_secondes < 60:
            return f"{temps_secondes:.2f} secondes"
        temps_minutes = temps_secondes/60
        if temps_minutes < 60:
            return f"{temps_minutes:.2f} minutes"
        temps_heures = temps_minutes/60
        if temps_heures < 24:
            return f"{temps_heures:.2f} heures"
        temps_jours = temps_heures/24
        if temps_jours < 365:
            return f"{temps_jours:.2f} jours"
        temps_annee = temps_jours/365
        return f"{temps_annee:.2f} annees"

    def __str__(self):
        mdp_masquee = self.__valeur[1:] + '*' * (self.__longueur - 2)
        return f"Mot de passe: {mdp_masquee}, Score: {self.calculer_score()}/100"

class GenerateurMotdePasse:
    def __init__(self):
        self.__minuscules = string.ascii_lowercase
        self.__majuscules = string.ascii_uppercase
        self.__chiffre = string.digits
        self.__symbole = "!@#$%^&*()-_+=[]{}|:;',.<>?/"

    def generer_aleatoire(self, longueur = 8, avec_symboles = False) -> MotDePasse:
        if not isinstance(longueur, int) or not isinstance(avec_symboles, bool):
            raise TypeError("Mot de passe invalide")

        mdp_aleatoire = self.__minuscules + self.__majuscules + self.__chiffre
        if avec_symboles:
            mdp_aleatoire += self.__symbole
        while True:
            mot = ''.join(random.choice(mdp_aleatoire))
            mdp = MotDePasse(mot)
            if mdp.contient_minuscules() and mdp.contient_majuscules() and mdp.contient_chiffre() and (not avec_symboles or mdp.contient_symbole()):
                return mdp

    def generer_simple(self, mot_base: str):
        if not isinstance(mot_base, str):
            raise TypeError("Mot de passe invalide: Doit être une chaîne de caractères")

        substitution = {"a": '4', "e": '3', "i": '1', "o": '0', "s": "$"}
        nouveau_mdp = ''
        for c in mot_base:
            nouveau_mdp += substitution.get(c.lower(), c)
        nouveau_mdp += str(random.randint(0, 9))
        return MotDePasse(nouveau_mdp)



mon_mdp = GenerateurMotdePasse().generer_aleatoire(1)
print(mon_mdp)