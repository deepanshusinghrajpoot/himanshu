

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
      Node* back;

    public:
      Node(int data1, Node* next1, Node* back1){
         data = data1;
         next = next1;
         back = back1;
      }

    
    public:
      Node(int data1){
        data = data1;
        next = nullptr;
        back = nullptr;
      }
 };





Node* converArrIntoDoublyLinkedList(vector<int>&arr){

    Node* head = new Node(arr[0]);
    Node* prev = head;

    for(int i=1; i<arr.size(); i++){

        Node* temp = new Node(arr[i]);
        prev->next = temp;
        temp->back = prev;

        prev = temp;
    }

    return head;
}




// Insert Node at the head;

Node* insertNodeAtHead(Node* head, int val){
     
      if(head == NULL) return new Node(val);

      Node* newNode = new Node(val);
      newNode->next = head;
      head->back = newNode;

      return newNode;
}



// Insert the element at the last position

Node* insertNodeAtLast(Node* head, int val){

    if(head == NULL) return new Node(val);

    Node* temp = head;

    while(temp->next){
        temp = temp->next;
    }

    Node* newNode = new Node(val);
    temp->next = newNode;
    newNode->back = temp;

    return head;
}



// Insert node at kth position

Node* insertNodeKthPosition(Node* head, int k, int val){

    if(head == NULL){
        if(k == 1){
            return new Node(val);
        }else{
            return NULL;
        }
    }

    if(k == 1){
        Node* newNode = new Node(val);

        newNode->next = head;
        head->back = newNode;

        return newNode;
    }

    Node* temp = head;
    int count = 0;

    while(temp){

        count++;

        if(count == k){
             Node* prev = temp->back;

             Node* newNode = new Node(val);
    
             newNode->next = temp;
             temp->back = newNode;

             prev->next = newNode;
             newNode->back = prev;

             break;
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
        head->back = newNode;

        return newNode;
     }

     Node* temp = head;

     while(temp){
        
         if(temp->data == val){
            
            Node* prev = temp->back;

            Node* newNode = new Node(ele);

            newNode->next = temp;
            temp->back = newNode;

            prev->next = newNode;
            newNode->back = prev;
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
    Node* head = converArrIntoDoublyLinkedList(arr);
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
    head = insertNodeKthPosition(head, 11, 50);
    traverseLinkedList(head);


    cout<<endl;


    // Insert node befoure the value
    cout<<"Insert element befoure the value :- ";
    head = insertEleBefoureValue(head, 10, 90);
    traverseLinkedList(head);

    return 0;
}

