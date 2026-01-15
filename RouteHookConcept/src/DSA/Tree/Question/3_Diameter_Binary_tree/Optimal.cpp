


/*








=========== DIAMETER OF BINARY TREE (OPTIMIZED APPROACH) ===========

Definition:
Diameter = Longest path between ANY two nodes in the tree  
(Path may or may not pass through root)

Measured in:
➡ Number of EDGES

-----------------------------------------------------------
Tree:
-----------------------------------------------------------

                1
             /     \
           2         3
         /   \
        4     5
       /
      6

-----------------------------------------------------------
Core Idea (Optimized):
-----------------------------------------------------------
• Compute HEIGHT and DIAMETER together in ONE traversal
• While returning height, update diameter

At each node:
Diameter = max(Diameter, Height(left) + Height(right))

👉 Height is NOT recalculated again

-----------------------------------------------------------
Postorder Traversal (Bottom-Up):
-----------------------------------------------------------
(Left → Right → Node)

-----------------------------------------------------------
Step-by-Step Height + Diameter Update:
-----------------------------------------------------------

Node 6:
Left = 0, Right = 0
Diameter = max(0, 0)
Return Height = 1

-----------------------------------------------------------

Node 4:
Left = 1, Right = 0
Diameter = max(0, 1)
Return Height = 2

-----------------------------------------------------------

Node 5:
Left = 0, Right = 0
Diameter = max(1, 0)
Return Height = 1

-----------------------------------------------------------

Node 2:
Left = 2, Right = 1
Diameter = max(1, 3)
Return Height = 3

-----------------------------------------------------------

Node 3:
Left = 0, Right = 0
Diameter = max(3, 0)
Return Height = 1

-----------------------------------------------------------

Node 1:
Left = 3, Right = 1
Diameter = max(3, 4)
Return Height = 4

-----------------------------------------------------------
Final Answer:
-----------------------------------------------------------
Diameter = 4 edges
(Path: 6 → 4 → 2 → 1 → 3)

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------
O(N)

-----------------------------------------------------------
Why O(N)? (Short & Clear):
-----------------------------------------------------------
• Each node is visited exactly ONCE
• Height and diameter updated in the SAME recursion

No repeated height calculation.

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------
O(H)
H = height of the tree (recursion stack)

-----------------------------------------------------------
One-Line Interview Answer:
-----------------------------------------------------------
"By computing height and diameter together in one DFS,
the optimized solution runs in O(N) time."

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



int findHeight(Node* root, int & diameter){

    if(root == NULL) return 0;

    int lh = findHeight(root->left, diameter);
    int rh = findHeight(root->right, diameter);

    diameter = max(diameter, lh + rh);

    return 1 + max(lh, rh);
}


int findDiameter(Node* root){

    int diameter = 0;
    findHeight(root, diameter);

    return diameter;
}



int main(){

    Node* root = new Node(3);

    root->left = new Node(4);
    root->right = new Node(5);

    root->right->left = new Node(7);
    root->right->right = new Node(6);


    root->right->left->left = new Node(9);
    root->right->left->right = new Node(10);



    cout<<"Find the final diameter of the tree:- ";
    cout<<findDiameter(root);

    

    return 0;
}