# -*- coding: utf-8 -*-

#L'anglais a été mis par défaut. Si vous voulez une console en français, changez la string juste en bas à "FR"
CONSOLE_LANGUAGE = "ENG"          
#DO NOT DELETE STATEMENT / NE PAS EFFACER CETTE DÉCLARATION

Morse_Code = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def decrypt(message: str) -> str :
    word=message.split("/")
    result=''
    for character in word:
        result+=" "
        letter=character.split()
        for c in letter:
            for keys in Morse_Code.keys():
                if c == Morse_Code[keys]:
                    result+=keys.lower()
    return result.lstrip()    

def encrypt(message: str) -> str:
    word=message.split()
    result=''
    for character in word:
        result+="/"
        letter=list(character)
        for c in letter:
            result+=" "
            for keys in Morse_Code.keys():
                
                if c == keys.lower():
                    result+= Morse_Code[keys]

    result=result.lstrip('/').lstrip()
    result = result.replace("/", " /")
    return result


def solve(testCase):
    text = testCase
    # Code goes here / Votre code commence ici 
    
    
    if text.startswith(".") or text.startswith("-"):
        result=decrypt(text)
    else:
        result=encrypt(text)
    
    
    
    
    
    
    
    
    
    return result #Return test case output here / Retourner la sortie de votre code sur cette ligne







# Do not modify anything beyond this point. / Ne rien modifier après ce point.
# The rest of this code is to facilitate the validation and testing of your code.
# Le reste de ce code sert à faciliter la validation et le test de votre code.

TESTCASES = [".--- --- -.- . ... / --- -. / -.-- --- ..-",
            "this means nothing",
            "-.-. --- ..- -.-. --- ..-",
            "why are we here",
            "alien en haut"
            ] #inputs / entrées



ANSWERS = ["jokes on you",
            "- .... .. ... / -- . .- -. ... / -. --- - .... .. -. --.",
            "coucou",
            ".-- .... -.-- / .- .-. . / .-- . / .... . .-. .",
            ".- .-.. .. . -. / . -. / .... .- ..- -"
            ] #expected outputs / sorties attendue



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
