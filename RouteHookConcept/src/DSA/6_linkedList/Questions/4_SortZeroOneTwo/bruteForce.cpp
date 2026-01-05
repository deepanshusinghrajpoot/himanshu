

/*


Question : Sort aLinked List 0's, 1's, 2's
=============================================



Example:

Input Linked List:
1--------->0--------->2--------->1--------->0--------->2

Sorted Linked List (0s → 1s → 2s)
--------------------------------
0--------->0--------->1--------->1--------->2--------->2




Time Complexity (T.C):
O(2N)

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

    Node* temp = head;

    int count0 = 0;
    int count1 = 0;
    int count2 = 0;

    while(temp){

        if(temp->data == 0) count0++;
        else if(temp->data == 1) count1++;
        else count2++;

        temp = temp->next;
    }


    temp = head;
    while(temp){
        if(count0){
            temp->data = 0;
            count0--;
        }
        else if(count1){
            temp->data = 1;
            count1--;
        }
        else if(count2){
            temp->data = 2;
            count2--;
        }

        temp = temp->next;
    }


    return head;
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