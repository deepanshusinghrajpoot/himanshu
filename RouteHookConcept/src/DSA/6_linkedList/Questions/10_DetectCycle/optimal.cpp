


/*

141. Linked List Cycle
=======================
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by 
continuously following the next pointer. Internally, pos is used to denote the
index of the node that tail's next pointer is connected to. Note that pos is
not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.



Example (one frame):

Approach Used:
Floyd’s Cycle Detection (Slow & Fast Pointer)


Base Case / Loop Condition
=========================
while (fast != NULL && fast->next != NULL)

• fast != NULL      → required for even-length traversal  
• fast->next != NULL → required for odd-length traversal  
• Prevents null pointer access


Input 1 (Odd Length – 5 nodes):
-------------------------------
1 --------> 2 --------> 3 --------> 4 --------> 5

Stopping Condition:
fast->next == NULL  
(loop breaks safely)

Result:
No cycle detected


Input 2 (Even Length – 6 nodes):
--------------------------------
1 --------> 2 --------> 3 --------> 4 --------> 5 --------> 6

Stopping Condition:
fast == NULL  
(loop breaks safely)

Result:
No cycle detected


Time Complexity (T.C):
O(N)


Space Complexity (S.C):
O(1)


Why Both Conditions Are Needed
==============================
✔ fast->next != NULL handles **odd length** lists  
✔ fast != NULL handles **even length** lists  
✔ Together they prevent segmentation fault  
✔ Ensures correct termination in all cases  


Final Output:
Odd Length  → No Cycle  
Even Length → No Cycle


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





bool checkCycleInList(Node* head){

     Node* slow = head;
     Node* fast = head;

     while(fast && fast->next){   
        slow = slow->next;
        fast = fast->next->next;
        if(slow == fast)  return true;
     }

     return false;
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

    cout<<"Detect loop in the linkedList:- ";
    cout<<checkCycleInList(head);



    return 0;
}








