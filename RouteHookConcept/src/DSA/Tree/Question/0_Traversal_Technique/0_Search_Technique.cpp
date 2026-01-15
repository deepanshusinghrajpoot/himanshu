/*



Traversal Technique (BFS / DFS)
=================================



DFS (Depth First Search)
--------------------------

Definition: DFS means go deep in one direction first, then backtrack and explore other paths.
...........



Types of DFS
............

Inorder → Left → Root → Right
Preorder → Root → Left → Right
Postorder → Left → Right → Root



🌳 Large Binary Tree Example
                1
             /     \
           2         3
         /   \     /   \
        4     5   6     7
       / \         \
      8   9         10


✅ Inorder Traversal (Left → Root → Right)
8 → 4 → 9 → 2 → 5 → 1 → 6 → 10 → 3 → 7

✅ Preorder Traversal (Root → Left → Right)
1 → 2 → 4 → 8 → 9 → 5 → 3 → 6 → 10 → 7

✅ Postorder Traversal (Left → Right → Root)
8 → 9 → 4 → 5 → 2 → 10 → 6 → 7 → 3 → 1



⏱ DFS Complexity

Time Complexity: O(N)
Space Complexity: O(H)
        H = height of tree
        Worst case: O(N)
        Balanced tree: O(log N)







BFS (Breadth First Search)
--------------------------

Definition: BFS traverses the tree level by level, from left to right, using a queue.
            Also called Level Order Traversal.



🌳 Same Large Binary Tree
                1
             /     \
           2         3
         /   \     /   \
        4     5   6     7
       / \         \
      8   9         10


✅ BFS Traversal (Level Order)

Visit nodes level by level:

1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10



⏱ BFS Complexity
     Time Complexity: O(N)
     Space Complexity: O(N) (queue in worst case)




*/