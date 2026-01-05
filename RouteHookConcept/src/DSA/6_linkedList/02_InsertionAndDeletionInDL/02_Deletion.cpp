
/*

Delete of element in Doubly linked list
-------------------------------

1.  Head
2.  Position
3.  value
4.  last 








*/





#include<bits/stdc++.h>
using namespace std;


class Node{

    public:
      int data;
      Node* next;
      Node* back;

    public:
      Node(int data1){
        data = data1;
        next = nullptr;
        back = nullptr;
      }

    public:
      Node(int data1, Node* next1, Node* back1){
          data = data1;
          next = next1;
          back = back1;
      }
};



Node* converArrIntoDoublyLinkedList(vector<int>&arr){

    Node* head = new Node(arr[0]);
    Node* prev = head;

    for(int i=1; i<arr.size(); i++){

        Node* temp = new Node(arr[i], nullptr, prev);
        prev->next = temp;

        prev = temp;
    }

    return head;
}


// Remove head from Doubly linked list

Node* removeHeadOfDoublyLinkedList(Node* head){

     if(head == NULL) return NULL;

     Node* prev = head;
     head = head->next;

     head->back = nullptr;
     prev->next = nullptr;

     delete prev;

     return head;
}



// Remove last node of linked list

Node* removeLastNodeOfDoublyLinkedList(Node* head){

    if(head == NULL ||  head->next == NULL){
         head = NULL;
         return NULL;
    }

    Node* tail = head;
    while(tail->next){
        tail = tail->next;
    }

    Node* prev = tail->back;

    tail->back = nullptr;
    prev->next = nullptr;

    delete tail;

    return head;
}




// Remove kth position element

Node* removeKthPositionNodeInDoublyLinkedList(Node* head, int k){

     
      Node* temp = head;
      int count =0;

      while(temp){
        count++;
        if(count == k)  break;
        temp = temp->next;
      }

      Node* prev = temp->back;
      Node* front = temp->next;

      if(prev == NULL && front == NULL){
           return NULL;
      }
      else if(prev == NULL){
           return removeHeadOfDoublyLinkedList(head);
      }
      else if(front == NULL){
           return removeLastNodeOfDoublyLinkedList(head);
      }

      prev->next = front;
      front->back = prev;

      temp->next = nullptr;
      temp->back = nullptr;

      delete temp;

      return head;

}


// remove Node from the Doubly linked list accept head;

void removeNodeDoublyLinkedList(Node* temp){
      
      Node* prev = temp->back;
      Node* front = temp->next;

      if(front == NULL){
         prev->next = nullptr;
         temp->back = nullptr;
         delete temp;

         return;
      }

      prev->next = front;
      front->back = prev;

      temp->next = temp->back = nullptr;

      delete temp;
}




// Traverse the linked list

void traverseLinkedList(Node* head){
   
   Node* temp = head;

   while(temp){
     cout<<temp->data<<" ";
     temp = temp->next;
   }

}





int main(){

    
    vector<int>arr{1, 2, 3, 4, 5, 6};
 
    Node* head = converArrIntoDoublyLinkedList(arr);
    
    cout<<"Traversal of the linkedList ";
    traverseLinkedList(head);
    
    cout<<endl;
    
    cout<<"Remove Head of the Doubly lnked list :- ";
    head = removeHeadOfDoublyLinkedList(head);
    traverseLinkedList(head);

    cout<<endl;

    cout<<"Remove last node of the Doubly linked list :- ";
    head = removeLastNodeOfDoublyLinkedList(head);
    traverseLinkedList(head);


    cout<<endl;

    cout<<"Remove kth position node from the Doubly linked list :- ";
    head = removeKthPositionNodeInDoublyLinkedList(head, 2);
    traverseLinkedList(head);
    

    cout<<endl;

    cout<<"Remove node from the Doubly linked list :- ";
    removeNodeDoublyLinkedList(head->next->next);
    traverseLinkedList(head);

    return 0;
}