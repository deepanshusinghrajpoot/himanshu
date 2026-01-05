
/*

Delete of element in linked list
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

    public:
      Node(int data1){
        data = data1;
        next = nullptr;
      }

    public:
      Node(int data1, Node* next1){
          data = data1;
          next = next1;
      }
};

Node* converArrIntoLinkedList(vector<int>&arr){

    Node* head = new Node(arr[0]);
    Node* move = head;

    for(int i=1; i<arr.size(); i++){
        Node* temp = new Node(arr[i]);
        move->next = temp;
        move = temp;
    }

    return head;
}


// Remove head from linked list

Node* removeHead(Node* head){

    if(head == NULL) return head;

    Node* temp = head;

    head = head->next;
    
    delete temp;

    return head;
}



// Remove last node of linked list

Node* removeLastNodeOfLinkedList(Node* head){

    if(head == NULL || head->next == NULL) return NULL;

    Node* temp = head;

    while(temp->next->next){
        temp = temp->next;
    }

    delete temp->next;

    temp->next = nullptr;

    return head;
}




// Remove kth position element

Node* removeKthPositionNode(Node* head, int k){

    if(head == NULL) return head;

    
    // Here we consider one extra base as comparision to deletion in doubly linkedList
    // because initialy prev node at null
    if(k==1){
       Node* temp = head;
       head = head->next;
       delete temp;
       return head;
    }


    Node* temp = head;
    Node* prev = NULL;

    int count = 0;

    while(temp){
       count++;

       if(count == k){

          prev->next = prev->next->next;
          temp->next = nullptr;
          delete temp;

          break;
       }

       prev = temp;

       temp = temp->next;
    }

    return head;
}


// remove k value from the linked list

Node* removeKvalueLinkedList(Node* head, int k){
      
      if(head == NULL) return head;

      // Here we consider one extra base as comparision to deletion in doubly linkedList
      // because initialy prev node at null
      if(head->data == k){
         Node* temp = head;
         head = head->next;
         delete temp;
         return head;
      }
      

      Node* temp = head;
      Node* prev = NULL;

      while(temp){
          
         if(temp->data == k){
            prev->next = prev->next->next;
            temp->next = nullptr;
            delete temp;
            break;
         }

         prev = temp;
         temp = temp->next;
      }

      return head;
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
 
    Node* head = converArrIntoLinkedList(arr);

    cout<<"Travesal of the linkedList :- ";
    traverseLinkedList(head);

    cout<<endl;

    cout<<"Remove Head of the lnked list :- ";
    head = removeHead(head);
    traverseLinkedList(head);

    cout<<endl;

    cout<<"Remove last node of linked list :- ";
    head = removeLastNodeOfLinkedList(head);
    traverseLinkedList(head);


    cout<<endl;

    cout<<"Remove kth position node from the linked list :- ";
    head = removeKthPositionNode(head, 2);
    traverseLinkedList(head);
    

    cout<<endl;

    cout<<"Remove k value node from the linked list :- ";
    head = removeKvalueLinkedList(head, 5);
    traverseLinkedList(head);

    return 0;
}