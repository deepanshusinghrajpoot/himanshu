

/*


Insertion of element in linked list
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
      Node(int data1, Node* next1){
         data = data1;
         next = next1;
      }

    public:
      Node(int data1){
         data = data1;
         next = nullptr;
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


// Insert Node at the head;

Node* insertNodeAtHead(Node* head, int val){

    return new Node(val, head);
}



// Insert the element at the last position

Node* insertNodeAtLast(Node* head, int val){

    if(head == NULL) return new Node(val);

    Node* temp = head;

    while(temp->next){
        temp = temp->next;
    }

    Node* ele = new Node(val);
    temp->next = ele;
    temp = ele;

    return head;
}



// Insert node at kth position

Node* insertNodeKthPosition(Node* head, int k, int val){

    if(head == NULL){
        if(k==1){
            return new Node(val);
        }
        else return NULL;
    }


    if(k==1){
        Node* temp = new Node(val);
        temp->next = head;
        return temp;
    }


    Node* temp = head;
    int count = 0;

    while(temp){

        count++;

        if(count == k-1){
            Node* ele = new Node(val);
            ele->next = temp->next;
            temp->next = ele;
        }

        temp = temp->next;
    }

    return head;
}


// Insert Element Befoure the value

Node* insertEleBefoureValue(Node* head, int val, int ele){

    if(head == NULL) return NULL;

    if(head->data == val){
        Node* newNode = new Node(ele);
        newNode->next = head;
        return newNode;
    }

    Node* temp = head;

    while(temp->next){

        if(temp->next->data == val){
            Node* newNode = new Node(ele);
            newNode->next = temp->next;
            temp->next = newNode;
            break;
        }

        temp = temp->next;
    }

    return head;
}


// Traverse the linkedlist

void traverseLinkedList(Node* head){

     Node* temp = head;

     while(temp){
        cout<<temp->data<<" ";
        temp = temp->next;
     }
}



int main(){


    vector<int>arr{1, 2, 3, 4, 5, 6, 7, 8, 9};

    // Convert arr into linkedlist
    cout<<"Convert arr into linkedlist :- ";
    Node* head = converArrIntoLinkedList(arr);
    traverseLinkedList(head);

    cout<<endl;

    // Insert node at head
    cout<<"Insert node at head :- ";
    head = insertNodeAtHead(head, 10);
    traverseLinkedList(head);


    cout<<endl;


    // Insert node at last
    cout<<"Insert node at last position :- ";
    head = insertNodeAtLast(head, 80);
    traverseLinkedList(head);


    cout<<endl;


    // Insert node at kth position
    cout<<"Insert node at kth position :- ";
    head = insertNodeKthPosition(head, 3, 50);
    traverseLinkedList(head);


    cout<<endl;


    // Insert node befoure the value
    cout<<"Insert element befoure the value :- ";
    head = insertEleBefoureValue(head, 8, 90);
    traverseLinkedList(head);

    return 0;
}