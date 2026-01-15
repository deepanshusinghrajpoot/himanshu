


/*

  Detect the first Node of the loop
=========================================




Example (one frame):

Approach Used:
Floyd’s Cycle Detection + Mathematical Reset (Optimal)


Base Case
=========
If head == NULL OR head->next == NULL  
→ Loop not possible  
→ Return NULL


Input (Loop Present):
--------------------
1 --------> 2 --------> 3 --------> 4 --------> 5
              ^                    |
              |--------------------|


First Node of Loop = 3


How the Code Works
=================

Step 1: Detect the loop (Slow–Fast)
----------------------------------
• slow moves 1 step  
• fast moves 2 steps  

Condition used:
while (fast != NULL && fast->next != NULL)

✔ Handles even-length traversal  
✔ Handles odd-length traversal  
✔ Prevents NULL access  

When:
slow == fast  
→ Loop confirmed  
→ Both pointers meet **inside the loop** (not necessarily at entry)


Step 2: Find first node of loop
-------------------------------
• Move slow back to head  
• Keep fast at meeting point  
• Move both one step at a time  

while (slow != fast):
    slow = slow->next  
    fast = fast->next  

When they meet again  
→ That node is the **first node of the loop**


Why `findNode()` Works
=====================
✔ Distance from head to loop entry  
✔ Equals distance from meeting point to loop entry  
✔ Proven Floyd’s cycle mathematics  


Visual Movement
---------------
Meeting point: node 4 (example)

Reset:
slow = head (1)  
fast = meeting point (4)

1 → 2 → 3  
4 → 5 → 3  

They meet at node 3  
→ Loop entry found


Odd vs Even Length Safety
=========================
Odd length traversal:
• fast reaches last node  
• fast != NULL  
• fast->next == NULL  

Even length traversal:
• fast jumps to NULL  
• fast == NULL  

Hence always use:
while (fast != NULL && fast->next != NULL)


Time Complexity (T.C):
O(N)


Space Complexity (S.C):
O(1)


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



Node* findNode(Node* slow, Node* fast, Node* head){

    slow = head;

    while(slow != fast){
        slow = slow->next;
        fast = fast->next;
    }

    return slow;
}



Node* detectFirstNodeOfLoop(Node* head){
     
    Node* slow = head;
    Node* fast = head;

    while(fast && fast->next){
        slow = slow->next;
        fast = fast->next->next;

        if(slow == fast) return findNode(slow, fast, head);
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








