
/*







=========== ROOT TO NODE PATH IN BINARY TREE ===========

Definition:
Find the path from ROOT node to a given TARGET node (k).

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

Target (k) = 8

-----------------------------------------------------------
Core Idea:
-----------------------------------------------------------

• Use DFS (recursion)
• Store path while moving DOWN
• If target not found:
  BACKTRACK (remove last node)

-----------------------------------------------------------
Step-by-Step Path Formation:
-----------------------------------------------------------

Start at root:
Path = [1]

Go Left:
Path = [1, 2]

Go Left:
Path = [1, 2, 4]
→ 4 is NOT target and has no children
❌ Backtrack → remove 4

Path = [1, 2]

Go Right:
Path = [1, 2, 5]

Go Right:
Path = [1, 2, 5, 8]
✅ Target FOUND

-----------------------------------------------------------
Why BACKTRACKING?
-----------------------------------------------------------

• If current path does not lead to target
• Remove node from path
• Try alternate branch

-----------------------------------------------------------
Final Root → Node Path:
-----------------------------------------------------------

[1, 2, 5, 8]

-----------------------------------------------------------
Traversal Used:
-----------------------------------------------------------

DFS (Depth First Search)

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------
O(N)

-----------------------------------------------------------
Why O(N)?
-----------------------------------------------------------

• In worst case, every node is visited once
• Search continues until target is found

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------
O(H)

-----------------------------------------------------------
Why O(H)?
-----------------------------------------------------------

• Recursive call stack
• Path vector stores at most H nodes
• H = height of the tree

-----------------------------------------------------------
Edge Cases:
-----------------------------------------------------------

• Target not present → result vector remains empty
• Target = root → path = [root]

-----------------------------------------------------------
One-Line Interview Answer:
-----------------------------------------------------------
"We use DFS with backtracking to store the path while
moving down and remove nodes if the path fails."

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




bool root_to_node_path(Node* root, vector<int>&res, int k){

      if(root == NULL) return false;


      res.push_back(root->data);

      if(root->data == k) return true;
      if(root_to_node_path(root->left, res, k) || root_to_node_path(root->right, res, k)) return true;


      res.pop_back();
      return false;

}



vector<int> root_to_node(Node* root, vector<int>&res, int k){

    if(root == NULL) return res;
    root_to_node_path(root, res, k);

    return res;
}




int main(){


    Node* root1 = new Node(3);

    root1->left = new Node(4);
    root1->right = new Node(5);

    root1->right->left = new Node(7);
    root1->right->right = new Node(6);


    root1->right->left->left = new Node(9);
    root1->right->left->right = new Node(10);



    vector<int>res;
    vector<int>ans = root_to_node(root1, res, 7);
    
    for(int i=0; i<ans.size(); i++){
        cout<<ans[i]<<" ";
    }


    return 0;
}