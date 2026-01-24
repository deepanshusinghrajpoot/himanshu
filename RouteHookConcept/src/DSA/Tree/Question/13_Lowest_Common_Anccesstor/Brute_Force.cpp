
/*




=========== LOWEST COMMON ANCESTOR (USING ROOT→NODE PATH) ===========

Definition:
Lowest Common Ancestor (LCA) of two nodes p and q
is the LOWEST node in the tree that has BOTH p and q
as descendants.

-----------------------------------------------------------
Tree:
-----------------------------------------------------------

                     1
                  /     \
                2         3
              /   \     /   \
             4     5   6     7
                  |
                  8

Let:
p = Node(8)
q = Node(4)

-----------------------------------------------------------
Core Idea:
-----------------------------------------------------------

1️⃣ Find path from ROOT → p
2️⃣ Find path from ROOT → q
3️⃣ Compare both paths from ROOT
4️⃣ Last common node = LCA

-----------------------------------------------------------
Step 1️⃣: Root → p Path
-----------------------------------------------------------

p = 8

Path(p):
[1 → 2 → 5 → 8]

-----------------------------------------------------------
Step 2️⃣: Root → q Path
-----------------------------------------------------------

q = 4

Path(q):
[1 → 2 → 4]

-----------------------------------------------------------
Step 3️⃣: Compare Paths
-----------------------------------------------------------

Index-wise comparison:

Index 0: 1 == 1  ✅
Index 1: 2 == 2  ✅
Index 2: 5 != 4  ❌ (STOP)

-----------------------------------------------------------
Lowest Common Node:
-----------------------------------------------------------

LCA = Node(2)

-----------------------------------------------------------
Why This Works:
-----------------------------------------------------------

• Both paths start from root
• Paths remain same until LCA
• First mismatch means last matched node
  was the LOWEST common ancestor

-----------------------------------------------------------
Traversal Used:
-----------------------------------------------------------

DFS (for path finding)

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------
O(N)

-----------------------------------------------------------
Where does O(N) come from?
-----------------------------------------------------------

• Path to p → O(N)
• Path to q → O(N)
• Path comparison → O(N)

Total = O(N)

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------
O(N)

-----------------------------------------------------------
Why O(N)?
-----------------------------------------------------------

• Two path vectors store up to N nodes
• Recursion stack also up to height H

-----------------------------------------------------------
Edge Cases:
-----------------------------------------------------------

• If p == q → LCA is p itself
• If one node is ancestor of other → ancestor is LCA
• If node not present → result is NULL

-----------------------------------------------------------
One-Line Interview Answer:
-----------------------------------------------------------
"Find root-to-node paths for both nodes and the last
common node in both paths is the LCA."

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



bool root_to_node_path(Node* root, vector<Node*>&res, Node* k){

    if(root == NULL) return false;

    res.push_back(root);

    if(root == k)  return true;
    if(root_to_node_path(root->left, res, k) || root_to_node_path(root->right, res, k)) return true;

    res.pop_back();
    return false;
}


Node* lowest_common_anccestor(Node* root, Node* p, Node* q){

    vector<Node*>res1;
    vector<Node*>res2;

    root_to_node_path(root, res1, p);
    root_to_node_path(root, res2, q);

    if(res1.size() <= res2.size()){

        for(int i=res1.size()-1; i>=0; i--){
            if(res1[i] == res2[i]) return res1[i];
        }
    }
    else{

        for(int i=res2.size()-1; i>=0; i--){
            if(res1[i] == res2[i]) return res1[i];
        }
    }

    return NULL;
}



int main(){


    Node* root1 = new Node(3);

    root1->left = new Node(4);
    root1->right = new Node(5);

    root1->right->left = new Node(7);
    root1->right->right = new Node(6);


    root1->right->left->left = new Node(9);
    root1->right->left->right = new Node(10);

    Node* p = root1->right->left->right;
    Node* q = root1->right->right;

    cout<<"Lowest Common Anccestor:- ";
    cout<<lowest_common_anccestor(root1, p, q)->data;

    

    return 0;
}