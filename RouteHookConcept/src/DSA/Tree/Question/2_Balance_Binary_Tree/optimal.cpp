
/*




=========== CHECK BALANCED BINARY TREE ===========

Definition:
A Binary Tree is BALANCED if for every node:
| height(left) − height(right) | ≤ 1

-----------------------------------------------------------
Key Idea (Very Important):
-----------------------------------------------------------
• Return HEIGHT if subtree is balanced  
• Return -1 immediately if subtree is NOT balanced  
• This avoids re-checking heights (optimized)

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
Recursive Flow (Bottom-Up):
-----------------------------------------------------------

Node 6:
Left = 0, Right = 0
Height = 1

-----------------------------------------------------------

Node 4:
Left = 1, Right = 0
|1 - 0| = 1  ✅
Height = 2

-----------------------------------------------------------

Node 5:
Left = 0, Right = 0
Height = 1

-----------------------------------------------------------

Node 2:
Left = 2, Right = 1
|2 - 1| = 1  ✅
Height = 3

-----------------------------------------------------------

Node 3:
Left = 0, Right = 0
Height = 1

-----------------------------------------------------------

Node 1:
Left = 3, Right = 1
|3 - 1| = 2  ❌  (NOT BALANCED)

Return = -1

-----------------------------------------------------------
Final Result:
-----------------------------------------------------------
Tree is NOT BALANCED

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

-----------------------------------------------------------
Key Interview Takeaway:
-----------------------------------------------------------
Use HEIGHT + -1 trick to detect imbalance early
and avoid extra computations.

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



int Check_Balance_Binary_Tree(Node* root){
     
    if(root == NULL) return 0;


    int lh = Check_Balance_Binary_Tree(root->left);
    if(lh == -1) return -1;
    
    int rh = Check_Balance_Binary_Tree(root->right);
    if(rh == -1) return -1;

    if(abs(lh-rh) > 1) return -1;

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
    cout<<Check_Balance_Binary_Tree(root);

    return 0;
}