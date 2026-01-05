
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
O(N)


Table (data rewriting step):

temp(data before)   arr[i]   temp(data after)
----------------------------------------------
       1               1            1
       2               3            3
       3               5            5
       4               2            2
       5               4            4
       6               6            6




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

    vector<int>arr;

    Node* temp = head;

    while(temp && temp->next){
        arr.push_back(temp->data);
        temp = temp->next->next;
    }
    if(temp) arr.push_back(temp->data);


    temp = head->next;
    while(temp && temp->next){
        arr.push_back(temp->data);
        temp = temp->next->next;
    }
    if(temp) arr.push_back(temp->data);


    
    temp = head;
    int i=0;
    while(temp){
        temp->data = arr[i];
        i++;
        temp = temp->next;
    }

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