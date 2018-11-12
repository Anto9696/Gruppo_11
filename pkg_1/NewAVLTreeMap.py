from TdP_collections.map.avl_tree import AVLTreeMap,TreeMap

class NewAVLTreeMap(AVLTreeMap):
    """Sorted map implementation using an AVL tree."""

    # -------------------------- nested _Node class --------------------------
    class _Node(TreeMap._Node):
        """Node class for AVL maintains height value for balancing.

        We use convention that a "None" child has height 0, thus a leaf has height 1.
        """
        __slots__ = '_balance_factor'  # additional data member to store height

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._balance_factor = 0  # will be recomputed during balancing

        def left_balance_factor(self):
            return self._left._balance_factor if self._left is not None else 0

        def right_balance_factor(self):
            return self._right._balance_factor if self._left is not None else 0

    # ------------------------- positional-based utility methods -------------------------

    #NOTE => Il fattore di bilanciamento e' left_h - right_h

    def _recompute_balance_factor(self, p):
        if p is None or

    def _recompute_height(self, p):
        p._node._height = 1 + max(p._node.left_height(), p._node.right_height())

    def _isbalanced(self, p):
        return abs(p._node._balance_factor) <= 1

    def _tall_child(self, p, favorleft=False):  # parameter controls tiebreaker
        if p._node.left_height() + (1 if favorleft else 0) > p._node.right_height():
            return self.left(p)
        else:
            return self.right(p)

    def _tall_grandchild(self, p):
        child = self._tall_child(p)
        # if child is on left, favor left grandchild; else favor right grandchild
        alignment = (child == self.left(p))
        return self._tall_child(child, alignment)

    def _rebalance(self, p):
        while p is not None:


    def _recompute_balance_factor(self, p, insert):
        current_node = self.parent(p)
        while current_node is not None:
            if (self.left(current_node) == p and insert) or (self.right(current_node) == p and not insert):
                current_node._node._balance_factor += 1
            else:
                current_node._node._balance_factor -= 1
            p = current_node
            current_node = self.parent(p)

    def _rebalance_insert(self, p):
        #self._recompute_balance_factor(p,True)
        #self._rebalance(p)
        current_node = self.parent(p)
        while current_node is not None:
            if self.left(current_node) == p:
                current_node._node._balance_factor += 1
            else:
                current_node._node._balance_factor -= 1
            if abs(current_node._node._balance_factor) == 2:
                self._restructure(self.left(p) if self.left(p) is not None else self.right(p))
                if self.is_leaf(p):
                    p._node._balance_factor = 0
                    self.parent(p)._node._balance_factor = 0
                    if self.left(self.parent(p)) != p:
                        self.left(self.parent(p))._node._balance_factor = 0
                    else:
                        self.right(self.parent(p))._node._balance_factor = 0
                else:
                    p._node._balance_factor = 0
                    self.left(p)._node._balance_factor = 0
                    self.right(p)._node._balance_factor = 0
            if current_node._node._balance_factor == 0:
                break
            p = current_node
            current_node = self.parent(p)


    def _rebalance_delete(self, p):
        #Recompute balance_factor of parent node deleted
        """        el
"""
        if self.is_leaf(p) or (self.left(p) is not None and self.right(p) is not None):
            tallest_child = None
            if self.is_leaf(p):
                p._node._balance_factor = 0
            elif p._node.left_balance_factor() == p._node.right_balance_factor():  # Se ci sono entrambi i figli almeno 1 ha balance_factor==0
                p._node._balance_factor += 1 * (-1 if self.is_leaf(self.left(p)) else 1)  # Nel caso entrambi hanno balance = 0 ==> 1 è foglia
                tallest_child = self.right(p) if self.is_leaf(self.left(p)) else self.left(p)
            elif p._node.left_balance_factor() == 0:
                p._node._balance_factor -= 1
                tallest_child = self.right(p)
            else:
                p._node._balance_factor += 1
                tallest_child = self.left(p)
            if abs(p._node._balance_factor) == 2:
                tallest_grandchild = self.left(tallest_child) if self.is_leaf(self.right(tallest_child)) else self.right(tallest_child)
                self._restructure(tallest_grandchild)
                #Update balance
                #break ???
            current_node = self.parent(p)
            while current_node is not None:
                if self.right(current_node) == p:
                    current_node._node._balance_factor += 1
                else:
                    current_node._node._balance_factor -= 1

        #Tutti gli altri caso aggiorno ma non propago perchè l'altezza non è cambiata
        elif self.left(p) is None:
            p._node._balance_factor -= 1
        elif self.right(p) is None:
            p._node._balance_factor += 1

