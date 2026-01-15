
/*




=========== MAX DEPTH / HEIGHT OF BINARY TREE ===========

Definition:
Maximum number of nodes from ROOT to the deepest LEAF.

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
Idea (In One Line):
-----------------------------------------------------------
Height = 1 + max(left subtree height, right subtree height)

-----------------------------------------------------------
Recursive Flow (Bottom-Up):
-----------------------------------------------------------

Node 6:
Left = 0, Right = 0
Height = 1

-----------------------------------------------------------

Node 4:
Left = 1, Right = 0
Height = 2

-----------------------------------------------------------

Node 5:
Left = 0, Right = 0
Height = 1

-----------------------------------------------------------

Node 2:
Left = 2, Right = 1
Height = 3

-----------------------------------------------------------

Node 3:
Left = 0, Right = 0
Height = 1

-----------------------------------------------------------

Node 1:
Left = 3, Right = 1
Height = 4

-----------------------------------------------------------
Final Answer:
-----------------------------------------------------------
Max Depth = 4

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------
O(N)
→ Each node visited once

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------
O(H)
H = height of tree (recursion stack)

Worst case (skewed): O(N)
Best case (balanced): O(log N)

-----------------------------------------------------------
Key Interview Takeaway:
-----------------------------------------------------------
Height is calculated bottom-up using DFS recursion.

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



int Max_Depth_Binary_Tree(Node* root){

    if(root == NULL) return 0;

    int lh = Max_Depth_Binary_Tree(root->left);
    int rh = Max_Depth_Binary_Tree(root->right);

    return 1 + max(lh, rh);
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
    cout<<Max_Depth_Binary_Tree(root);

    return 0;
}