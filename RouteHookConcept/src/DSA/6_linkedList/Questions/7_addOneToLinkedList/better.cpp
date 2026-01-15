


/*

 Add one to a number represented as Linked List
 ===============================================


Problem statement
You're given a positive integer represented in the form of a singly linked-list of digits. 
The length of the number is 'n'.

Add 1 to the number, i.e., increment the given number by one.

The digits are stored such that the most significant digit is at the head of the linked list and the 
least significant digit is at the tail of the linked list.



Example:
Input: Initial Linked List: 1 -> 5 -> 2
Output: Modified Linked List: 1 -> 5 -> 3
Explanation: Initially the number is 152. After incrementing it by 1, the number becomes 153.



Example (one frame):

Input Linked List:
9 --------> 9 --------> 9

+1
--------------------
Output Linked List:
1 --------> 0 --------> 0 --------> 0


Time Complexity (T.C):
O(3N)

Space Complexity (S.C):
O(1)


Step 1: Reverse the linked list
-------------------------------
Original:
9 --------> 9 --------> 9

Reversed:
9 --------> 9 --------> 9


Step 2: Add 1 using carry (in-place)
------------------------------------

temp   carry(in)   temp->data(before)   temp->data(after)   carry(out)
-----------------------------------------------------------------------
  9        1              9                     0               1
  9        1              9                     0               1
  9        1              9                     0               1


Step 3: Handle remaining carry
------------------------------
Create new node [1] and prepend:
1 --------> 0 --------> 0 --------> 0


Step 4: Reverse again (already handled in prepend)
--------------------------------------------------
Final Output:
1 --------> 0 --------> 0 --------> 0


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




Node* addOneToLinkedList(Node* head){
   
    head = reverseList(head);
    Node* temp = head;
    int carry = 1;

    while(temp){

        temp->data = temp->data + carry;

        if(temp->data < 10){
            carry = 0;
            break;
        }
        else{
            temp->data = 0;
            carry = 1;
        }

        temp = temp->next;
    }


    if(carry == 1){
        Node* newNode = new Node(carry);
        head =  reverseList(head);
        newNode->next = head;
        return newNode;
    }


    head = reverseList(head);
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

    
    vector<int>arr{9};

    cout<<"convert array into linkedlist:- ";
    Node* head = convertArrIntoLinkedList(arr);
    traverseLinkedList(head);

    
    cout<<endl;

    cout<<"Add 1 in the linkedlist:- ";
    head = addOneToLinkedList(head);
    traverseLinkedList(head);


    return 0;
}








