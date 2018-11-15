from pkg_1.esercizio1 import NewAVLTreeMap

def visual_tree(tree):
    if(isinstance(tree,NewAVLTreeMap)):
        level=""
        for node in tree.breadthfirst():
            level += "("+str(node.element()._key)+" "+str(node._node._balance_factor)+")"#+str(tree.height(node))+")"
        print(level)

def delete_key(tree,k):
    print("Deleting "+str(k))
    del tree[k]
    visual_tree(tree)

if __name__=="__main__":
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
