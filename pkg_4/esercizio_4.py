from TdP_collections.text.find_kmp import find_kmp

def circular_substring(P, T):
    """restituisce True se P è una sottostringa circolare di T e False altrimenti."""
    n = len(T)
    m = len(P)
    if m>0 and n>0:
        T_extended = T[n-m : n]+T
        return find_kmp(T_extended,P) if m <= n else -1
    else:
        raise ValueError("T e/o P sono vuote")


