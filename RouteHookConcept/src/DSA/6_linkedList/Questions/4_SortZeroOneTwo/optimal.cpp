

/*




Example:

Input Linked List:
1--------->0--------->2--------->1--------->0--------->2

Sorted Linked List (0s → 1s → 2s)
--------------------------------
0--------->0--------->1--------->1--------->2--------->2




Time Complexity (T.C):
O(N)

Space Complexity (S.C):
O(1)





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








Node* SortZeroOneTwo(Node* head){
  

    Node* zeroHead = new Node(-1);
    Node* oneHead = new Node(-1);
    Node* twoHead = new Node(-1);

    Node* zero = zeroHead;
    Node* one = oneHead;
    Node* two = twoHead;

    Node* temp = head;

    while(temp){
        if(temp->data == 0){
            zero->next = temp;
            zero = temp;
        }
        else if(temp->data == 1){
            one->next = temp;
            one = temp;
        }
        else{
            two->next = temp;
            two = temp;
        }

        temp = temp->next;
    }

    zero->next = oneHead->next ? oneHead->next : twoHead->next;
    one->next = twoHead->next;
    two->next = NULL;


    return zeroHead->next;
 
}









int main(){


    vector<int>arr1{1, 2, 0, 2, 2, 1, 0, 0, 2, 1, 0, 2, 0, 1, 1};

    cout<<"conver array into linkedlist:- ";
    Node* head = converArrIntoLinkedList(arr1);
    traverseLinkedList(head);

    cout<<endl;

    cout<<"Sort linked list which contain only 0, 1, 2 :- ";
    head = SortZeroOneTwo(head);
    traverseLinkedList(head); 

    return 0;
}