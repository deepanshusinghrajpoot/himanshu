


/*

234. Palindrome Linked List
==============================

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.


Example:

Input Linked List:
1--------->2--------->3--------->2--------->1   (fast->next == NULL)
 
1--------->2--------->3--------->2           (fast->next->next == NULL)
Palindrome Check
----------------
Output:
true




Time Complexity (T.C):
O(2N)

Space Complexity (S.C):
O(1)



EVEN nodes (4)
----------------

1 → 2 → 3 → 4


start:
slow=1, fast=1

move:
slow=2, fast=3

stop (fast->next->next == NULL)

slow at 2



ODD nodes (5)
-----------------

1 → 2 → 3 → 4 → 5

start:
slow=1, fast=1

move:
slow=2, fast=3

move:
slow=3, fast=5

stop (fast->next == NULL)

slow at 3



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


Node* reverseList(Node* head){

    Node* temp = head;
    Node* prev = NULL;

    while(temp){
        Node* front = temp->next;
        temp->next = prev;
        prev = temp;
        temp = front;
    }

    return prev;
}


bool isPalindrome(Node* head){
   
     Node* slow = head;
     Node* fast = head;

     while(fast->next && fast->next->next){
        slow = slow->next;
        fast = fast->next->next;
     }

     Node* newHead = reverseList(slow->next);
     Node* first = head;
     Node* second = newHead;

     while(second){
        if(first->data != second->data){
            reverseList(newHead);
            return false;
        }
        first = first->next;
        second = second->next;
     }

     reverseList(newHead);
     return true;
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

    
    vector<int>arr{9, 6, 4, 2, 4, 6, 9};

    cout<<"conver array into linkedlist:- ";
    Node* head = convertArrIntoLinkedList(arr);
    traverseLinkedList(head);

    
    cout<<endl;

    cout<<"Check Linked List is palindrome or not :- ";
    cout<<isPalindrome(head);


    return 0;
}








