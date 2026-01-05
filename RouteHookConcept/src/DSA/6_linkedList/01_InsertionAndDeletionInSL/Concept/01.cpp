


/*



Qus 1:-  How to create a linkedList from a given array
Qus 2:-  How Traversal singly linkedList
Qus 3:-  How to find the length of linked list
Qus 4:-  How to search the element in the linked list 



Note:- Never ever temper the head



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


// How to traverse the linkedList

void travesalLinkedList(Node* head){
    
      Node* temp = head;

      while(temp){
        cout<<temp->data<<" ";

        temp = temp->next;
      }

}





// How to find the length of linked list

int lengthOfLinkedLIst(Node* head){

    Node* temp = head;
    int count = 0;

    while(temp){
      temp = temp->next;
      count++;
    }

    return count;
}


// Search the element in the linked list

bool searchELementInLinkedList(Node* head, int val){
   
     Node* temp = head;
     
     while(temp){
       if(temp->data == val){
          return true; 
       }
       temp = temp->next;
     }

     return false;
}





int main(){

    vector<int>arr{1, 2, 3, 4, 5, 6};
 
    Node* head = converArrIntoLinkedList(arr);
  
    cout<<head->data<<endl;



    cout<<"Traversal of the linked  List :- ";
    travesalLinkedList(head);

    cout<<endl;
    
    cout<<"Length of the linked list :- ";
    cout<<lengthOfLinkedLIst(head);

    cout<<endl;

    cout<<"Check the value is present the linked list or not :- ";
    cout<<searchELementInLinkedList(head, 6);
    

    return 0;
    
}