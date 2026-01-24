/*



=========== BOUNDARY TRAVERSAL OF BINARY TREE ===========

Definition:
Boundary Traversal = Traverse the boundary of a binary tree
in ANTI-CLOCKWISE order starting from the root.

Boundary includes:
1️⃣ Root node
2️⃣ Left Boundary   (excluding leaf nodes)
3️⃣ All Leaf Nodes  (left → right)
4️⃣ Right Boundary  (excluding leaf nodes, bottom → top)

-----------------------------------------------------------
Tree:
-----------------------------------------------------------

                     1
                  /     \
                2         3
              /   \         \
             4     5         6
            / \     \       / \
           7   8     9    10  11

-----------------------------------------------------------
Step 0️⃣: Root
-----------------------------------------------------------
Start with root (always included)

Result:
[1]

-----------------------------------------------------------
Step 1️⃣: Left Boundary (excluding leaves)
-----------------------------------------------------------
Traverse from root->left
Rule:
• Prefer LEFT child
• If no LEFT, go RIGHT
• Skip leaf nodes

Left Boundary Nodes:
2 → 4

Result:
[1, 2, 4]

-----------------------------------------------------------
Step 2️⃣: Leaf Nodes (left to right)
-----------------------------------------------------------
Traverse entire tree
Add ONLY leaf nodes

Leaf Nodes:
7, 8, 9, 10, 11

Result:
[1, 2, 4, 7, 8, 9, 10, 11]

-----------------------------------------------------------
Step 3️⃣: Right Boundary (excluding leaves, bottom-up)
-----------------------------------------------------------
Traverse from root->right
Rule:
• Prefer RIGHT child
• If no RIGHT, go LEFT
• Skip leaf nodes
• STORE first, ADD in reverse

Right Boundary Nodes (top-down):
3 → 6

Reverse order:
6 → 3

Final Result:
[1, 2, 4, 7, 8, 9, 10, 11, 6, 3]

-----------------------------------------------------------
Final Boundary Traversal (Anti-Clockwise):
-----------------------------------------------------------

1 → 2 → 4 → 7 → 8 → 9 → 10 → 11 → 6 → 3

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------
O(N)

-----------------------------------------------------------
Where does O(N) come from?
-----------------------------------------------------------
• Each node is visited at most once
• Left boundary + leaf traversal + right boundary = N nodes

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------
O(H)

-----------------------------------------------------------
Why O(H)?
-----------------------------------------------------------
• Recursive leaf traversal uses call stack
• H = height of tree

-----------------------------------------------------------
Important Interview Notes:
-----------------------------------------------------------
✔ Root added only once
✔ Leaf nodes never repeated
✔ Right boundary added in reverse order

-----------------------------------------------------------
One-Line Interview Answer:
-----------------------------------------------------------
"Boundary traversal is done in O(N) time by separately
processing left boundary, leaves, and right boundary."

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


bool isLeaf(Node* root){

    if(root->left == NULL && root->right == NULL) return true;
    return false;

}



void left_boundary_traversal(Node* root, vector<int>&result){

    Node* curr = root->left;

    while(curr){
        if(!isLeaf(curr)) result.push_back(curr->data);

        if(curr->left) curr = curr->left;
        else curr = curr->right;
    }
}


void right_boundary_traversal(Node* root, vector<int>&result){

    Node* curr = root->right;

    vector<int>temp;
    while(curr){
        if(!isLeaf(curr)) temp.push_back(curr->data);

        if(curr->right)  curr = curr->right;
        else curr = curr->left;
    }


    for(int i=temp.size() - 1; i>=0; i--){
        result.push_back(temp[i]);
    }
}



void leaf_boundary_traversal(Node* root, vector<int>&result){

    if(isLeaf(root)){
        result.push_back(root->data);
        return;
    }

    if(root->left) leaf_boundary_traversal(root->left, result);
    if(root->right) leaf_boundary_traversal(root->right, result);
}


int main(){

    Node* root1 = new Node(3);

    root1->left = new Node(4);
    root1->right = new Node(5);

    root1->right->left = new Node(7);
    root1->right->right = new Node(6);


    root1->right->left->left = new Node(9);
    root1->right->left->right = new Node(10);




    vector<int>result;

    if(!isLeaf(root1)) result.push_back(root1->data);
    left_boundary_traversal(root1, result);
    leaf_boundary_traversal(root1, result);
    right_boundary_traversal(root1, result);

    
    for(int i=0; i<result.size(); i++){
        cout<<result[i]<<" ";
    }

     

    return 0;
}
