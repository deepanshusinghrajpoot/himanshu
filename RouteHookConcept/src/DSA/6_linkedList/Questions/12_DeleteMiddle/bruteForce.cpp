


/*

Delete middle node of the linked list
=========================================

In case odd length linked list has one middle node
In case even length linked list has two middle node =====> delete second middle node





Example (one frame):

Approach Used:
Count Nodes Method (Delete Middle Node)


Base Case
=========
If head == NULL OR head->next == NULL  
→ No middle node possible  
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

Step 1: Count total nodes
------------------------
Traverse list to get count = N


Step 2: Find node just before middle
------------------------------------
beforeMid = count / 2  

This positions `temp` **one node before** the middle.


Step 3: Delete middle node
--------------------------
deleteNode = temp->next  
temp->next = temp->next->next  
delete deleteNode  


Time Complexity (T.C):
O(N)


Space Complexity (S.C):
O(1)


Why This Works
==============
✔ count/2 gives middle position  
✔ For even length → deletes second middle  
✔ Only pointer adjustment, no extra space  
✔ Safe deletion using base case  


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

     Node* temp = head;
     int count = 0;

     while(temp){
        count++;
        temp = temp->next;
     }

     int beforeMid = count/2;

     temp = head;
     while(temp){
        beforeMid--;
        if(beforeMid == 0) break;
        temp = temp->next;
     }

     Node* deleteNode = temp->next;
     temp->next = temp->next->next;
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

    
    vector<int>arr{9, 3, 4, 2, 1};

    cout<<"convert array into linkedlist:- ";
    Node* head = convertArrIntoLinkedList(arr);
    traverseLinkedList(head);


    cout<<endl;

    cout<<"Delete the middle node of the linked list:- ";
    head = deleteMiddleNodeOfLinkedList(head);
    traverseLinkedList(head);


    return 0;
}








