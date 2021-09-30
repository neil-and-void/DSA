from typing import *

def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    zz_orders = []
    def df_traversal(root, lvl, zz_orders):
        # base
        if root == None:
            return

        # recursive
        else:
            if len(zz_orders) <= lvl:
                zz_orders.append([])
            zz_orders[lvl].append(root.val)

            df_traversal(root.left, lvl+1, zz_orders)
            df_traversal(root.right, lvl+1, zz_orders)

    print(zz_orders)

