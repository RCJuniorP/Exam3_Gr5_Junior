import datetime
import locale
locale.setlocale(locale.LC_TIME,'')

def afficher_jours_examens(horaire_examen: dict) -> list[str]|None:
    """
    Cette fonction sert à extraire les jours de la semaines où il y a des examens
    :param horaire_examen: dictionnaire contenant les dates d'examens
    :return: une liste de jours de la semaine
    """
    jours = []
    if not isinstance(horaire_examen, dict): # Cette fonction se retrouve dans la documentation python
        print("L'horaire d'examen doit être un dictonnaire!")
        return None
    for examen in horaire_examen:
        if not isinstance(examen, str):
            print("Les clés dans le dictionnaire de l'horaire d'examen doivent être des string!")
            return None
        if not isinstance(horaire_examen[examen], str):
            print("Les valeurs dans le dictonnaire de l'horaire d'examen doivent être des string!")
            return None
        try:
            date = datetime.datetime.strptime(horaire_examen[examen], "%d/%m/%Y") # Cette fonction crée une exception ValueError lorsque le format est incorrect (voir documentation python)
        except ValueError:
            print("Une des dates n'est pas sous le bon format!")
            return None
        j = date.strftime("%A") # La documentation python sur strptime() a été utilisée pour corriger ces erreurs.
        jours.append(j)
    return jours

if __name__ == '__main__':
    horaire_examen = {
        "math" : "10/12/2015",
        "anglais" : "12/12/2025",
        "français" : "15/12/2025"
    }
    resultat = afficher_jours_examens(horaire_examen)
    if resultat is None:
        print("Les données sont invalides!")
    else:
        print("Les examens sont :", ", ".join(afficher_jours_examens(horaire_examen)))
