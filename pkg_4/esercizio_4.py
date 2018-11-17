
def find_kmp(P, T):
    """Return the lowest index of T at which substring P begins (or else -1)."""
    n = len(T)
    m = len(P)
    if m == 0: return False  #pattern vuoto
    fail = compute_kmp_fail(P) # rely on utility to precompute
    j = 0 # index into text
    k = 0 # index into pattern
    while j < n:
        if T[j] == P[k]: # P[0:k] matched thus far
            if k == m - 1: # match is complete
                return True
            j += 1 # try to extend match
            k += 1
        elif k > 0:
            k = fail[ k -1] # reuse suffix of P[0:k-1]
        else:
            j += 1
    return False # reached end without match

def compute_kmp_fail(P):
    """Utility that computes and returns KMP 'fail' list."""
    m = len(P)
    fail = [0] * m # by default, presume overlap of 0 everywhere
    j = 1
    k = 0
    while j < m: # compute f(j) during this pass, if nonzero
        if P[j] == P[k]: # k + 1 characters match thus far
            fail[j] = k + 1
            j += 1
            k += 1
        elif k > 0: # k follows a matching prefix
            k = fail[k-1]
        else: # no match found starting at j
            j += 1
    return fail

def circular_substring(P, T):
    """restituisce True se P è una sottostringa circolare di T e False altrimenti."""
    n = len(T)
    m = len(P)
    T_extended = T[n-m : n] + T[: n]
    return find_kmp(P, T_extended)



if __name__ == "__main__":    #FARE RUN PER ESEGUIRE IL TEST
    decision = "y"
    while(decision == "y"):
        T = input("Inserisci il testo T: ")
        P = input("Inserisci il pattern da cercare per il quale vuoi sapere se è una sottostringa circolare di T: ")
        result = circular_substring(P, T)
        print(result)
        if(result):
            print("P è una sottostringa circolare di T")
        else:
            print("P è una sottostringa circolare di T")

        decision = input("Vuoi eseguire un altro test? [Y/N]").lower()


