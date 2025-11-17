import datetime
import locale
locale.setlocale(locale.LC_TIME,'')

def afficher_jours_examens(horaire_examen: dict) -> list[str]:
    """
    Cette fonction sert à extraire les jours de la semaines où il y a des examens
    :param horaire_examen: dictionnaire contenant les dates d'examens
    :return: une liste de jours de la semaine
    """
    jours = []
    for examen in horaire_examen:
        date = datetime.datetime.strptime(horaire_examen[examen], "%d/%m/%Y")
        j = date.strftime("%a")
        jours.append(j)
    return jours

if __name__ == '__main__':
    horaire_examen = {
        "math" : "10/12/2015",
        "anglais" : "12/12/2025",
        "français" : "15/12/2025"
    }
    print("Les examens sont :", ", ".join(afficher_jours_examens(horaire_examen)))
