
messages_gr5 = {
    "pseudo" : "IronCode",
    "messages" : ["Le monstre est au niveau 7", "Code 9 activé demain", "La réponse est 142"],
    "signatures" : ["fresea", "odivai", "nses14"]
}

# ***********************************************************************
# creer_signature : Fonction qui crée la signature d'un message
# ************************** Variables ****************************
# Entrées : message (str)
# Intermédiaires : mots (list[str]), mot (str)
# Sorties : resultat (str)
# ***********************************************************************
# --Début--
# Si le message n'est pas un string:
#   Retourner None.
# Initialiser la variable resultat à une liste vide.
# Trouver les mots dans le message en utilisant la méthode str.split.
# Pour chaque mot dans la liste de mots:
#   Si la longeur du mot est supérieure ou égale à 3:
#       Ajouter au résultat la section du mot qui va du troisième caractère avant la fin inclusivement au dernier caractère exclusivement.
# Retourner le résultat.
# --Fin--
def creer_signature(message : str) -> str|None:
    """
    Crée la signature d'un message.
    :param message: Le message dont la signature doit être crée.
    :return: La signature du message. None en cas d'erreur.
    """
    if not isinstance(message, str):
        return None
    resultat : str = ""
    mots : list[str] = message.split() # Doc python
    for mot in mots:
        if len(mot) >= 3:
            resultat += mot[-3:-1]
    return resultat

# ***********************************************************************
# verifier_signature_valide : Fonction qui vérifie si une signature correspond à un message donné.
# ************************** Variables ****************************
# Entrées : message (str), signature (str)
# Intermédiaires : signature_correcte (str)
# Sorties : Le résultat de la fonction (bool ou None)
# ***********************************************************************
# --Début--
# Si le message n'est pas un string ou la signature n'est pas un string:
#   Retourner None.
# Calculer la signature correcte du message à l'aide de la fonction creer_signature.
# Si la signature correcte est None (il y a eu une erreur):
#   Retourner None.
# Si la signature du message est égale à la signature correcte:
#   Retourner Vrai.
# Sinon:
#   Retourner False.
# --Fin--
def verifier_signature_valide(message : str, signature : str) -> bool|None:
    """
    Vérifie si une signature correspond à un message donné.
    :param message: Le message à vérifier.
    :param signature: La signature du message à vérifier.
    :return: Vrai si la siganture correspond au message, sinon Faux. None s'il y a eu une erreur.
    """
    if not isinstance(message, str) or not isinstance(signature, str):
        return None
    signature_correcte : str = creer_signature(message)
    if signature_correcte is None:
        return None
    if signature == signature_correcte:
        return True
    else:
        return False

# ***********************************************************************
# Programme principal
# ************************** Variables ****************************
# Entrées : messages (list[str]), signatures (list[str])
# Intermédiaires : nb_messages (int), nb_signatures (int), message (str), signature (str)
# Sorties : messages_valides (list[str]), messages_alteres (list[str]), messages_sans_signature (list[str]), signatures_sans_message (list[str])
# ***********************************************************************
# --Début--
# Essayer d'obtenir les messages et les signatures du dictionnaire messages_gr5.
# Si il y a une exception KeyError (les messages ou les signatures n'existent pas):
#   Afficher un message d'erreur puis terminer le programme.
# Si les messages ou les signatures ne sont pas des listes:
#   Afficher un message d'erreur puis terminer le programme.
# Pour chaque message:
#   Si le message n'est pas un string:
#       Afficher un message d'erreur puis terminer le programme.
# Pour chaque signature:
#   Si la signature n'est pas un string:
#       Afficher un message d'erreur puis terminer le programme.
# Calculer le nombre de messages avec la fonction len.
# Calculer le nombre de signatures avec la fonction len.
# Initialiser les variables messages_valides, messages_alteres, messages_sans_signature et signatures_sans_message avec des listes vides.
# Si le nombre de signatures est supérieur au nombre de messages:
#   Les signatures sans message sont égales à la section de la liste des signatures qui va du nombre de messages inclusivement à la fin de la liste.
# Pour un index allant de 0 au nombre de message exclusivement:
#   Trouver le message qui correspond à cet index.
#   Si l'index est supérieur ou égal au nombre de signatures:
#       Ajouter le message aux messages sans signature, puis sauter le reste de la boucle.
#   Trouver la signature qui correspond à l'index.
#   Si la signature est valide (en utilisant la fonction verifier_signature_valide avec comme arugments le message et la signature):
#       Ajouter le message au messages valides.
#   Sinon:
#       Ajouter le message au messages altérés.
# ***Répéter ce code pour les 4 variables de sortie (messages_valides, messages_alteres, messages_sans_signature et signatures_sans_message)***
# Si il y a au moins un message ou signature dans la varible de sortie:
#   Afficher un séparateur.
#   Afficher la catégorie qui correspond à la variable de sortie.
#   Pour chaque message ou signature dans la variable de sorite:
#       Afficher le message/la signature.
# --Fin--
def main():
    try:
        messages : list[str] = messages_gr5["messages"]
        signatures : list[str] = messages_gr5["signatures"]
    except KeyError:
        print("Les messages ou les signatures sont absentes!")
        return
    if not isinstance(messages, list) or not isinstance(signatures, list):
        print("Les messages et les signatures doivent être des listes!")
        return
    for message in messages:
        if not isinstance(message, str):
            print("Les messages doivent être une liste de string!")
            return
    for signature in signatures:
        if not isinstance(signature, str):
            print("Les signatures doivent être une liste de string!")
            return

    nb_messages : int = len(messages)
    nb_signatures : int = len(signatures)

    messages_valides : list[str] = []
    messages_alteres : list[str] = []
    messages_sans_signature : list[str] = []
    signatures_sans_message : list[str] = []

    if nb_signatures > nb_messages:
        signatures_sans_message = signatures[nb_messages:]

    for i in range(nb_messages):
        message : str = messages[i]
        if i >= nb_signatures:
            messages_sans_signature.append(message)
            continue
        signature : str = signatures[i]
        if verifier_signature_valide(message, signature):
            messages_valides.append(message)
        else:
            messages_alteres.append(message)

    if messages_valides:
        print("-------------------------------------------")
        print("Messages avec des signatures validées : ")
        for message in messages_valides:
            print(message)
    if messages_alteres:
        print("-------------------------------------------")
        print("Messages altérés, signatures non valides : ")
        for message in messages_alteres:
            print(message)
    if messages_sans_signature:
        print("-------------------------------------------")
        print("Messages sans signature : ")
        for message in messages_sans_signature:
            print(message)
    if signatures_sans_message:
        print("-------------------------------------------")
        print("Signatures sans message : ")
        for signature in signatures_sans_message:
            print(signature)

if __name__ == "__main__":
    main()