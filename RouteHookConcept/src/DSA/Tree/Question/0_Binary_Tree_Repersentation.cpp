/*



Binary Tree Repersentation in c++
-----------------------------------


Binary Tree Example
        1
       / \
      2   3
       \
        5

Explanation

1 → Root node
2 and 3 → Children of root
5 → Right child of node 2
3 and 5 → Leaf nodes


*/








#include<bits/stdc++.h>
using namespace std;


 class Node{
     
  public:

    int data;
    Node* left;
    Node* right;

    Node(int data1){
        data = data1;
        left = nullptr;
        right = nullptr;
    }
 };



int main(){

    Node* root = new Node(1);

    root->left = new Node(2);
    root->right = new Node(3);

    root->left->right = new Node(5);

    return 0;
}