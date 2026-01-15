


/*

141. Length of Linked List Cycle
=======================

Example (one frame):

Approach Used:
Floyd’s Cycle Detection + Loop Length Calculation (Optimal)


Base Case
=========
If head == NULL OR head->next == NULL  
→ Loop not possible  
→ Return 0


Input (Loop Present):
--------------------
1 --------> 2 --------> 3 --------> 4 --------> 5
              ^                    |
              |--------------------|


How the Code Works
=================

Step 1: Detect the loop (Fast–Slow Pointer)
-------------------------------------------
• slow moves 1 step  
• fast moves 2 steps  
• Loop condition used:
  while (fast != NULL && fast->next != NULL)

• If slow == fast → loop exists  


Step 2: Calculate loop length
-----------------------------
• Keep slow fixed at meeting point  
• Move fast one step at a time  
• Count nodes until fast meets slow again  


Visual Loop Traversal:
----------------------
Meeting at node 3  

3 → 4 → 5 → 3  

Loop Length = 3


Why `findLength()` Works
=======================
✔ Meeting point is guaranteed inside loop  
✔ One complete traversal gives exact loop length  
✔ Stops exactly when fast meets slow again  


Important Concept (Fast & Fast->next condition)
===============================================

Why we use:
while (fast != NULL && fast->next != NULL)


Odd Length Linked List
---------------------
1 --------> 2 --------> 3 --------> 4 --------> 5

• fast reaches last node  
• fast != NULL  
• fast->next == NULL  

Stopping Condition:
fast->next == NULL  
(loop breaks safely)


Even Length Linked List
----------------------
1 --------> 2 --------> 3 --------> 4 --------> 5 --------> 6

• fast jumps two steps and becomes NULL  
• fast == NULL  

Stopping Condition:
fast == NULL  
(loop breaks safely)


Why Both Conditions Are Needed
==============================
✔ `fast != NULL` handles **even-length** lists  
✔ `fast->next != NULL` handles **odd-length** lists  
✔ Prevents accessing next of NULL  
✔ Works correctly for:
  - Cycle detection  
  - Loop length  
  - Middle of linked list  


Time Complexity (T.C):
O(N)


Space Complexity (S.C):
O(1)


Final Output:
Loop Present → Length = 3  
No Loop      → Length = 0


Final Takeaway
==============
Always use:
while (fast != NULL && fast->next != NULL)

Because:
Odd length  → stop at last node  
Even length → stop at NULL


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



int findLength(Node* slow, Node* fast){

    int count = 1;
    fast = fast->next;

    while(fast != slow){
        count++;
        fast = fast->next;
    }

    return count;
}


int lengthOfLoop(Node* head){

    Node* slow = head;
    Node* fast = head;

    while(fast && fast->next){
         slow = slow->next;
         fast = fast->next->next;

         if(slow == fast)  return findLength(slow, fast);
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








