from tree.tree import makeTree, TreeNode, deconstructTree

def invert_tree(root: TreeNode) -> TreeNode:
    root.left, root.right = root.right, root.left
    if root.left:
        invert_tree(root.left)
    if root.right:
        invert_tree(root.right)
    return root

if __name__ == '__main__':
    input = [1,2,3,4,5,6,7]
    in_tree = makeTree(input)
    out_tree = invert_tree(in_tree)
    output = deconstructTree(out_tree)
    print(output)
    assert output is [1,3,2,7,6,5,4]
