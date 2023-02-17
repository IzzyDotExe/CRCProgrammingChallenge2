# -*- coding: utf-8 -*-

#L'anglais a été mis par défaut. Si vous voulez une console en français, changez la string juste en bas à "FR"
CONSOLE_LANGUAGE = "ENG"          
#DO NOT DELETE STATEMENT / NE PAS EFFACER CETTE DÉCLARATION



def solve(testCase):
    text = testCase
    # Code goes here / Votre code commence ici 
    
    
    
    
    
    
    
    return   #Return test case output here / Retourner la sortie de votre code sur cette ligne



# Do not modify anything beyond this point. / Ne rien modifier après ce point.
# The rest of this code is to facilitate the validation and testing of your code.
# Le reste de ce code sert à faciliter la validation et le test de votre code.

TESTCASES = ["Vanier = Rouge", "RWA = Exacto", "Marcy = Tea", "Vert -> Blanc", "Vert = Coffee", "Pizza = Pince", "Jaune = Ramen", "Kiosk2 = Lait", "Kiosk0 = BdeB", "Marteau -> Spag", "Ramen -> Drill", "Burger = Jus", "CAL = Poutine", "BdeB -> Bleu", "Eau -> Spag"]


#Function to show if your code works / Fonction pour vous montrer si votre code fonctionne
def checkAnswer():
    print("Votre Sortie:") if CONSOLE_LANGUAGE == "FR" else print("Your Output:")
    
    #Quick print to show all your code's outputs on different lines / Affichage rapide pour vous montrer vos sorties
    output = solve(TESTCASES)
    for i in range(6):
        for j in range(5):
            try:
                print(output[j][i], end='\t')
            except:
                print("Dimensions invalides") if CONSOLE_LANGUAGE == "FR" else print("Invalid dimensions")
                return
        print()

#DO NOT TOUCH! / NE PAS TOUCHER!
if __name__ == "__main__":
    checkAnswer()
