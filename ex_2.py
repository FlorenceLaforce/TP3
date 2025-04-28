class SolveurNReines:
    def __init__(self, taille, solutions, echiquier):
        self.__taille = taille  #Sert aux dimensions et nb reines
        self.__solutions = solutions
        self.__echiquier = echiquier
        self.__solutions = []
        self.__echiquier = [['. '] * self.__taille for _ in range(self.__taille)]


    def placer_reine(self, l):
        if l == self.__taille:
            resultat = [''.join(ligne) for ligne in self.__echiquier]
            self.__solutions.append(resultat)
            return

    def est_placement_valide(self, ligne, colonne):
        pass


    def resoudre(self):
        pass


    def sauvegarder_solution(self, nom_fichier):
        pass


    def afficher_solutions(self, index):
        pass


solveur = SolveurNReines(4)

nb_solutions = solveur.resoudre()
print(f"Nombre de solutions trouvées: {nb_solutions}")

solveur.afficher_solution(0)

solveur.sauvegarder_solutions("4reines.txt")