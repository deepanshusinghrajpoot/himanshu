
/*




=========== CHECK TWO BINARY TREES ARE IDENTICAL ===========

Definition:
Two binary trees are IDENTICAL if:
• They have the same structure
• Corresponding nodes have the same data

-----------------------------------------------------------
Trees:
-----------------------------------------------------------

Tree P:                     Tree Q:

        1                          1
      /   \                      /   \
     2     3                    2     3
          /                          /
         4                          4

-----------------------------------------------------------
Core Idea:
-----------------------------------------------------------
Compare BOTH trees simultaneously using DFS.

At each step:
1. If both nodes are NULL → identical (true)
2. If one is NULL and other is not → NOT identical
3. If data is different → NOT identical
4. Recursively check:
   • left subtree
   • right subtree

-----------------------------------------------------------
Recursive Flow:
-----------------------------------------------------------

Check(p, q)

→ Compare current node values
→ Go LEFT  (p->left,  q->left)
→ Go RIGHT (p->right, q->right)

-----------------------------------------------------------
Base Cases:
-----------------------------------------------------------

Case 1:
p == NULL && q == NULL
→ true (same structure)

Case 2:
p == NULL || q == NULL
→ false (structure mismatch)

-----------------------------------------------------------
Working Example:
-----------------------------------------------------------

Node(1,1) → equal
  ├── Node(2,2) → equal
  │     ├── NULL, NULL → true
  │     └── NULL, NULL → true
  └── Node(3,3) → equal
        ├── Node(4,4) → equal
        └── NULL, NULL → true

-----------------------------------------------------------
Final Answer:
-----------------------------------------------------------
Trees are IDENTICAL ✅

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------
O(N)

-----------------------------------------------------------
Where does O(N) come from?
-----------------------------------------------------------
• Each node is visited ONCE
• Constant comparison at each node

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------
O(H)
H = height of tree (recursive call stack)

-----------------------------------------------------------
One-Line Interview Answer:
-----------------------------------------------------------
"By recursively comparing corresponding nodes and structure,
we check tree equality in O(N) time."

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





bool Check_Two_Tree_Identical(Node* p, Node* q){

    if(p == NULL  ||  q == NULL) return p == q;

    return (p->data == q->data) 
           && Check_Two_Tree_Identical(p->left, q->left)
           && Check_Two_Tree_Identical(p->right, q->right);
}





int main(){

    Node* root1 = new Node(3);

    root1->left = new Node(4);
    root1->right = new Node(5);

    root1->right->left = new Node(7);
    root1->right->right = new Node(6);


    root1->right->left->left = new Node(9);
    root1->right->left->right = new Node(10);





    Node* root2 = new Node(3);

    root2->left = new Node(4);
    root2->right = new Node(5);

    root2->right->left = new Node(7);
    root2->right->right = new Node(6);


    root2->right->left->left = new Node(9);
    root2->right->left->right = new Node(10);


     
    cout<<"Check Two Binary Trees Are Identical:- ";
    cout<<Check_Two_Tree_Identical(root1, root2);

    return 0;
}
