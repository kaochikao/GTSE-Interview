class Solution(object):
    def trimBST(self, root, L, R):

        def trim(node):
            if not node:
                return None

            # if 我自己都已經大於R, 我的right child更不用說
            # 所以，連我自己也去掉，return我的left child
            # but, 如何確保這裡left child都大於L?
                # 由於之所以會traverse到current node, 代表parent是沒被trim的
                # parent val是會比我的left child都小的，所以根本不用看left child.
            elif node.val > R:
                return trim(node.left)
            elif node.val < L:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)