# -*- coding: utf-8 -*-

#L'anglais a été mis par défaut. Si vous voulez une console en français, changez la string juste en bas à "FR"
CONSOLE_LANGUAGE = "ENG"          
#DO NOT DELETE STATEMENT / NE PAS EFFACER CETTE DÉCLARATION



def solve(testCase):
    joueur = testCase[0]
    tireurs = testCase[1]
    murs = testCase[2]
    # Code goes here / Votre code commence ici 
    
    
    
    
    
    
    
    
    
    
    
    return     #Return test case output here / Retourner la sortie de votre code sur cette ligne







# Do not modify anything beyond this point. / Ne rien modifier après ce point.
# The rest of this code is to facilitate the validation and testing of your code.
# Le reste de ce code sert à faciliter la validation et le test de votre code.

TESTCASES = [[[5,5],[[1,3],[7,2],[3,3],[1,9]],[[0,8,2,4],[4,4,8,4],[5,9,8,6]]],
            [[10,10],[[2,2],[10,3],[7,10]],[[8,10,10,7],[0,0,10,1],[4,6,4,10]]],
            [[3,7],[[0,8],[9,8],[7,0],[10,6]],[[1,8,5,9],[5,10,6,8],[6,7,7,5],[2,6,5,6]]],
            [[9,5],[[9,9],[1,4],[10,2],[2,7]],[[9,4,8,5],[8,5,9,6],[9,6,10,5]]]] #inputs / entrées



ANSWERS = ["0,3",
            "SAFE",
            "0,1",
            "2" ] #expected outputs / sorties attendue



#Function to show if your code works / Fonction pour vous montrer si votre code fonctionne
def checkAnswer():
    score = 0
    print("Votre Sortie:") if CONSOLE_LANGUAGE == "FR" else print("Your Output:")
    
    #Quick print to show all your code's outputs on different lines / Affichage rapide pour vous montrer vos sorties
    outputs = []
    for i, case in enumerate(TESTCASES):
        outputs.append((solve(case)))
        print(outputs[i])
    print()
    
    #To tell you if a testcase is successful / Pour vous dire si un test est réussi
    for caseIndex, out in enumerate(outputs):
        caseIndex += 1
        if out == ANSWERS[caseIndex - 1]:
            print(f"\nTest {caseIndex} réussi.") if CONSOLE_LANGUAGE == "FR" else print(f"\nCase {caseIndex} successful.")
            score+=1
        else:
            print(f"\nTest {caseIndex} non réussi.\nOn s'attendait à \"{ANSWERS[caseIndex-1]}\"\nSortie Obtenue: \"{out}\"") if CONSOLE_LANGUAGE == "FR" else print(""+
                                            f"\nCase {caseIndex} unsuccessful.\nExpected \"{ANSWERS[caseIndex-1]}\"\nGot \"{out}\"")
    
    #Tracking of total number of successful tests / Suivi du nombre total de tests réussis
    print(f"\n{score}/{len(ANSWERS)} tests complétés.") if CONSOLE_LANGUAGE == "FR" else print(f"\n{score}/{len(ANSWERS)} successful test cases.")
    if score == len(ANSWERS):
        print("Tout a l'air bon!") if CONSOLE_LANGUAGE == "FR" else print("Everything seems good!")
    else:
        print("Il semble y avoir un problème avec certaines sorties.") if CONSOLE_LANGUAGE == "FR" else print("There seems to be a problem in the outputs somewhere.")


#DO NOT TOUCH! / NE PAS TOUCHER!
if __name__ == "__main__":
    checkAnswer()
