
/*



=========== LOWEST COMMON ANCESTOR (OPTIMIZED RECURSIVE) ===========

Definition:
Lowest Common Ancestor (LCA) of nodes p and q
is the LOWEST node that has BOTH p and q
in its left and right subtrees
(or one node itself).

-----------------------------------------------------------
Tree:
-----------------------------------------------------------

                     1
                  /     \
                2         3
              /   \     /   \
             4     5   6     7
                  |
                  8

Let:
p = 8
q = 4

-----------------------------------------------------------
Core Idea:
-----------------------------------------------------------

• Traverse tree using DFS
• Stop recursion when:
  - root is NULL
  - root == p
  - root == q

• Collect results from LEFT and RIGHT

-----------------------------------------------------------
Decision Rules:
-----------------------------------------------------------

1️⃣ If left == NULL → return right  
2️⃣ If right == NULL → return left  
3️⃣ If BOTH are NOT NULL → current node is LCA

-----------------------------------------------------------
Recursive Flow (Key Steps):
-----------------------------------------------------------

At Node 4:
→ root == q
Return 4

-----------------------------------------------------------

At Node 8:
→ root == p
Return 8

-----------------------------------------------------------

At Node 2:
Left returned = 4
Right returned = 8
✔ Both NOT NULL
→ LCA = 2

-----------------------------------------------------------

At Node 1:
Left returned = 2
Right returned = NULL
→ return 2

-----------------------------------------------------------
Final Answer:
-----------------------------------------------------------

LCA = Node(2)

-----------------------------------------------------------
Why This Works:
-----------------------------------------------------------

• If p and q lie in DIFFERENT subtrees
  → first node where paths split is LCA

• If one node is ancestor of other
  → ancestor is returned directly

-----------------------------------------------------------
Traversal Used:
-----------------------------------------------------------

DFS (Postorder-like)

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------
O(N)

-----------------------------------------------------------
Where does O(N) come from?
-----------------------------------------------------------

• Each node is visited ONCE
• No repeated work (unlike path method)

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------
O(H)

-----------------------------------------------------------
Why O(H)?
-----------------------------------------------------------

• Recursive call stack
• H = height of the tree

-----------------------------------------------------------
Edge Cases:
-----------------------------------------------------------

• p == q → that node is LCA
• One node missing → returns the one found
• Tree is skewed → worst-case stack = N

-----------------------------------------------------------
One-Line Interview Answer:
-----------------------------------------------------------
"This DFS approach finds LCA in one traversal
by propagating node presence upward."

===========================================================





*/



#include<bits/stdc++.h>
using namespace std;



class Node{

    public:
       int data;
       Node* left;
       Node* right;


       Node(int data1, Node* left1, Node* right1){
           data = data1;
           left = left1;
           right = right1;
       }


       Node(int data1){
           data = data1;
           left = nullptr;
           right = nullptr;
       }
};



Node* lowest_common_anccestor(Node* root, Node* p, Node* q){

      if(root == NULL || root == p || root == q) return root;

      Node* left = lowest_common_anccestor(root->left, p, q);
      Node* right = lowest_common_anccestor(root->right, p, q);

      if(left == NULL){
        return right;
      }
      else if(right == NULL){
        return left;
      }
      else return root;
}



int main(){


    Node* root1 = new Node(3);

    root1->left = new Node(4);
    root1->right = new Node(5);

    root1->right->left = new Node(7);
    root1->right->right = new Node(6);


    root1->right->left->left = new Node(9);
    root1->right->left->right = new Node(10);

    Node* p = root1->right->left->right;
    Node* q = root1->right->right;

    cout<<"Lowest Common Anccestor:- ";
    cout<<lowest_common_anccestor(root1, p, q)->data;

    

    return 0;
}