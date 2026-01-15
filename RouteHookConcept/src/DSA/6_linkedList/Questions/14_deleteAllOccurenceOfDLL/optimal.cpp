

/*

Delete all occurrences of a key in a Doubly Linked List (DLL)
===============================================================


Example (one frame):

Approach Used:
Delete all occurrences of a key in a Doubly Linked List (DLL)


Base Case
=========
If head == NULL  
→ List is empty  
→ Return NULL


Input:
------
DLL:
NULL <- 1 <-> 2 <-> 3 <-> 2 <-> 4 -> NULL

Key = 2


Output:
-------
NULL <- 1 <-> 3 <-> 4 -> NULL


How the Code Works
=================

Traversal Logic
---------------
• temp starts from head  
• Traverse until temp == NULL  


Case 1: Current node data == key
--------------------------------

1️⃣ If deleting HEAD node  
   • Move head to next node  
   • New head’s prev becomes NULL  

2️⃣ Store neighbors  
   prevNode = temp->prev  
   nextNode = temp->next  

3️⃣ Re-link nodes  
   • prevNode->next = nextNode  
   • nextNode->prev = prevNode  

4️⃣ Delete current node  
   delete temp  

5️⃣ Move temp forward  
   temp = nextNode  


Case 2: Current node data != key
--------------------------------
• Simply move ahead  
  temp = temp->next  


Why This Works
==============
✔ Handles deleting head node  
✔ Handles deleting middle node  
✔ Handles deleting tail node  
✔ Deletes **all occurrences**, not just one  
✔ Safe pointer movement after deletion  


Edge Case Handling
==================
• Multiple consecutive keys → handled  
• Key at start → handled  
• Key at end → handled  
• Key not present → list unchanged  


Time Complexity (T.C):
O(N)


Space Complexity (S.C):
O(1)


Final Takeaway
==============
Always:
• Save prev & next before deletion  
• Re-link neighbors correctly  
• Move temp to nextNode after delete  

This ensures safe deletion in DLL
without breaking links.







*/




#include<bits/stdc++.h>
using namespace std;



class Node{

    public:
       int data;
       Node* next;
       Node* prev;

    public:
       Node(int data1, Node* next1, Node* prev1){
           data = data1;
           next = next1;
           prev = prev1;
       }

       Node(int data1){
         data = data1;
         next = nullptr;
         prev = nullptr;
       }
      
};





Node* deleteOccurenceOfKeyFromDLL(Node* head, int key){

    Node* temp = head;

    while(temp){

        if(temp->data == key){

            if(temp == head){
                head = head->next;
            }

            Node* prevNode = temp->prev;
            Node* nextNode = temp->next;

            if(prevNode)  prevNode->next = nextNode;
            if(nextNode)  nextNode->prev = prevNode;

            delete temp;
            temp = nextNode;
        }
        else{
            temp = temp->next;
        }
    }

    return head;
}











Node* converArrInToDLL(vector<int>&arr){

    Node* head = new Node(arr[0]);
    Node* move = head;

    for(int i=1; i<arr.size(); i++){

        Node* newNode = new Node(arr[i]);
        
        move->next = newNode;
        newNode->prev = move;

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



    vector<int>arr{2, 4, 1, 5, 8, 9, 1, 0};


    cout<<"Create a DLL from a array :- ";
    Node* head = converArrInToDLL(arr);
    traverseLinkedList(head);

    cout<<endl;

    cout<<"Delete the occurence of especific key:- ";
    head = deleteOccurenceOfKeyFromDLL(head, 1);
    traverseLinkedList(head);

    return 0;
}