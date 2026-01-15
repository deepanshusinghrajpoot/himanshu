

/*



=========== ITERATIVE INORDER (DFS) – VISUAL FLOW ===========

Traversal Order:
Left → Root → Right

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
Idea (In One Line):
-----------------------------------------------------------
Go LEFT as much as possible → VISIT → then go RIGHT

-----------------------------------------------------------
Step-by-Step Stack Flow:
-----------------------------------------------------------

Initial:
Node = 1
Stack = []
Output = []

-----------------------------------------------------------

Step 1: Go LEFT
Push 1 → move to 2
Push 2 → move to 4
Push 4 → move to NULL

Stack: [1, 2, 4]
Output: []

-----------------------------------------------------------

Step 2: Visit (when LEFT is NULL)
Pop 4 → visit

Stack: [1, 2]
Output: [4]

Move RIGHT of 4 → NULL

-----------------------------------------------------------

Step 3:
Pop 2 → visit

Stack: [1]
Output: [4, 2]

Move RIGHT of 2 → 5

-----------------------------------------------------------

Step 4: Go LEFT again
Push 5 → move to NULL

Stack: [1, 5]
Output: [4, 2]

-----------------------------------------------------------

Step 5:
Pop 5 → visit

Stack: [1]
Output: [4, 2, 5]

Move RIGHT of 5 → NULL

-----------------------------------------------------------

Step 6:
Pop 1 → visit

Stack: []
Output: [4, 2, 5, 1]

Move RIGHT of 1 → 3

-----------------------------------------------------------

Step 7:
Push 3 → move LEFT → NULL
Pop 3 → visit

Stack: []
Output: [4, 2, 5, 1, 3]

-----------------------------------------------------------
Final Inorder Traversal:
-----------------------------------------------------------
4 → 2 → 5 → 1 → 3

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
Inorder = LEFT first, so we push nodes until NULL,
then visit and move RIGHT.

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




void  inorderTraversal(Node* root){
  
      vector<int>ans;
      
      stack<Node*>st;

      Node* node = root;

      while(true){

           if(node != NULL){
              st.push(node);
              node = node->left;
           }
           else{
              if(st.empty() == true)  break;

              node = st.top();
              st.pop();

              ans.push_back(node->data);

              node = node->right;
           }
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

    cout<<"Inorder traversal:- ";
    inorderTraversal(root);

    return 0;
}