/*

================ PREORDER TRAVERSAL (DFS) =================

Traversal Order:
Root → Left → Right


-----------------------------------------------------------
How it works (Visual):
-----------------------------------------------------------

Tree:
                1
             /     \
           2         3
         /   \
        4     5

Traversal:
1 → 2 → 4 → 5 → 3

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------
O(N)
→ Each node is visited once

-----------------------------------------------------------
Space Complexity (Auxiliary Space):
-----------------------------------------------------------
O(H)
H = height of tree (recursion stack)

Worst case (skewed tree): O(N)
Best case (balanced tree): O(log N)

-----------------------------------------------------------
Key Interview Takeaway:
-----------------------------------------------------------
Preorder visits ROOT first and uses recursion,
so space depends on tree height.

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


void preorderTraversal(Node* root){

    if(root == NULL) return;


    cout<<root->data<<" ";
    preorderTraversal(root->left);
    preorderTraversal(root->right);
}



int main(){

    Node* root = new Node(1);

    root->left = new Node(2);
    root->right = new Node(3);

    root->left->right = new Node(4);

    cout<<"Preorder traversal:- ";
    preorderTraversal(root);

    return 0;
}