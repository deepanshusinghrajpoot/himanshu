


/*

 Find middle length of the linked list
 =======================================

 Example (one frame):

Approach Used:
Slow & Fast Pointer Method (Tortoise–Hare)


Base Cases
=========
1) If head == NULL → return NULL
2) If list has only one node → return head (slow and fast both at head)


Input 1 (Odd Length):
--------------------
1 --------> 2 --------> 3 --------> 4 --------> 5  
Condition for stopping: fast->next == NULL  

Middle Node = 3


Input 2 (Even Length):
---------------------
1 --------> 2 --------> 3 --------> 4 --------> 5 --------> 6  
Condition for stopping: fast == NULL  

Middle Node = 4   (second middle)


Time Complexity (T.C):
O(N)


Space Complexity (S.C):
O(1)


Why Base Condition Acts Here
============================
✔ In odd-length list → fast->next == NULL signals end, slow is middle  
✔ In even-length list → fast == NULL signals end, slow is second middle  
✔ Ensures loop stops exactly at middle node  
✔ Avoids null pointer errors  


Final Output:
Odd  → Middle = 3  
Even → Middle = 4



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






Node* findMiddleOfLinkedList(Node* head){
     
    if(head == NULL) return NULL;

    Node* slow = head;
    Node* fast = head;

    while(fast && fast->next){
        slow = slow->next;
        fast = fast->next->next;
    }

    return slow;
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

    
    cout<<endl;

    cout<<"Return the middle node of the linkedList :- ";
    Node* middleNode = findMiddleOfLinkedList(head);
    cout<<middleNode->data;


    return 0;
}








