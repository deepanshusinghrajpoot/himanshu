/*


=========== ITERATIVE PREORDER (DFS) – VISUAL FLOW ===========

Traversal Order:
Root → Left → Right

-----------------------------------------------------------
Tree:
-----------------------------------------------------------

                1
             /     \
           2         3
         /   \
        4     5

-----------------------------------------------------------
Data Structure Used:
-----------------------------------------------------------
STACK  (LIFO)

-----------------------------------------------------------
Step-by-Step Stack Flow:
-----------------------------------------------------------

Initial:
Stack: [1]
Output: []

-----------------------------------------------------------

Step 1:
Pop 1 → visit
Push RIGHT(3), then LEFT(2)

Stack: [3, 2]
Output: [1]

-----------------------------------------------------------

Step 2:
Pop 2 → visit
Push RIGHT(5), then LEFT(4)

Stack: [3, 5, 4]
Output: [1, 2]

-----------------------------------------------------------

Step 3:
Pop 4 → visit

Stack: [3, 5]
Output: [1, 2, 4]

-----------------------------------------------------------

Step 4:
Pop 5 → visit

Stack: [3]
Output: [1, 2, 4, 5]

-----------------------------------------------------------

Step 5:
Pop 3 → visit

Stack: []
Output: [1, 2, 4, 5, 3]

-----------------------------------------------------------
Final Preorder Traversal:
-----------------------------------------------------------
1 → 2 → 4 → 5 → 3

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------
O(N)

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------
O(H)
H = height of tree (stack)

-----------------------------------------------------------
Key Interview Takeaway:
-----------------------------------------------------------
Push RIGHT first so LEFT is processed first.

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

     vector<int>ans;

     stack<Node*>st;
     st.push(root);

     while(!st.empty()){
          
          root = st.top();
          st.pop();

          ans.push_back(root->data);

          if(root->right)  st.push(root->right);
          if(root->left)  st.push(root->left);
     }

     




     for(int i=0; i<ans.size(); i++){
         cout<<ans[i]<<" ";
     }
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