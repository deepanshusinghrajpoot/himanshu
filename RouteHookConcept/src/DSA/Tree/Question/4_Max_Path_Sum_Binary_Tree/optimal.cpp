/*





=========== MAXIMUM PATH SUM IN BINARY TREE ===========

Definition:
Maximum Path Sum = Maximum sum of values along ANY path
(Path can start & end at ANY node)

Rules:
• Path must be continuous
• Path does NOT need to pass through root
• Path can go left → node → right (once)

-----------------------------------------------------------
Tree:
-----------------------------------------------------------

                1
             /     \
           2         3
         /   \
       -4     5

-----------------------------------------------------------
Core Idea:
-----------------------------------------------------------
At each node:
• Ignore negative paths (use max(0, ...))
• Update global max using:
  
  leftSum + rightSum + node->data

-----------------------------------------------------------
Postorder Traversal (Bottom-Up):
-----------------------------------------------------------
Left → Right → Node

-----------------------------------------------------------
Step-by-Step Calculation:
-----------------------------------------------------------

Node -4:
left = 0, right = 0
maxPSum = max(INT_MIN, -4)
Return = -4 → max(0, -4) = 0

-----------------------------------------------------------

Node 5:
left = 0, right = 0
maxPSum = max(-4, 5)
Return = 5

-----------------------------------------------------------

Node 2:
left = 0, right = 5
maxPSum = max(5, 0 + 5 + 2 = 7)
Return = 2 + max(0, 5) = 7

-----------------------------------------------------------

Node 3:
left = 0, right = 0
maxPSum = max(7, 3)
Return = 3

-----------------------------------------------------------

Node 1:
left = 7, right = 3
maxPSum = max(7, 7 + 3 + 1 = 11)
Return = 1 + max(7, 3) = 8

-----------------------------------------------------------
Final Answer:
-----------------------------------------------------------
Maximum Path Sum = 11
(Path: 5 → 2 → 1 → 3)

-----------------------------------------------------------
Why `max(0, subtreeSum)`?
-----------------------------------------------------------
Negative paths reduce total sum,
so we discard them.

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------
O(N)

-----------------------------------------------------------
Where does O(N) come from?
-----------------------------------------------------------
• Each node visited exactly ONCE
• Constant work at each node:
  - max()
  - addition
  - comparison

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------
O(H)
H = height of tree (recursion stack)

-----------------------------------------------------------
One-Line Interview Answer:
-----------------------------------------------------------
"Using postorder traversal and ignoring negative paths,
maximum path sum is computed in O(N) time."

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


int maximumPathSum(Node* root, int& maxPSum){

    if(root == NULL) return 0;

    int leftSum = max(0, maximumPathSum(root->left, maxPSum));
    int rightSum = max(0, maximumPathSum(root->right, maxPSum));

    maxPSum = max(maxPSum, leftSum + rightSum + root->data);

    return root->data + max(leftSum, rightSum);
}


int maxPathSum(Node* root){
   
    int maxPSum = INT_MIN;
    maximumPathSum(root, maxPSum);
    return maxPSum;

}





int main(){

    Node* root = new Node(3);

    root->left = new Node(4);
    root->right = new Node(5);

    root->right->left = new Node(7);
    root->right->right = new Node(6);


    root->right->left->left = new Node(9);
    root->right->left->right = new Node(10);

    cout<<"Maximum Path Sum:- ";
    cout<<maxPathSum(root);

    return 0;
}