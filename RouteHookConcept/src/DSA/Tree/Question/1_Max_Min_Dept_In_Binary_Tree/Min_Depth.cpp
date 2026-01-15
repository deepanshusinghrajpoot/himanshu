
/*








=========== MIN DEPTH OF BINARY TREE ===========

Definition:
Minimum number of nodes from ROOT to the nearest LEAF.

-----------------------------------------------------------
Important Rule (Very Important):
-----------------------------------------------------------
If one child is NULL, you MUST take the OTHER child.
(You cannot stop at a non-leaf node)

-----------------------------------------------------------
Tree:
-----------------------------------------------------------

                1
             /     \
           2         3
         /
        4
       /
      5

-----------------------------------------------------------
Why special condition is needed:
-----------------------------------------------------------
Node 2 has only LEFT child.
Right depth = 0 → NOT a valid leaf path.

-----------------------------------------------------------
Recursive Flow (Bottom-Up):
-----------------------------------------------------------

Node 5:
Left = 0, Right = 0
Min Depth = 1

-----------------------------------------------------------

Node 4:
Left = 1, Right = 0
One side is NULL
Min Depth = 1 + max(1, 0) = 2

-----------------------------------------------------------

Node 2:
Left = 2, Right = 0
One side is NULL
Min Depth = 1 + max(2, 0) = 3

-----------------------------------------------------------

Node 3:
Left = 0, Right = 0
Min Depth = 1

-----------------------------------------------------------

Node 1:
Left = 3, Right = 1
Both sides exist
Min Depth = 1 + min(3, 1) = 2

-----------------------------------------------------------
Final Answer:
-----------------------------------------------------------
Min Depth = 2   (1 → 3)

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------
O(N)

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------
O(H)
H = height of tree (recursion stack)

-----------------------------------------------------------
Key Interview Takeaway:
-----------------------------------------------------------
For MIN depth, NULL child must be ignored.
Use MAX when one subtree is missing.

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



int Min_Depth_Binary_Tree(Node* root){

    if(root == NULL) return 0;

    int lh = Min_Depth_Binary_Tree(root->left);
    int rh = Min_Depth_Binary_Tree(root->right);

    if(lh == 0 || rh == 0) return 1 + max(lh, rh);

    return 1 + min(lh, rh);
    
}



int main(){

    Node* root = new Node(3);

    root->left = new Node(4);
    root->right = new Node(5);

    root->right->left = new Node(7);
    root->right->right = new Node(6);


    root->right->left->left = new Node(9);
    root->right->left->right = new Node(10);


    cout<<"Max Depth Of Binary Tree:- ";
    cout<<Min_Depth_Binary_Tree(root);

    return 0;
}