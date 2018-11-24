from pkg_1.esercizio1 import NewAVLTreeMap
from TdP_collections.map.avl_tree import AVLTreeMap

# Stampa l'albero tree per livelli. Ogni coppia (k b) k è chiave e b è fattore di bilanciamento
def visual_tree(tree):
    if isinstance(tree,NewAVLTreeMap):
        level=""
        for node in tree.breadthfirst():
            level += "("+str(node.element()._key)+" "+str(node._node._balance_factor)+")"
        return level


def verify(tree,test_tree):
    if len(tree) != len(test_tree):
        raise ValueError("The trees are not equal")
    tree_iter = tree.breadthfirst()
    tree_iter_test = test_tree.breadthfirst()
    count = 0
    while True:
        try:
            node = next(tree_iter)
            node_test =  next(tree_iter_test)
            if node.element()._key != node_test.element()._key:
                raise ValueError("The trees are not equal")
            count = count + 1
        except StopIteration:
            break
    if len(tree) != count:
        raise ValueError("The trees are not equal")


def delete_key(tree,test_tree,k):
    print("Deleting "+str(k))
    del tree[k]
    del test_tree[k]
    verify(tree,test_tree)


def scegli():
    print("1. Insert a node ")
    print("2. Delete a node ")
    print("3. Print ")
    print("4. Exit")
    scelta = int(input())
    return scelta


if __name__ == "__main__":
    tree = NewAVLTreeMap()
    test_tree = AVLTreeMap()

    for i in range(10):
        tree[i]=i
        test_tree[i]=i
        print("INSERT "+str(i))
        verify(tree,test_tree)

    print(visual_tree(tree))

    # Deleting a leaf
    delete_key(tree,test_tree,9)
    # Deleting a leaf
    delete_key(tree,test_tree,4)
    # Deleting a node with one child
    delete_key(tree,test_tree,5)
    # Deleting a node with two children
    delete_key(tree,test_tree,1)
    #Need restructure
    delete_key(tree,test_tree,2)
    delete_key(tree,test_tree,0)
    # Delete All
    delete_key(tree,test_tree,7)
    delete_key(tree,test_tree,6)
    delete_key(tree,test_tree,3)
    delete_key(tree,test_tree,8)

    for i in range(10):
        tree[-i]=i
        test_tree[-i]=i
        print("INSERT "+str(-i))
        verify(tree,test_tree)

    for i in range(10):
        delete_key(tree,test_tree,-i)

    print("Albero Vuoto!")
    i = scegli()
    while i!=4:
        if i == 1:
            val = int(input("Inserisci chiave "))
            tree[val]=val
            test_tree[val]=val
            verify(tree,test_tree)
        elif i == 2:
            val = int(input("Inserisci chiave "))
            delete_key(tree,test_tree,val)
        elif i==3:
            print(visual_tree(tree))
        else:
            print("Not a good choice!")
        i = scegli()
