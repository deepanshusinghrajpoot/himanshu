
/*




================ BFS (LEVEL ORDER TRAVERSAL) =================

Traversal Type:
Breadth First Search (Level by Level)



-----------------------------------------------------------
How it works (Visual):
-----------------------------------------------------------

Tree:
                1
             /     \
           2         3
         /   \
        4     5

Level Order:
[
  [1],
  [2, 3],
  [4, 5]
]

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------
O(N)
→ Each node is visited once

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------
O(N)
→ Queue can hold all nodes of a level

-----------------------------------------------------------
Key Interview Takeaway:
-----------------------------------------------------------
BFS uses a QUEUE and processes nodes level by level.

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



vector<vector<int>> BFS_usig_queue(Node* root){

    vector<vector<int>>ans;

    if(root == NULL) return ans;

    queue<Node*>qu;
    qu.push(root);

    while(!qu.empty()){
        
        int size = qu.size();
        vector<int>level;

        for(int i=0; i<size; i++){
            Node* node = qu.front();
            qu.pop();

            if(node->left) qu.push(node->left);
            if(node->right) qu.push(node->right);

            level.push_back(node->data);
        }

        ans.push_back(level);
    }

    return ans;
}






int main(){
     
     Node* root = new Node(1);

    root->left = new Node(2);
    root->right = new Node(3);

    root->left->right = new Node(4);

    cout<<"Preorder traversal:- ";
    vector<vector<int>>ans = BFS_usig_queue(root);

    for(int i=0; i<ans.size(); i++){
        for(int j=0; j<ans[i].size(); j++){
            cout<<ans[i][j]<<" ";
        }
    }


    return 0;
}