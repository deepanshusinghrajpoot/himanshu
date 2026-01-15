


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

Input:
1--------->2--------->9

+1
--------------------
Output:
1--------->3--------->0


Time Complexity (T.C):
O(N)

Space Complexity (S.C):
O(N)


Reversed List:
9--------->2--------->1


temp   carry(in)   sum = temp+carry   newNode = sum%10   carry(out)
-------------------------------------------------------------------
  9        1            9+1 = 10             0              1
  2        1            2+1 = 3              3              0
  1        0            1+0 = 1              1              0


Final (reverse again):
1--------->3--------->0


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

    Node* newHead = reverseList(head);

    Node* dummyNode = new Node(-1);
    Node* current = dummyNode;
    
    Node* temp = newHead;
    int carry = 1;

    while(temp){

        int sum = carry;
        
        if(temp) sum += temp->data;

        Node* newNode = new Node(sum%10);
        carry = sum/10;
        
        current->next = newNode;
        current = newNode;

        if(temp) temp = temp->next;
    }

    if(carry){
        Node* newNode = new Node(carry);
        current->next = newNode;
    }

    head = reverseList(dummyNode->next);

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








