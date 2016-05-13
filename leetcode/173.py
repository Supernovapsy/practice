# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.largest = root
        while self.largest and self.largest.right:
            self.largest = self.largest.right
        self.newtree = root
        self.ret_stack = []
        self.ret = None # Element next to be returned

    def hasNext(self):
        """
        :rtype: bool
        """
        # invariant: self.ret has not been outputted.
        if self.newtree:
            self.ret = self.newtree
            while self.ret.left:
                self.ret_stack.append(self.ret)
                self.ret = self.ret.left
            self.newtree = self.ret.right
        else:
            if not self.ret_stack:
                return False
            self.ret = self.ret_stack.pop()
            self.newtree = self.ret.right
        return True

    def next(self):
        """ :rtype: int

        Same as the presuccessor function.
        """
        return self.ret.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
