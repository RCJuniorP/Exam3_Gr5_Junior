
messages_gr5 = {
    "pseudo" : "IronCode",
    "messages" : ["Le monstre est au niveau 7", "Code 9 activé demain", "La réponse est 142"],
    "signatures" : ["fresea", "odivai", "nses14"]
}

# ***********************************************************************
# nom_fonction : Fonction qui fait quelque chose...
#                      deuxième ligne
# ************************** Variables ****************************
# Entrées : var1 (type), var2 (type)
# Intermédiaires : var1 (type)
# Constanes : const1 (type)
# Sorties : return_var (type)
# ***********************************************************************
# --Début--
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
    mots : list[str] = message.split()
    for mot in mots:
        if len(mot) >= 3:
            resultat += mot[-3:-1]
    return resultat

# ***********************************************************************
# nom_fonction : Fonction qui fait quelque chose...
#                      deuxième ligne
# ************************** Variables ****************************
# Entrées : var1 (type), var2 (type)
# Intermédiaires : var1 (type)
# Constanes : const1 (type)
# Sorties : return_var (type)
# ***********************************************************************
# --Début--
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
    return signature == signature_correcte

# ***********************************************************************
# Programme principal
# ************************** Variables ****************************
# Entrées : messages (list[str]), signatures (list[str])
# Intermédiaires : message (str), signature (str)
# Sorties : messages_valides (list[str]), messages_alteres (list[str])
# ***********************************************************************
# --Début--
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
    nb_messages : int = len(messages)
    nb_signatures : int = len(signatures)

    messages_valides : list[str] = []
    messages_alteres : list[str] = []
    messages_sans_signature : list[str] = []
    signatures_sans_message : list[str] = []

    if nb_signatures > nb_messages:
        signatures_sans_message = signatures[nb_messages:]
        for signature_sans_message in signatures_sans_message:
            if not isinstance(signature_sans_message, str):
                print("Les signatures doivent être une liste de string!")
                return

    for i in range(nb_messages):
        message : str = messages[i]
        if not isinstance(message, str):
            print("Les messages doivent être une liste de string!")
            return
        if i >= nb_signatures:
            messages_sans_signature.append(message)
            continue
        signature : str = signatures[i]
        if not isinstance(signature, str):
            print("Les signatures doivent être une liste de string!")
            return
        if verifier_signature_valide(message, signature):
            messages_valides.append(message)
        else:
            messages_alteres.append(message)


    print("Messages avec des signatures validées : ")
    for message in messages_valides:
        print(message)
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
        print(", ".join(signatures_sans_message))

if __name__ == "__main__":
    main()