
/*






=========== VERTICAL ORDER TRAVERSAL (BINARY TREE) ===========

Definition:
Vertical Traversal groups nodes column-wise (left → right),
and inside each column:
• Top to bottom
• If same position → sorted order

-----------------------------------------------------------
Coordinate System Used:
-----------------------------------------------------------

Each node is assigned:
(vertical, level)

• Root → (0, 0)
• Left child  → (vertical - 1, level + 1)
• Right child → (vertical + 1, level + 1)

-----------------------------------------------------------
Tree:
-----------------------------------------------------------

                     1
                  /     \
                2         3
              /   \     /   \
             4     5   6     7
                    \
                     8

-----------------------------------------------------------
Assigned Coordinates:
-----------------------------------------------------------

Node 1 → ( 0, 0)
Node 2 → (-1, 1)
Node 3 → ( 1, 1)
Node 4 → (-2, 2)
Node 5 → ( 0, 2)
Node 6 → ( 0, 2)
Node 7 → ( 2, 2)
Node 8 → ( 1, 3)

-----------------------------------------------------------
Data Structure Used:
-----------------------------------------------------------

map< vertical,
     map< level,
          multiset< node values > > >

-----------------------------------------------------------
WHY MAP IS USED? (IMPORTANT)
-----------------------------------------------------------

1️⃣ map keeps KEYS in SORTED order automatically

• Vertical columns appear from LEFT → RIGHT
  (-2 → -1 → 0 → 1 → 2)

• Levels inside a column appear from TOP → BOTTOM
  (0 → 1 → 2 → ...)

👉 No extra sorting required

-----------------------------------------------------------
WHY MULTISET?
-----------------------------------------------------------

• When multiple nodes share SAME (vertical, level)
• multiset stores values in sorted order automatically

Example:
Node 5 & Node 6 both at (0, 2)
multiset → [5, 6]

-----------------------------------------------------------
BFS (Level Order) Why?
-----------------------------------------------------------

• Ensures nodes are processed level by level
• Maintains correct top-to-bottom order

-----------------------------------------------------------
Column-wise Construction:
-----------------------------------------------------------

Vertical -2 → [4]
Vertical -1 → [2]
Vertical  0 → [1, 5, 6]
Vertical  1 → [3, 8]
Vertical  2 → [7]

-----------------------------------------------------------
Final Vertical Traversal Output:
-----------------------------------------------------------

[
  [4],
  [2],
  [1, 5, 6],
  [3, 8],
  [7]
]

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------
O(N log N)

-----------------------------------------------------------
Where does O(N log N) come from?
-----------------------------------------------------------

• N insertions into map / multiset
• Each insertion costs log N (balanced BST)

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------
O(N)

-----------------------------------------------------------
Why O(N)?
-----------------------------------------------------------

• map + multiset + queue store all N nodes

-----------------------------------------------------------
One-Line Interview Answer:
-----------------------------------------------------------
"We use map because it keeps vertical and level keys
automatically sorted, avoiding manual sorting."

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



vector<vector<int>> vertical_traversal_binary_tree(Node* root){


       vector<vector<int>>result;

       if(root == NULL) return result;


       map<int, map<int, multiset<int>>>nodes;

       queue<pair<Node*, pair<int, int>>>qu;

       qu.push({root, {0, 0}});

       while(!qu.empty()){

           auto p = qu.front();
           qu.pop();

           root = p.first;

           int vertical = p.second.first;
           int level = p.second.second;

           nodes[vertical][level].insert(root->data);


           if(root->left) qu.push({root->left, {vertical-1, level+1}});
           if(root->right) qu.push({root->right, {vertical+1, level+1}});
       }


       for(auto p : nodes){
           vector<int>col;
           for(auto q : p.second){
               for(int val : q.second){
                   col.push_back(val);
               }
           }

           result.push_back(col);
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


    
    vector<vector<int>>ans = vertical_traversal_binary_tree(root1);


    for(int i=0; i<ans.size(); i++){
        for(int j=0;  j<ans[i].size(); j++){
            cout<<ans[i][j]<<" ";
        }
    }


     

    return 0;
}
