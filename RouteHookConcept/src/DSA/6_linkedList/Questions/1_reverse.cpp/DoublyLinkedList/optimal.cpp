
/*

206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.


OPTIMAL OPPROACH

*/



#include<bits/stdc++.h>
using namespace std;


class Node{

    public:
       int data;
       Node* prev;
       Node* next;


    public:
       Node(int data1, Node* prev1, Node* next1){
          data = data1;
          next = next1;
       }


       Node(int data1){
         data = data1;
         prev = nullptr;
         next = nullptr;
       }
};



Node* reverseList(Node* head){


    /*
    
          -------- It is based on swap two number (a, b) ----------

          int temp = a
          a = b
          b = temp
    
    
    */

    if(head == NULL || head->next == NULL) return head;


    Node* current = head;
    Node* lastNode = NULL;

    while(current){
        
        lastNode = current->prev;
        current->prev =  current->next;
        current->next = lastNode;


        current = current->prev;
    }

    return lastNode->prev;
}




Node* convertArrIntoLinkedList(vector<int>&arr){

    Node* head = new Node(arr[0]);

    Node* move = head;

    for(int i=1; i<arr.size(); i++){

        Node* newNode = new Node(arr[i]);
        
        newNode->prev = move;
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

    
    vector<int>arr{9, 6, 4, 2, 1, 6, 0};

    cout<<"conver array into linkedlist:- ";
    Node* head = convertArrIntoLinkedList(arr);
    traverseLinkedList(head);

    cout<<endl;

    cout<<"Reverse the linked List:- ";
    head = reverseList(head);
    traverseLinkedList(head);


    return 0;
}





/*

T.C = O(N)
S.C = O(1) :- It is accquare by stack to store data


*/


