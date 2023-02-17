# -*- coding: utf-8 -*-

#L'anglais a été mis par défaut. Si vous voulez une console en français, changez la string juste en bas à "FR"
CONSOLE_LANGUAGE = "ENG"          
#DO NOT DELETE STATEMENT / NE PAS EFFACER CETTE DÉCLARATION

filename = "trudeau_international_hourly_january_2023.csv"

#content of every array you should return
name_stats = [["monthly_average_temperature"], ["moving_average_temperature"], ["monthly_standard_deviation_temperature"], ["monthly_median_temperature"], ["monthly_sknewness_temperature"], ["weekly_lowest_value_temperature"], ["weekly_highest_value_temperature"], ["monthly_lowest_recorded_value_temperature"], ["monthly_highest_record_value_temperature"], ["monthly_average_humidity"], ["moving_average_humidity"], ["monthly_standard_deviation_humidity"], ["monthly_median_humidity"], ["monthly_sknewness_humidity"], ["weekly_lowest_value_humidity"], ["weekly_highest_value_humidity"], ["monthly_lowest_recorded_value_humidity"], ["monthly_highest_record_value_humidity"], ["monthly_average_wind"], ["moving_average_wind"], ["monthly_standard_deviation_wind"], ["monthly_median_wind"], ["monthly_sknewness_wind"], ["weekly_lowest_value_wind"], ["weekly_highest_value_wind"], ["monthly_lowest_recorded_value_wind"], ["monthly_highest_record_value_wind"]]

def solve(filename: str) -> list:
    filename = filename
    # Code goes here / Votre code commence ici 
    



    return      #Return test case output here / Retourner la sortie de votre code sur cette ligne



# Do not modify anything beyond this point. / Ne rien modifier après ce point.
# The rest of this code is to facilitate the validation and testing of your code.
# Le reste de ce code sert à faciliter la validation et le test de votre code.


#Function to show if your code works / Fonction pour vous montrer si votre code fonctionne
def checkAnswer():
    print("Souvenez-vous, on ne vous donne pas les réponses pour ce problème") if CONSOLE_LANGUAGE == "FR" else print("Remember, we are not giving answer for this problem")
    print("Votre Sortie:") if CONSOLE_LANGUAGE == "FR" else print("Your Output:")
    
    #Quick print to show all your code's outputs on different lines / Affichage rapide pour vous montrer vos sorties
    for i, element in enumerate(solve(filename)):
        print(name_stats[i][0])
        print(element)
#DO NOT TOUCH! / NE PAS TOUCHER!
if __name__ == "__main__":
    checkAnswer()