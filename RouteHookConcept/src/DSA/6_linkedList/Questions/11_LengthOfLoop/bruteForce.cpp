


/*

141. Length of Linked List Cycle
=======================

Example (one frame):

Approach Used:
Hashing using map<Node*, int> (store visit index)


Base Case
=========
If head == NULL  
→ No loop  
→ Return 0


Input (Loop Present):
--------------------
1 --------> 2 --------> 3 --------> 4 --------> 5
              ^                    |
              |--------------------|


Time Complexity (T.C):
O(N log N)
(map insert + lookup)


Space Complexity (S.C):
O(N)


Working (Conceptual, no table)
==============================
• Traverse the linked list node by node  
• Store each node’s address with its visit index  
• If a node is visited again:
  loop length = current_index − first_index_of_that_node  


Example Explanation
===================
First visit:
3 stored with index = 3  

Second visit:
3 encountered again at index = 6  

Loop Length:
6 − 3 = 3  


Why This Works
==============
✔ Repeated node means loop exists  
✔ Index difference gives exact loop length  
✔ Stops immediately on detecting loop  
✔ Easy to understand but uses extra memory  


Final Output:
Loop Length = 3  
(No loop → returns 0)


*/



#include<bits/stdc++.h>
using namespace std;


class Node{

    public:
       int data;
       Node* next;


    public:
       Node(int data1, Node* next1){
          data = data1;
          next = next1;
       }


       Node(int data1){
         data = data1;
         next = nullptr;
       }
};





int lengthOfLoop(Node* head){

     map<Node*, int>mp;

     Node* temp = head;
     int index = 1;

     while(temp){     
        if(mp.find(temp) != mp.end()) return index - mp[temp];
        mp[temp] = index;
        index++;
        temp  = temp->next;
     }

     return 0;
}








Node* convertArrIntoLinkedList(vector<int>&arr){

    Node* head = new Node(arr[0]);

    Node* move = head;

    for(int i=1; i<arr.size(); i++){

        Node* newNode = new Node(arr[i]);
        
        move->next = newNode;
        move = newNode;
    }

    return head;
}


void traverseLinkedList(Node* head){

    Node* temp = head;

    while(temp){

        cout<<temp->data<<" ";
        temp = temp->next;

    }
}

int main(){

    
    vector<int>arr{9, 4, 5, 6, 7, 8};

    cout<<"convert array into linkedlist:- ";
    Node* head = convertArrIntoLinkedList(arr);
    traverseLinkedList(head);


    Node* temp = head;
    while(temp->next){
        temp = temp->next;
    }

    Node* temp1 = head;
    temp1 = temp1->next->next;

    temp->next = temp1;
    

    cout<<endl;

    cout<<"Length of loop of the linked list:- ";
    cout<<lengthOfLoop(head);



    return 0;
}








