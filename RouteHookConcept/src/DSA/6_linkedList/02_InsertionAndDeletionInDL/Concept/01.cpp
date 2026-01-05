


/*



Qus 1:-  How to create a Doubly linkedList from a given array
Qus 2:-  How Traversal Doubly linkedList
Qus 3:-  How to find the length of Doubly linked list
Qus 4:-  How to search the element in the Doubly linked list 



Note:- Never ever temper the head



*/


#include<bits/stdc++.h>
using namespace std;


class Node{

    public:
      int data;
      Node* next;
      Node* prev;


    public:
      Node(int data1, Node* next1, Node* prev1){
         data = data1;
         next = next1;
         prev = prev1;
      }


    public:
       Node(int data1){
         data = data1;
         next = nullptr;
         prev = nullptr;
       }
};




//Qus 1:-  How to create a Doubly linkedList from a given array


Node* converArrDoublyIntoLinkedList(vector<int>&arr){
         
      Node* head = new Node(arr[0], nullptr, nullptr);
      Node* move = head;

      for(int i=1; i<arr.size(); i++){
         
          Node* temp = new Node(arr[i]);
          temp->prev = move;
          move->next = temp;

          move = temp;
      }


      return head;
}




// Qus 2:-  How Traversal Doubly linkedList

 
void travesalDoublyLinkedList(Node* head){

    Node* temp = head;

    while(temp){
        cout<<temp->data<<" ";
        temp = temp->next;
    }
}






// How to find the length of linked list

int lengthOfDoublyLinkedLIst(Node* head){

    Node* temp = head;
    int count = 0;

    while(temp){
        count++;
        temp = temp->next;
    }

    return count;
}


// Search the element in the linked list

bool searchELementInDoublyLinkedList(Node* head, int val){

    Node* temp = head;

    while(temp){

        if(temp->data == val) return true;

        temp = temp->next;
    }

    return false;
}





int main(){

    vector<int>arr{1, 2, 3, 4, 5, 6};
 
    Node* head = converArrDoublyIntoLinkedList(arr);
  
    cout<<head->data<<endl;



    cout<<"Traversal of the Doubly linked  List :- ";
    travesalDoublyLinkedList(head);

    cout<<endl;
    
    cout<<"Length of the Doubly linked list :- ";
    cout<<lengthOfDoublyLinkedLIst(head);

    cout<<endl;

    cout<<"Check the value is present in the Doubly linked list or not :- ";
    cout<<searchELementInDoublyLinkedList(head, 6);
    

    return 0;
    
}