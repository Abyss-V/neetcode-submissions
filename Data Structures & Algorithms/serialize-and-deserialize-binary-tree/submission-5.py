# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
    
        if not root:
            return "N"
        return f"{root.val}" + "-L" + self.serialize(root.left) + "-R"+self.serialize(root.right)
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
   
        s = data.split("-")

        if data[0] == "N":
            return None
        root = TreeNode(int(data[0]))
        p = []
        h = root
        v = set()
        direction = "R"
        p.append(root)
        for d in s[1:]:
            
            if d[0] =="L":
                direction = "L"
            elif d[0] == "R":
                direction = "R"
            if d[1] == "N" and direction == "L":
                p[-1].left = None
                
            elif d[1] == "N" and direction == "R":
                p[-1].right = None
              
                v.add(p[-1])
                p.pop()
                while p and p[-1].right in v:
                    n = p.pop()
                    v.add(n)
                v = set()
            elif d[1].isdigit() and direction == "L":

                p[-1].left = TreeNode(int(d[1:]))
                p.append(p[-1].left)
            elif d[1].isdigit() and direction == "R":
         
                p[-1].right = TreeNode(int(d[1:]))
                p.append(p[-1].right)
             

                
        return h