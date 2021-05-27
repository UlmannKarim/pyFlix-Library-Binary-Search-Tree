##Comments on recursion:
##
##1. If you have a method that returns something, then the method should
##   always return something, and it should always return something of the 
##   same type. 
##
##2. If you have a recursive method that returns something, then every path
##   through the method *in the source code for the method definition* must
##   have an explicit return statement - in particular, you must return the
##   value of the recursive method call.
##
##
##E.g.
##def is_odd_positive(x):
##    if x < 1:
##        return False
##    elif x == 1:
##        return True
##    else:
##        return is_odd_positive(x-2)
##
##works, but
##
##def is_odd_positive_bad(x):
##    if x < 1:
##        return False
##    elif x == 1:
##        return True
##    else:
##        is_odd_positive_bad(x-2)
##
##does not, because any call with an input parameter greater than 1 does not
##return a value.

class BNode:
    """ An internal node in a (doubly linked) binary tree. """

    def __init__(self, item=None):
        """ Initialise a BNode on creation, with value==item. """
        self._element = item
        self._leftchild = None
        self._rightchild = None
        self._parent = None

    def __str__(self):
        """ Return a string representation of the tree rooted at this node.

            The string will be created by an in-order traversal.
        """
        outstr = ''
        if self._leftchild:
            outstr = outstr + str(self._leftchild)
        outstr = outstr + ' ' + str(self._element)
        if self._rightchild:
            outstr = outstr + str(self._rightchild)
        return outstr

    def get_element(self):
        """ Return the element of this node. """
        return self._element

    def get_leftchild(self):
        """ Return the leftchild of this node. """
        return self._leftchild

    def get_rightchild(self):
        """ Return the rightchild of this node. """
        return self._rightchild

    def get_parent(self):
        """ Return the parent of this node. """
        return self._parent

    def set_element(self, newelement):
        """ Assign newelement as the element of this node, overwriting old value. """
        self._element = newelement

    def set_leftchild(self, newleft):
        """ Assign newleft as the leftchild of this node.

            Return False if newleft is not a BNode; True otherwise.
            Does not enforce consistent parent reference in newleft.
        """
        if newleft is not None and not isinstance(newleft, BNode):
            return False
        self._leftchild = newleft

    def set_rightchild(self, newright):
        """ Assign newright as the rightchild of this node.

            Return False if newright is not a BNode; True otherwise.
            Does not enforce consistent parent reference in newright.
        """
        if newright is not None and not isinstance(newright, BNode):
            return False
        self._rightchild = newright

    def set_parent(self, newparent):
        """ Assign newparent as the parent of this node.

            Return False if newparent is not a BNode; True otherwise.
            Does not enforce consistent child reference in newparent.
        """
        if newparent is not None and not isinstance(newparent, BNode):
            return False
        self._parent = newparent

    def remove_left(self):
        """ Remove and return the left subtree.

            Ensure remaining trees are consistent by updating parent
            and child links.
        """
        temp = self._leftchild
        self._leftchild.set_parent(None)
        self.set_leftchild(None)
        return temp

    def remove_right(self):
        """ Remove and return the right subtree.

            Ensure remaining trees are consistent by updating parent
            and child links.
        """
        temp = self._rightchild
        self._rightchild.set_parent(None)
        self.set_rightchild(None)
        return temp

    def get_height(self):
        """ report the height of this node in the tree. """
        leftheight = -1
        if (self._leftchild):
            leftheight = self._leftchild.get_height()
        rightheight = -1
        if (self._rightchild):
            rightheight = self._rightchild.get_height()
        return 1 + max(leftheight, rightheight)

    def _print_structure(self):
        """ (Private) Print a structured representation of tree at this node. """
        outstr = str(self._element) + '(' + str(self.get_height()) + ')['
        if self._leftchild:
            outstr = outstr + str(self._leftchild._element) + ' '
        else:
            outstr = outstr + '* '
        if self._rightchild:
            outstr = outstr + str(self._rightchild._element) + ']'
        else:
            outstr = outstr + '*]'
        if self._parent:
            outstr = outstr + ' -- ' + str(self._parent._element)
        else:
            outstr = outstr + ' -- *'
        print(outstr)
        if self._leftchild:
            self._leftchild._print_structure()
        if self._rightchild:
            self._rightchild._print_structure()

    def _isthisapropertree(self):
        """ Return True if this node is a properly implemented tree. """
        ok = True
        if self._leftchild:
            if self._leftchild._parent != self:
                ok = False
            if self._leftchild._isthisapropertree() == False:
                ok = False
        if self._rightchild:
            if self._rightchild._parent != self:
                ok = False
            if self._rightchild._isthisapropertree() == False:
                ok = False
        if self._parent:
            if (self._parent._leftchild != self
                    and self._parent._rightchild != self):
                ok = False
        return ok

    def _test():
        root = BNode('a')
        if not root._isthisapropertree():
            print("ERROR! " + str(root) + " is not a proper tree. ")
        print(str(root))
        subL = BNode('b')
        root.set_leftchild(subL)
        subL.set_parent(root)
        if not root._isthisapropertree():
            print("ERROR! " + str(root) + " is not a proper tree. ")
        print(str(root))
        subLR = BNode('c')
        subL.set_rightchild(subLR)
        subLR.set_parent(subL)
        if not root._isthisapropertree():
            print("ERROR! " + str(root) + " is not a proper tree. ")
        print(str(root))
        root._print_structure()
        print("Height of root is " + str(root.get_height()))


import math


class ExprTree(BNode):

    def __init__(self, elt):
        """ Initialise this node as an instance of the superclass (BNode). """
        super().__init__(elt)

    def __str__(self):
        """ Return a string of the expression tree rooted at this node.

            The string will be created by an in-order traversal.
        """
        unarybrackets = ['sq', 'sqrt']
        # unary operators which require brackets around their operand
        # if the operand is a leaf, we force the brackets; otherwise the operand
        # is a non-leaf expression and will create its own brackets
        outstr = ''
        if self._leftchild is None and self._rightchild is None:
            outstr = outstr + str(self._element)
        else:
            if self._parent and self._element not in unarybrackets:
                outstr = '('
                # unary minus is unary, but needs brackets outside the minus
            if self._leftchild:
                outstr = outstr + str(self._leftchild)
            outstr = outstr + str(self._element)
            if self._element in unarybrackets and self._rightchild.is_leaf():
                outstr = outstr + '('
            outstr = outstr + str(self._rightchild)
            if self._element in unarybrackets and self._rightchild.is_leaf():
                outstr = outstr + ')'
            if self._parent and self._element not in unarybrackets:
                outstr = outstr + ')'
        return outstr

    def is_leaf(self):
        if self._leftchild is None and self._rightchild is None:
            return True
        return False

    def eval(self):
        """ Return an evaluation of the tree rooted at this node.

            Assumes that the tree is a simple arithmetic expression,
            involving integers or reals, and the operators +,-,*,/
            sq, sqrt and - (unary minus).
        """
        if self._leftchild == None and self._rightchild == None:
            return self._element
        elif self._leftchild == None:
            if self._element == "-":
                return -1 * self._rightchild.eval()
            elif self._element == "sqrt":
                return math.sqrt(self._rightchild.eval())
            elif self._element == "sq":
                value = self._rightchild.eval()
                return value * value
        elif self._rightchild == None:
            print("ERROR: no left child for " + str(self))
            exit(-1)
        else:
            if self._element == "+":
                return self._leftchild.eval() + self._rightchild.eval()
            if self._element == "-":
                return self._leftchild.eval() - self._rightchild.eval()
            if self._element == "*":
                return self._leftchild.eval() * self._rightchild.eval()
            if self._element == "/":
                return self._leftchild.eval() / self._rightchild.eval()

    def _test():
        three = ExprTree(3)
        four = ExprTree(4)
        mysum = ExprTree("+")
        mysum.set_leftchild(three)
        three.set_parent(mysum)
        mysum.set_rightchild(four)
        four.set_parent(mysum)
        # mysum._print_structure()
        # print(str(three.eval()))
        # print(str(four.eval()))

        print(str(mysum) + ' = ' + str(mysum.eval()))
        # mysum._print_structure()
        # print()

        nine = ExprTree(9)
        mysqrt = ExprTree("sqrt")
        nine.set_parent(mysqrt)
        mysqrt.set_rightchild(nine)
        print(str(mysqrt) + ' = ' + str(mysqrt.eval()))
        # mysqrt._print_structure()
        # print()

        mysq = ExprTree("sq")
        mysq.set_rightchild(mysum)
        mysum.set_parent(mysq)
        print(str(mysq) + ' = ' + str(mysq.eval()))
        # mysq._print_structure()
        # print()

        diff = ExprTree("-")
        diff.set_leftchild(mysq)
        mysq.set_parent(diff)
        diff.set_rightchild(mysqrt)
        mysqrt.set_parent(diff)
        print(str(diff) + ' = ' + str(diff.eval()))
        # diff._print_structure()
        # print()

        two = ExprTree(2)
        uminus = ExprTree("-")
        uminus.set_rightchild(two)
        two.set_parent(uminus)
        divide = ExprTree("/")
        divide.set_leftchild(diff)
        diff.set_parent(divide)
        divide.set_rightchild(uminus)
        uminus.set_parent(divide)
        print(str(divide) + ' = ' + str(divide.eval()))
        # divide._print_structure()
