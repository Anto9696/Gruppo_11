from pkg_1.esercizio1 import NewAVLTreeMap

# Stampa l'albero tree per livelli. Ogni coppia (k b) k è chiave e b è fattore di bilanciamento
def visual_tree(tree):
    if isinstance(tree,NewAVLTreeMap):
        level=""
        for node in tree.breadthfirst():
            level += "("+str(node.element()._key)+" "+str(node._node._balance_factor)+")"
        print(level)


def delete_key(tree,k):
    print("Deleting "+str(k))
    del tree[k]
    visual_tree(tree)


def scegli():
    print("1. Insert a node ")
    print("2. Delete a node ")
    print("3. Exit")
    scelta = int(input())
    return scelta

if __name__ == "__main__":
    tree = NewAVLTreeMap()

    for i in range(10):
        tree[i]=i
        print("INSERT "+str(i))
        visual_tree(tree)

    # Deleting a leaf
    delete_key(tree,9)
    # Deleting a leaf
    delete_key(tree,4)
    # Deleting a node with one child
    delete_key(tree,5)
    # Deleting a node with two children
    delete_key(tree,1)
    #Need restruct
    delete_key(tree,2)
    delete_key(tree,0)
    # Delete All
    delete_key(tree,7)
    delete_key(tree,6)
    delete_key(tree,3)
    delete_key(tree,8)

    i = scegli()
    while i!=3:
        if i == 1:
            val = int(input("Inserisci chiave "))
            tree[val]=val
            visual_tree(tree)
        elif i == 2:
            val = int(input("Inserisci chiave "))
            delete_key(tree,val)
        else:
            print("Not a good choice!")
        i = scegli()
