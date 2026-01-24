
/*





=========== LEFT VIEW OF BINARY TREE ===========

Definition:
Left View = Nodes visible when the tree
is viewed from the LEFT side.

Rule:
For each LEVEL,
➡ pick the FIRST (leftmost) visible node.

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

• Traverse tree using BFS
• Visit RIGHT child first, then LEFT
• For each level:
  overwrite the value in map
• LAST overwritten value = LEFT view

-----------------------------------------------------------
WHY RIGHT FIRST?
-----------------------------------------------------------

• Right child enters queue earlier
• Left child is processed later
• Later overwrite ensures LEFTMOST node survives

-----------------------------------------------------------
Data Structure Used:
-----------------------------------------------------------

map<int, Node*> mp

-----------------------------------------------------------
WHY MAP IS USED?
-----------------------------------------------------------

1️⃣ Level acts as KEY
   → one node per level

2️⃣ map stores keys in SORTED order
   → output from top → bottom

3️⃣ Overwriting guarantees
   → correct LEFT view node

-----------------------------------------------------------
Map Updates (Level-wise):
-----------------------------------------------------------

Level 0 → 1
Level 1 → 2   (overwrites 3)
Level 2 → 4   (overwrites 6, 5)
Level 3 → 7

-----------------------------------------------------------
Final Left View:
-----------------------------------------------------------

Levels:
0    1    2    3
↓    ↓    ↓    ↓
[1,   2,   4,   7]

-----------------------------------------------------------
Final Output:
-----------------------------------------------------------

[1, 2, 4, 7]

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------
O(N log N)

-----------------------------------------------------------
Where does O(N log N) come from?
-----------------------------------------------------------

• BFS traversal → O(N)
• map insert/update → O(log N)

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------
O(N)

-----------------------------------------------------------
Why O(N)?
-----------------------------------------------------------

• Queue + map may store N nodes

-----------------------------------------------------------
One-Line Interview Answer:
-----------------------------------------------------------
"By traversing right first and overwriting per level,
the last stored node gives the left view."

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


vector<int> left_view_binary_tree(Node* root){
       
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

        if(root->right) qu.push({root->right, level + 1});
        if(root->left) qu.push({root->left, level + 1});

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
    vector<int>ans = left_view_binary_tree(root1);

    for(int i=0; i<ans.size(); i++){
        cout<<ans[i]<<" ";
    }

    return 0;
}




