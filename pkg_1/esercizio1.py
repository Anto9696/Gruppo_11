from TdP_collections.map.avl_tree import AVLTreeMap,TreeMap

class NewAVLTreeMap(TreeMap):
    """Sorted map implementation using an AVL tree."""

    # -------------------------- nested _Node class --------------------------
    class _Node(TreeMap._Node):
        __slots__ = '_balance_factor'  # additional data member to store height

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._balance_factor = 0  # will be recomputed during balancing

        def left_balance_factor(self):
            return self._left._balance_factor if self._left is not None else None

        def right_balance_factor(self):
            return self._right._balance_factor if self._left is not None else None

    # ------------------------- positional-based utility methods -------------------------

    #NOTE => Il fattore di bilanciamento e' left_h - right_h

    def _tall_child(self, p, favorleft=False):  # parameter controls tiebreaker
        if p._node._balance_factor > 0 or (p._node._balance_factor==0 and favorleft):
            return self.left(p)
        else:
            return self.right(p)

    def _tall_grandchild(self, p):
        child = self._tall_child(p)
        # if child is on left, favor left grandchild; else favor right grandchild
        alignment = (child == self.left(p))
        return self._tall_child(child, alignment)

    def _recompute_balance(self,p):
        if self.is_leaf(p):
            p._node._balance_factor = 0
        elif self.left(p) is None:
            p._node._balance_factor = -1
        elif self.right(p) is None:
            p._node._balance_factor = 1
        else:
            p._node._balance_factor = self.height(self.left(p)) - self.height(self.right(p))

    def _rebalance(self, p, insert):
        current_node = self.parent(p) if insert else p
        while current_node is not None:
            if not insert and self.is_leaf(current_node):
                current_node._node._balance_factor = 0
            elif not insert and self.left(current_node) is None:
                current_node._node._balance_factor -= 1
            elif not insert and self.right(current_node) is None:
                current_node._node._balance_factor += 1
            elif (self.left(current_node) == p and insert) or (self.right(current_node) == p and not insert):
                current_node._node._balance_factor += 1
            else:
                current_node._node._balance_factor -= 1
            if abs(current_node._node._balance_factor) == 2:
                current_node = self._restructure(self._tall_grandchild(current_node))
                self._recompute_balance(self.left(current_node))
                self._recompute_balance(self.right(current_node))
                self._recompute_balance(current_node)
            if (current_node._node._balance_factor == 0 and insert) or (abs(current_node._node._balance_factor) == 1 and not insert):
                current_node = None
            else:
                p = current_node
                current_node = self.parent(p)

    def _rebalance_insert(self, p):
        self._rebalance(p,True)


    def _rebalance_delete(self, p):
        #Recompute balance_factor of parent node deleted
        #self._recompute_balance(p)
        """if abs(p._node._balance_factor) == 2:
            p = self._restructure(self._tall_grandchild(p))
            self._recompute_balance(self.left(p))
            self._recompute_balance(self.right(p))
            self._recompute_balance(p)"""
        self._rebalance(p, False)
        """while p is not None:
            if self.num_children(p) == 1:
                if self.right(p) is None:
                    p._node._balance_factor += 1
                else:
                    p._node._balance_factor -= 1
                propagate = False
            elif self.num_children(p) ==0:
                p._node._balance_factor = 0
                propagate = True
            else:
                if self.is_leaf(self.right(p)) and self.is_leaf(self.left(p)):
                    p._node._balance_factor = 0
                    propagate = True
                elif self.is_leaf(self.right(p)):
                    p._node._balance_factor += 1
                    propagate = False
                else:
                    p._node._balance_factor -= 1
                    propagate = False
            if abs(p._node._balance_factor) == 2:
                p = self._restructure(self._tall_grandchild(p))
                self._recompute_balance(self.left(p))
                self._recompute_balance(self.right(p))
                self._recompute_balance(p)
                propagate = False
            if propagate:
                p = self.parent(p)
            else:
                p = None"""
            #if propagate:""
            #    self._rebalance(p,False)

