class SolveurNReines:
    def __init__(self, taille):
        self.__taille = taille  # équivaut à n
        self.__solutions = []  # liste de chaque solutions existante
        self.__echiquier = []  # "Tableau" d'échiquier"


    def placer_reine(self, colonne):
        if colonne == self.__taille:
            self.__solutions.append(self.__echiquier.copy())

        for ligne in range(self.__taille):
            if self.est_placement_valide(ligne, colonne):
                self.__echiquier[colonne] = ligne
                self.placer_reine(colonne + 1)
                self.__echiquier[colonne] = -1

    def est_placement_valide(self, ligne, colonne):
        for c in range(colonne):
            l = self.__echiquier[c]
            if l == ligne or abs(l - ligne) == abs(c - colonne):
                return False
        return True


    def resoudre(self):
        self.__solutions = []
        self.__echiquier = [-1] * self.__taille
        self.placer_reine(0)
        return len(self.__solutions)


    def sauvegarder_solution(self, nom_fichier):
        with open(nom_fichier, 'w') as f:
            for sol in self.__solutions:
                f.write(f'Solution #{sol}\n')
                for ligne in range(self.__taille):
                    row = ['. '] * self.__taille
                    row[sol[ligne]] = 'Q '
                    f.write(''.join(row) + '\n')
                f.write('\n')


    def afficher_solutions(self, index):
        if 0 <= index < len(self.__solutions):
            sol = self.__solutions[index]
            for ligne in range(self.__taille):
                row = ['. '] * self.__taille
                row[sol[ligne]] = 'Q '
                print(''.join(row))
        else:
            print('Indice de solution invalide.')


solveur = SolveurNReines(4)

nb_solutions = solveur.resoudre()
print(f"Nombre de solutions trouvées: {nb_solutions}")

solveur.afficher_solutions(0) # 0 signifie la première solution

solveur.sauvegarder_solution("4reines.txt")
