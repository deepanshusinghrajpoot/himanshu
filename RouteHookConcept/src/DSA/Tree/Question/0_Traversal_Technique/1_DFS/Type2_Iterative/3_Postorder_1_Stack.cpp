





/*






=========== ITERATIVE POSTORDER (ONE STACK) – VISUAL FLOW ===========

Traversal Order:
Left → Right → Root

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
+ one TEMP pointer (to track right child)

-----------------------------------------------------------
Core Idea (Very Important):
-----------------------------------------------------------
1️⃣ Go LEFT as much as possible
2️⃣ Check RIGHT child
3️⃣ If RIGHT is NULL → VISIT node
4️⃣ Keep popping while coming back from RIGHT subtree

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

Step 2: LEFT is NULL
Right child of 4 = NULL
→ VISIT 4

Stack: [1, 2]
Output: [4]

-----------------------------------------------------------

Step 3:
Top = 2
Right child of 2 = 5 (NOT NULL)
→ move to RIGHT

Node = 5

-----------------------------------------------------------

Step 4: Go LEFT
Push 5 → move to NULL

Stack: [1, 2, 5]
Output: [4]

-----------------------------------------------------------

Step 5:
Right child of 5 = NULL
→ VISIT 5

Stack: [1, 2]
Output: [4, 5]

-----------------------------------------------------------

Step 6:
Now coming back from RIGHT of 2
→ VISIT 2

Stack: [1]
Output: [4, 5, 2]

-----------------------------------------------------------

Step 7:
Top = 1
Right child of 1 = 3
→ move to RIGHT

Node = 3

-----------------------------------------------------------

Step 8:
Push 3 → move LEFT → NULL
Right child of 3 = NULL
→ VISIT 3

Stack: [1]
Output: [4, 5, 2, 3]

-----------------------------------------------------------

Step 9:
Coming back from RIGHT of 1
→ VISIT 1

Stack: []
Output: [4, 5, 2, 3, 1]

-----------------------------------------------------------
Final Postorder Traversal:
-----------------------------------------------------------
4 → 5 → 2 → 3 → 1

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
Postorder is hardest because ROOT is visited LAST.
One-stack solution uses RIGHT-child tracking.

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




void postorder_using_one_stack(Node* root){


    vector<int>ans;

    stack<Node*>st;

    Node* node = root;

    while( node != NULL || !st.empty()){

         if(node != NULL){
            st.push(node);
            node = node->left;
         }
         else{

            Node* temp = st.top()->right;

            if(temp == NULL){
                  temp = st.top();
                  st.pop();

                  ans.push_back(temp->data);

                  while(!st.empty() && temp == st.top()->right){
                     temp = st.top();
                     st.pop();
                     ans.push_back(temp->data);
                  }
            }
            else{
                node = temp;
            }
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

    cout<<"Postorder traversal:- ";
    postorder_using_one_stack(root);

    return 0;
}






