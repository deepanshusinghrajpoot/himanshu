/*














=========== ITERATIVE POSTORDER (TWO STACKS) – VISUAL FLOW ===========

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
Data Structures Used:
-----------------------------------------------------------
Stack 1 → Processing stack  
Stack 2 → Reverse postorder stack

-----------------------------------------------------------
Core Idea (Very Simple):
-----------------------------------------------------------
1️⃣ Use Stack-1 like preorder (Root → Left → Right)
2️⃣ Push processed nodes into Stack-2
3️⃣ Stack-2 reverses order → gives POSTORDER

-----------------------------------------------------------
Step-by-Step Stack Flow:
-----------------------------------------------------------

Initial:
Stack1: [1]
Stack2: []
Output: []

-----------------------------------------------------------

Step 1:
Pop 1 from Stack1 → push to Stack2
Push LEFT(2), RIGHT(3) into Stack1

Stack1: [2, 3]
Stack2: [1]

-----------------------------------------------------------

Step 2:
Pop 3 → push to Stack2

Stack1: [2]
Stack2: [1, 3]

-----------------------------------------------------------

Step 3:
Pop 2 → push to Stack2
Push LEFT(4), RIGHT(5)

Stack1: [4, 5]
Stack2: [1, 3, 2]

-----------------------------------------------------------

Step 4:
Pop 5 → push to Stack2

Stack1: [4]
Stack2: [1, 3, 2, 5]

-----------------------------------------------------------

Step 5:
Pop 4 → push to Stack2

Stack1: []
Stack2: [1, 3, 2, 5, 4]

-----------------------------------------------------------

Final Step: Pop Stack2 (Reverse Order)
-----------------------------------------------------------

Stack2 Pop Order:
4 → 5 → 2 → 3 → 1

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
O(N)
→ Two stacks used

-----------------------------------------------------------
Key Interview Takeaway:
-----------------------------------------------------------
Two-stack postorder is easier to understand but
uses extra space compared to one-stack solution.

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


void postorder_using_two_stack(Node* root){

    vector<int>ans;

    stack<Node*>st1, st2;

    st1.push(root);

    while(!st1.empty()){
          
        root = st1.top();
        st1.pop();

        st2.push(root);
        
        if(root->left != NULL) st1.push(root->left);
        if(root->right != NULL) st1.push(root->right);
    }

    while(!st2.empty()){
        ans.push_back(st2.top()->data);
        st2.pop();
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
    postorder_using_two_stack(root);

    return 0;
}