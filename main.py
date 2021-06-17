

def party1():
    joueur1 = input(" Joueur 1 quel est votre nom ? ")
    score = 501

    while score > 0:
        score_volee = input(joueur1 + " entrez votre score: ")
        score -= int(score_volee)
        print(score)
        if score == 0:
            print("Bravo vous avez gagner")
        else:
            pass
        if score < 0:
            score += int(score_volee)
            print(score)
            pass       

def party2():
    joueur1 = input(" Joueur 1 quel est votre nom ? ")
    joueur2 = input(" Joueur 2 quel est votre nom ? ")
    scorej1 = 501
    scorej2 = 501
    while scorej1 > 0 and scorej2 > 0:
        score_voleej1 = input(joueur1 + " entrez votre score: ")
        scorej1 -= int(score_voleej1)
        print(scorej1)
        score_voleej2 = input(joueur2 + " entrez votre score: ")
        scorej2 -= int(score_voleej2)
        print(scorej2)
        if scorej1 == 0 or scorej2 == 0: # surement passer ce if en if et elif pour le print avec le nom 
            print("Bravo vous avez gagner")
        else:
            pass
        if scorej1 < 0:
            scorej1 += int(score_voleej1)
            print(scorej1)
        elif scorej2 < 0:
            scorej2 += int(score_voleej2)
            print(scorej2)
        else:
            pass

        

party2()