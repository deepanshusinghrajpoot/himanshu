


/*


  Detect the first Node of the loop
=========================================



Example (one frame):

Approach Used:
Hashing (map) – Detect First Node of Loop


Base Case
=========
If head == NULL  
→ No loop possible  
→ Return NULL


Input (Loop Present):
--------------------
1 --------> 2 --------> 3 --------> 4 --------> 5
              ^                    |
              |--------------------|


First Node of Loop = 3


How the Code Works
=================

Data Structure Used
------------------
map<Node*, int> mp  
→ Stores visited node addresses


Traversal Logic
---------------
temp = head

while (temp != NULL):
• If temp already exists in map  
  → This is the **first node of loop**
• Else mark temp as visited  
• Move to next node


Step-by-Step (Conceptual)
------------------------
Visit 1 → store in map  
Visit 2 → store in map  
Visit 3 → store in map  
Visit 4 → store in map  
Visit 5 → store in map  
Visit 3 again → already present  

→ Loop entry detected at node 3


Why This Works
==============
✔ Loop causes node repetition  
✔ First repeated node = loop entry  
✔ Uses node address (not data)  
✔ Simple and intuitive  


Time Complexity (T.C):
O(N)


Space Complexity (S.C):
O(N)


Final Output:
Loop Present → First Node = 3  
No Loop      → NULL




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




Node* detectFirstNodeOfLoop(Node* head){

     map<Node*, int>mp;

     Node* temp = head;

     while(temp){
        if(mp.find(temp) != mp.end()) return temp;
        mp[temp] = 1;
        temp = temp->next;
     }

     return NULL;
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

    
    vector<int>arr{9, 3, 4, 2, 1, 2, 4, 5, 7, 1, 0};

    cout<<"convert array into linkedlist:- ";
    Node* head = convertArrIntoLinkedList(arr);
    traverseLinkedList(head);


    Node* temp1 = head;
    while(temp1->next){
        temp1 = temp1->next;
    }

    Node* temp2 = head->next->next;
    temp1->next = temp2;
    

    cout<<endl;
    
    cout<<"Detect the first node of the loop:- ";
    Node* node = detectFirstNodeOfLoop(head);
    cout<<node->data;

    return 0;
}








