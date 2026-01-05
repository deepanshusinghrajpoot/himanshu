
/*

206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.


BRUTE FORCE APPROACH

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

    stack<int>st;

    while(temp){

        st.push(temp->data);
        temp = temp->next;

    }


    temp = head;

    while(temp){
         
        temp->data = st.top();
        st.pop();

        temp = temp->next;
    }


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

    
    vector<int>arr{9, 6, 4, 2, 1, 6, 0};

    cout<<"conver array into linkedlist:- ";
    Node* head = convertArrIntoLinkedList(arr);
    traverseLinkedList(head);

    cout<<"Reverse the linked List:- ";
    head = reverseList(head);
    traverseLinkedList(head);


    return 0;
}





/*

T.C = O(2N)
S.C = O(N) :- It is accquare by stack to store data


*/


