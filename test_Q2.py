import pytest
from Q2 import afficher_jours_examens

@pytest.mark.parametrize("horaire_examen, resultat_attendu", [
    ({"math" : "10/12/2015", "anglais" : "12/12/2025", "français" : "15/12/2025"}, ["jeudi", "vendredi", "lundi"])
])
def test_afficher_jours_examens(horaire_examen, resultat_attendu):
    resultat_obtenu = afficher_jours_examens(horaire_examen)
    assert type(resultat_obtenu) == type(resultat_attendu)
    assert resultat_obtenu == resultat_attendu