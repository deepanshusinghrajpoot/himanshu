



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





vector<int> top_view_binary_tree(Node* root){

    vector<int>result;

    if(root == NULL) return result;


    map<int, int>mp;
    queue<pair<Node*, int>>qu;

    qu.push({root, 0});

    while(!qu.empty()){

        auto el = qu.front();
        qu.pop();

        root = el.first;
        int vertical = el.second;

        if(mp.find(vertical) == mp.end()) mp[vertical] = root->data;

        if(root->left) qu.push({root->left, vertical-1});
        if(root->right) qu.push({root->right, vertical+1});
    }


    for(auto it: mp){
        result.push_back(it.second);
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


    

    cout<<"Top view of the binary tree:- ";
    vector<int>ans = top_view_binary_tree(root1);

    for(int i=0; i<ans.size(); i++){
        cout<<ans[i]<<" ";
    }


     

    return 0;
}
