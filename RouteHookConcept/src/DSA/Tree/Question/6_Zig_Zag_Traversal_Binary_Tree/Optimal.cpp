
/*




=========== ZIG-ZAG / SPIRAL TRAVERSAL OF BINARY TREE ===========

Definition:
Zig-Zag Traversal = Level Order Traversal
where direction ALTERNATES at each level.

Level 0 → Left to Right
Level 1 → Right to Left
Level 2 → Left to Right
…and so on

-----------------------------------------------------------
Tree:
-----------------------------------------------------------

                 1
              /     \
            2         3
          /   \     /   \
         4     5   6     7
        / \               \
       8   9               10

-----------------------------------------------------------
Traversal Strategy:
-----------------------------------------------------------
• Use BFS (Level Order)
• Maintain a direction flag:
  leftToRight = true / false
• For each level:
  - Store values in an array
  - Insert normally or in reverse index

-----------------------------------------------------------
Index Formula (Key Insight):
-----------------------------------------------------------

If leftToRight = true:
    index = i

If leftToRight = false:
    index = (levelSize - 1 - i)

-----------------------------------------------------------
Step-by-Step Level Processing:
-----------------------------------------------------------

Level 0 (leftToRight = true):
Queue: [1]

Level array size = 1
Index used: i

Result:
[1]

-----------------------------------------------------------

Level 1 (leftToRight = false):
Queue: [2, 3]

Index mapping:
i=0 → index=1 → put 2
i=1 → index=0 → put 3

Result:
[3, 2]

-----------------------------------------------------------

Level 2 (leftToRight = true):
Queue: [4, 5, 6, 7]

Index mapping:
i=0 → 4
i=1 → 5
i=2 → 6
i=3 → 7

Result:
[4, 5, 6, 7]

-----------------------------------------------------------

Level 3 (leftToRight = false):
Queue: [8, 9, 10]

Index mapping:
i=0 → index=2 → 8
i=1 → index=1 → 9
i=2 → index=0 → 10

Result:
[10, 9, 8]

-----------------------------------------------------------
Final Zig-Zag Traversal:
-----------------------------------------------------------

[
  [1],
  [3, 2],
  [4, 5, 6, 7],
  [10, 9, 8]
]

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------
O(N)

-----------------------------------------------------------
Where does O(N) come from?
-----------------------------------------------------------
• Each node is pushed & popped from queue ONCE
• Constant work per node

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------
O(N)

-----------------------------------------------------------
Why O(N)?
-----------------------------------------------------------
• Queue can hold up to one full level
• Result array stores all nodes

-----------------------------------------------------------
One-Line Interview Answer:
-----------------------------------------------------------
"Using BFS with alternating index placement,
zig-zag traversal is done in O(N) time."

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






vector<vector<int>> Zig_Zag_Traversal_Binary_Tree(Node* root){
   
    vector<vector<int>>result;

    if(root == NULL) return result;

    bool leftToRight = true;

    queue<Node*>qu;
    qu.push(root);

    while(!qu.empty()){

        int size = qu.size();
        vector<int>level(size);

        for(int i=0; i<size; i++){

            root = qu.front();
            qu.pop();


            int index = leftToRight ? i  : (size - 1 - i);

            level[index] = root->data;


            if(root->left) qu.push(root->left);
            if(root->right) qu.push(root->right);
        }

        leftToRight = !leftToRight;
        result.push_back(level);
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





 

     
    cout<<"Check Two Binary Trees Are Identical:- ";
  
    vector<vector<int>>ans = Zig_Zag_Traversal_Binary_Tree(root1);

    for(int i=0; i<ans.size(); i++){
        for(int j=0; j<ans[i].size(); j++){
            cout<<ans[i][j]<<" ";
        }
    }

    return 0;
}
