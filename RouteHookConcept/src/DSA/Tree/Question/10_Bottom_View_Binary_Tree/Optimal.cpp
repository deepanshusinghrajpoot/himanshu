
/*








=========== BOTTOM VIEW OF BINARY TREE ===========

Definition:
Bottom View shows the nodes visible when the tree
is viewed from the BOTTOM.

Rule:
For each vertical column,
➡ take the LAST (deepest) node encountered.

-----------------------------------------------------------
Coordinate System Used:
-----------------------------------------------------------

Each node has a vertical index:

• Root → vertical = 0
• Left child  → vertical - 1
• Right child → vertical + 1

-----------------------------------------------------------
Tree:
-----------------------------------------------------------

                     1
                  /     \
                2         3
              /   \         \
             4     5         6
                   \
                    7

-----------------------------------------------------------
Vertical Mapping (BFS Order):
-----------------------------------------------------------

Node 1 → v = 0
Node 2 → v = -1
Node 3 → v =  1
Node 4 → v = -2
Node 5 → v =  0
Node 6 → v =  2
Node 7 → v =  1

-----------------------------------------------------------
Core Idea:
-----------------------------------------------------------

• Traverse tree using BFS (level order)
• For each vertical:
  overwrite the node value
• Last node stored at each vertical = bottom view

-----------------------------------------------------------
WHY BFS?
-----------------------------------------------------------

• BFS goes level by level (top → bottom)
• Deeper nodes come later and overwrite earlier ones
• Ensures correct bottom-most node is kept

-----------------------------------------------------------
Data Structure Used:
-----------------------------------------------------------

map<int, Node*> mp

-----------------------------------------------------------
WHY MAP IS USED?
-----------------------------------------------------------

1️⃣ map stores keys in SORTED order automatically
   → verticals appear from LEFT → RIGHT

2️⃣ Each vertical keeps only ONE node
   → the LAST (bottom-most) node

-----------------------------------------------------------
Map Updates (Step-wise):
-----------------------------------------------------------

Vertical -2 → 4
Vertical -1 → 2
Vertical  0 → 5   (overwrites 1)
Vertical  1 → 7   (overwrites 3)
Vertical  2 → 6

-----------------------------------------------------------
Final Bottom View:
-----------------------------------------------------------

Vertical Order:
-2   -1    0    1    2
 ↓    ↓     ↓    ↓    ↓
[4,   2,    5,   7,   6]

-----------------------------------------------------------
Final Output:
-----------------------------------------------------------

[4, 2, 5, 7, 6]

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------
O(N log N)

-----------------------------------------------------------
Where does O(N log N) come from?
-----------------------------------------------------------

• N nodes processed once (BFS)
• Each insertion/update in map → log N

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------
O(N)

-----------------------------------------------------------
Why O(N)?
-----------------------------------------------------------

• Queue + map store up to N nodes

-----------------------------------------------------------
One-Line Interview Answer:
-----------------------------------------------------------
"Using BFS and map, we overwrite nodes at each vertical,
so the deepest node remains for bottom view."

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


vector<int> bottom_view_binary_tree(Node* root){

     vector<int>result;

     if(root == NULL) return result;


     map<int, Node*>mp;

     queue<pair<Node*, int>>qu;

     qu.push({root, 0});

     while(!qu.empty()){

          auto el = qu.front();
          qu.pop();

          root = el.first;
          int vertical = el.second;

          mp[vertical] = root;

          if(root->left) qu.push({root->left, vertical - 1});
          if(root->right) qu.push({root->right, vertical +  1});
     }


     for(auto p : mp){
        result.push_back(p.second->data);
     }

     return result;
}






int main(){


    Node* root1 = new Node(3);

    root1->left = new Node(4);
    root1->right = new Node(5);

    root1->right->left = new Node(7);
    root1->right->right = new Node(6);


    root1->right->left->left = new Node(9);
    root1->right->left->right = new Node(10);



    cout<<"Bottom view of binary tree:- ";
    vector<int>ans = bottom_view_binary_tree(root1);

    for(int i=0; i<ans.size(); i++){
        cout<<ans[i]<<" ";
    }

    return 0;
}