class MotDePass:
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

    def suggerer_amelioration(self) -> list:
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
        pass

    def estimer_temps_cassage(self):
        pass

    def __str__(self):
        mdp_masquee = self.__valeur[1:] + '*' * (self.__longueur - 2)
        return f"Mot de passe: {mdp_masquee}, Score: {self.calculer_score()}/100"

class GenerateurMotdePasse:
    def __init__(self):
        self.__minuscules = "abcdefghijklmnopqrstuvwxyz"
        self.__majuscules = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


