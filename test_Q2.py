import pytest
from Q2 import afficher_jours_examens

@pytest.mark.parametrize("horaire_examen, resultat_attendu", [ # Méthode vue en classe
    ({"math" : "10/12/2015", "anglais" : "12/12/2025", "français" : "15/12/2025"}, ["jeudi", "vendredi", "lundi"]),
    ({"math" : "10/12/2015", "anglais" : "12/12/2025", "français" : "2025"}, None),
    ({"histoire" : "19/11/2025", "français" : "22/11/2025", "Édu" : "2/12/2025"}, ["mercredi", "samedi", "mardi"]),
    (["histoire", "19/11/2025"], None),
    ("123", None),
    ({"math" : "10/12/2015", "anglais" : "12/12/2025", 2025 : "2/4/2025"}, None)
])
def test_afficher_jours_examens(horaire_examen, resultat_attendu):
    resultat_obtenu = afficher_jours_examens(horaire_examen)
    assert isinstance(resultat_obtenu, list) or resultat_obtenu is None
    assert resultat_obtenu == resultat_attendu