


/*

Delete middle node of the linked list
=========================================

In case odd length linked list has one middle node
In case even length linked list has two middle node =====> delete second middle node




Example (one frame):

Approach Used:
Slow & Fast Pointer Method (Optimal – One Pass)


Base Case
=========
If head == NULL OR head->next == NULL  
→ Middle node does not exist  
→ Return NULL


Input 1 (Odd Length):
--------------------
1 --------> 2 --------> 3 --------> 4 --------> 5

Middle Node = 3  
After Deletion:
1 --------> 2 --------> 4 --------> 5


Input 2 (Even Length):
---------------------
1 --------> 2 --------> 3 --------> 4 --------> 5 --------> 6

Middle Node = 4  (second middle)  
After Deletion:
1 --------> 2 --------> 3 --------> 5 --------> 6


How the Code Works
=================

Initial Setup
-------------
slow = head  
fast = head->next->next  

→ fast starts two steps ahead so that  
   slow stops **one node before the middle**


Traversal Logic
---------------
while (fast != NULL && fast->next != NULL)

• slow moves 1 step  
• fast moves 2 steps  


Deletion Step
-------------
deleteNode = slow->next  
slow->next = slow->next->next  
delete deleteNode  


Why This Works
==============
✔ One traversal only  
✔ slow lands just before middle  
✔ Deletes middle safely  
✔ For even length → deletes second middle  


Time Complexity (T.C):
O(N)


Space Complexity (S.C):
O(1)


Final Output:
Middle node deleted successfully


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





Node* deleteMiddleNodeOfLinkedList(Node*  head){

      if(head == NULL || head->next == NULL) return NULL;

      Node* slow = head;
      Node* fast = head;

      fast = fast->next->next;

      while(fast && fast->next){
          slow = slow->next;
          fast = fast->next->next;
      }

      Node* deleteNode = slow->next;
      slow->next = slow->next->next;
      delete deleteNode;

      return head;
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

    
    vector<int>arr{9, 2};

    cout<<"convert array into linkedlist:- ";
    Node* head = convertArrIntoLinkedList(arr);
    traverseLinkedList(head);


    cout<<endl;

    cout<<"Delete the middle node of the linked list:- ";
    head = deleteMiddleNodeOfLinkedList(head);
    traverseLinkedList(head);


    return 0;
}








