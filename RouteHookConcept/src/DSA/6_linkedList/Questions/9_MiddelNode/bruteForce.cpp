


/*

 Find middle length of the linked list
 =======================================

 Example (one frame):

Approach Used:
Count Nodes Method


Input 1 (Odd Length):
--------------------
1 --------> 2 --------> 3 --------> 4 --------> 5

Middle Node = 3


Input 2 (Even Length):
---------------------
1 --------> 2 --------> 3 --------> 4 --------> 5 --------> 6

Middle Node = 4   (second middle)


Base Case
=========
If head == NULL → return NULL


Time Complexity (T.C):
O(N)

Space Complexity (S.C):
O(1)


Step-by-Step Explanation
=======================

Input 1 (Odd Length)
-------------------
Total nodes = 5  
d = 5/2 + 1 = 3  

Traversal:
1 → 2 → 3  ← STOP  


Input 2 (Even Length)
--------------------
Total nodes = 6  
d = 6/2 + 1 = 4  

Traversal:
1 → 2 → 3 → 4  ← STOP  


Why This Works
==============
✔ Formula (N/2 + 1)  
✔ Odd length → exact middle  
✔ Even length → second middle  
✔ Constant extra space  


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

     Node* temp = head;
     int count = 0;
     while(temp){
         count++;
         temp = temp->next;
     }

     int d = count/2 + 1;

     temp = head;
     while(temp){
        d--;
        if(d == 0) break;
        temp = temp->next;
     }

     return temp;
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








