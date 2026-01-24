
/*






=========== RIGHT VIEW OF BINARY TREE ===========

Definition:
Right View = Nodes visible when the tree
is viewed from the RIGHT side.

Rule:
For each LEVEL,
➡ pick the LAST node encountered.

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
Level Assignment:
-----------------------------------------------------------

Root starts at level = 0
Each child → level + 1

Node → Level
1 → 0
2 → 1
3 → 1
4 → 2
5 → 2
6 → 2
7 → 3

-----------------------------------------------------------
Core Idea:
-----------------------------------------------------------

• Traverse tree using BFS (level order)
• For each level:
  overwrite the node value
• Last node stored at each level = RIGHT view

-----------------------------------------------------------
WHY BFS?
-----------------------------------------------------------

• BFS processes nodes level by level
• Rightmost node at a level is visited LAST
• Overwriting guarantees correct node

-----------------------------------------------------------
Data Structure Used:
-----------------------------------------------------------

map<int, Node*> mp

-----------------------------------------------------------
WHY MAP IS USED?
-----------------------------------------------------------

1️⃣ Level is the KEY
   → ensures nodes are grouped by level

2️⃣ map stores keys in SORTED order
   → output comes from top → bottom

3️⃣ Overwriting value keeps
   → the RIGHTMOST node of that level

-----------------------------------------------------------
Map Updates (Level-wise):
-----------------------------------------------------------

Level 0 → 1
Level 1 → 3   (overwrites 2)
Level 2 → 6   (overwrites 4, 5)
Level 3 → 7

-----------------------------------------------------------
Final Right View:
-----------------------------------------------------------

Levels:
0    1    2    3
↓    ↓    ↓    ↓
[1,   3,   6,   7]

-----------------------------------------------------------
Final Output:
-----------------------------------------------------------

[1, 3, 6, 7]

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------
O(N log N)

-----------------------------------------------------------
Where does O(N log N) come from?
-----------------------------------------------------------

• BFS visits N nodes → O(N)
• Each map insertion/update → O(log N)

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
"Using BFS and map, we overwrite nodes per level,
keeping the rightmost node for the right view."

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


vector<int> right_view_binary_tree(Node* root){
       
     vector<int>result;

     if(root == NULL) return result;

     map<int, Node*>mp;

     queue<pair<Node*, int>>qu;

     qu.push({root, 0});

     while(!qu.empty()){

        auto el = qu.front();
        qu.pop();

        root = el.first;
        int level = el.second;

        mp[level] = root;

        if(root->left) qu.push({root->left, level + 1});
        if(root->right) qu.push({root->right, level + 1});
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
    vector<int>ans = right_view_binary_tree(root1);

    for(int i=0; i<ans.size(); i++){
        cout<<ans[i]<<" ";
    }

    return 0;
}