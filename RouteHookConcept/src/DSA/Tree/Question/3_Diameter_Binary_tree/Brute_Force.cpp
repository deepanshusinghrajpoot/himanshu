
/*




=========== DIAMETER OF BINARY TREE (NAIVE APPROACH) ===========

Definition:
Diameter = Longest path between ANY two nodes in the tree  
(Path does NOT need to pass through root)

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
Core Idea (Naive):
-----------------------------------------------------------
At every node:
Diameter = max(Diameter, Height(left) + Height(right))

👉 Height is recalculated again and again

-----------------------------------------------------------
Height Values:
-----------------------------------------------------------

Height(6) = 1
Height(4) = 2
Height(5) = 1
Height(2) = 3
Height(3) = 1
Height(1) = 4

-----------------------------------------------------------
Diameter Calculation at Each Node:
-----------------------------------------------------------

At Node 6:
Left = 0, Right = 0
Diameter = 0

-----------------------------------------------------------

At Node 4:
Left = 1, Right = 0
Diameter = max(0, 1) = 1

-----------------------------------------------------------

At Node 2:
Left = 2, Right = 1
Diameter = max(1, 3) = 3

-----------------------------------------------------------

At Node 1:
Left = 3, Right = 1
Diameter = max(3, 4) = 4

-----------------------------------------------------------
Final Answer:
-----------------------------------------------------------
Diameter = 4 edges
(Path: 6 → 4 → 2 → 1 → 3)

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------
O(N²)
→ Height recalculated for each node

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------
O(H)
H = height of tree (recursion stack)

-----------------------------------------------------------
Key Interview Takeaway:
-----------------------------------------------------------
This solution is correct but inefficient.
Optimized solution computes HEIGHT & DIAMETER together.

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



int findHeight(Node* root){

    if(root == NULL) return 0;

    int lh = findHeight(root->left);
    int rh = findHeight(root->right);

    return 1 + max(lh, rh);
}





int findDiameter(Node* root, int & diameter){

    if( root == NULL) return 0;

    int lh = findHeight(root->left);
    int rh = findHeight(root->right);

    diameter = max(diameter, lh + rh);

    findDiameter(root->left, diameter);
    findDiameter(root->right, diameter);
}



int finalSolution(Node* root){

    int diameter = 0;
    findDiameter(root, diameter);

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
    cout<<finalSolution(root);

    

    return 0;
}