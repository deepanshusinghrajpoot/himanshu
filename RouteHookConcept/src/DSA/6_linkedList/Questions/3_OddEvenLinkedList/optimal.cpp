
/*

328. Odd Even Linked List
==========================

Given the head of a singly linked list, group all the nodes with odd indices together
followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 


Example:

Input Linked List:
1--------->2--------->3--------->4--------->5--------->6




Odd positions first, then Even positions
----------------------------------------
Output Linked List:
1--------->3--------->5--------->2--------->4--------->6


Time Complexity (T.C):
O(N)

Space Complexity (S.C):
O(1)


Table (pointers update step):

odd(data before)   even(data before)   Action
---------------------------------------------------------
1                  2                 odd->next = 3, even->next = 4
3                  4                 odd->next = 5, even->next = 6
5                  6                 odd->next = evenHead (2), even->next = NULL

Final Linking:
odd->next = 2
even->next = NULL



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


Node* converArrIntoLinkedList(vector<int>&arr){

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




Node* oddEvenLinkedList(Node* head){

    if(head ==  NULL || head->next == NULL) return head;

    Node* odd = head;
    Node* even = head->next;
    Node* evenHead = head->next;

    while(even  &&  even->next){
        odd->next = odd->next->next;
        odd = odd->next;

        even->next = even->next->next;
        even = even->next;
    }

    odd->next = evenHead;

    return head;
}











int main(){

   
    vector<int>arr{9, 6, 4, 2, 1, 6, 0};

    cout<<"conver array into linkedlist:- ";
    Node* head = converArrIntoLinkedList(arr);
    traverseLinkedList(head);


    cout<<endl;

    cout<<"Sort linked list first odd index then even:- ";
    head = oddEvenLinkedList(head);
    traverseLinkedList(head);

    return 0;
}