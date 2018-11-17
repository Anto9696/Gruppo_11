from TdP_collections.text.find_kmp import find_kmp

def circular_substring(P, T):
    """restituisce True se P è una sottostringa circolare di T e False altrimenti."""
    n = len(T)
    m = len(P)
    T_extended = T[n-m : n]+T[: n]
    print(T_extended)
    return find_kmp(T_extended,P)


