from TdP_collections.map.avl_tree import TreeMap

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
            return self._right._balance_factor if self._right is not None else None

    # ------------------------- positional-based utility methods -------------------------

    #NOTE => Il fattore di bilanciamento e' left_h - right_h

    def retrieve_balance_factor(self,p):
        return p._node._balance_factor

    # Return the tallest child and a boolean value --> O(1)
    # The boolean value is true if tallest child is the left child
    def _tall_child(self, p, favorleft=False):  # parameter controls tiebreaker
        if p._node._balance_factor > 0 or (p._node._balance_factor==0 and favorleft):
            return self.left(p),True
        else:
            return self.right(p),False

    # Return the tallest grand_child and an integer value "type" --> O(1)
    # Type = 0 ==> Need a single rotatation left to rebalance
    # Type = 1 ==> Need a single rotatation right to rebalance
    # Type = 2 ==> Need a double rotation to rebalance
    def _tall_grandchild(self, p):
        child,sx = self._tall_child(p)
        # if child is on left, favor left grandchild; else favor right grandchild
        alignment = (child == self.left(p))
        grand_child,sx_grandchild = self._tall_child(child, alignment)
        if sx_grandchild==sx and sx_grandchild:
            type = 1
        elif sx_grandchild==sx:
            type = 0
        else:
            type = 2
        return grand_child,type

    # Recompute balance factor after a restructure --> O(1)
    # type is the type of rotation done
    # parent is the root of restructured tree
    # balance_grandchild is the balance_factor of the tallest grandchild before restructure
    def _recompute_balance(self,parent,balance_grandchild,type):
        left = self.left(parent)
        right = self.right(parent)
        if type == 0:
            if parent._node._balance_factor == 0:
                left._node._balance_factor = -1
                parent._node._balance_factor = 1
            else:
                left._node._balance_factor = 0
                parent._node._balance_factor = 0
        elif type == 1:
            if parent._node._balance_factor == 0:
                right._node._balance_factor = 1
                parent._node._balance_factor = -1
            else:
                right._node._balance_factor = 0
                parent._node._balance_factor = 0
        elif type == 2:
            parent._node._balance_factor = 0
            if balance_grandchild == 0:
                left._node._balance_factor = 0
                right._node._balance_factor = 0
            elif balance_grandchild == -1:
                left._node._balance_factor = 1
                right._node._balance_factor = 0
            elif balance_grandchild == 1:
                left._node._balance_factor = 0
                right._node._balance_factor = -1
            else:
                raise ValueError("Not balanced Tree")
        else:
            raise ValueError("Unavailable Type")

    # Rebalance Tree ---> O(log n) where n are number of node
    def _rebalance(self, p, insert):
        current_node = self.parent(p)
        while current_node is not None:
            # Updating Balance_Factor
            if (self.left(current_node) == p and insert) or (self.right(current_node) == p and not insert):
                current_node._node._balance_factor += 1
            else:
                current_node._node._balance_factor -= 1

            # Need a restructure
            if abs(current_node._node._balance_factor) == 2:
                g_child,type = self._tall_grandchild(current_node)
                current_node = self._restructure(g_child)
                self._recompute_balance(current_node,g_child._node._balance_factor,type)

            # Stop conditions
            if (current_node._node._balance_factor == 0 and insert) or (abs(current_node._node._balance_factor) == 1 and not insert):
                current_node = None
            else:
                p = current_node
                current_node = self.parent(p)

    def _rebalance_insert(self, p):
        self._rebalance(p,True)


    def _rebalance_delete(self, p):
        if p is not None:
            if self.is_leaf(p):
                p._node._balance_factor = 0
            elif self.left(p) is None:
                p._node._balance_factor -= 1
            elif self.right(p) is None:
                p._node._balance_factor += 1
            elif self.is_leaf(self.left(p)) and self.is_leaf(self.right(p)):
                p._node._balance_factor = 0
            elif self.is_leaf(self.left(p)):
                p._node._balance_factor -= 1
            elif self.is_leaf(self.right(p)):
                p._node._balance_factor += 1

            if abs(p._node._balance_factor) == 2:
                g_child, type = self._tall_grandchild(p)
                p = self._restructure(g_child)
                self._recompute_balance(p, g_child._node._balance_factor, type)

            if p._node._balance_factor == 0:
                self._rebalance(p,False)

