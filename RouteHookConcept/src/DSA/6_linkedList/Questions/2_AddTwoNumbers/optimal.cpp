

/*


2. Add Two Numbers


You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:

   2--------->4--------->3

   +

   5--------->6--------->4

-------------------------------
 
   7---------->0--------->8






Time Complexity (T.C):
O(max(N, M))

Space Complexity (S.C):
O(max(N, M))

temp1  temp2  carry(in)   sum = t1+t2+carry   newNode = sum%10   carry(out)=sum/10
---------------------------------------------------------------------------------
  2      5        0            2+5+0 = 7            7                 0
  4      6        0            4+6+0 = 10           0                 1
  3      4        1            3+4+1 = 8            8                 0




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




Node* addTwoLinkedList(Node* head1, Node* head2){

    Node* dummyNode = new Node(-1);
    Node* current = dummyNode;

    Node* temp1 = head1;
    Node* temp2 = head2;

    int carry = 0;

    while(temp1 || temp2){

        int sum = carry;

        if(temp1) sum += temp1->data;
        if(temp2) sum += temp2->data;

        Node* newNode = new Node(sum%10);

        carry = sum/10;

        current->next = newNode;
        current = newNode;


        if(temp1)  temp1 = temp1->next;
        if(temp2)  temp2 = temp2->next;
    }


    if(carry){
        Node* newNode = new Node(carry);
        current->next = newNode;
        current = newNode;
    }


    return dummyNode->next;
}













int main(){

   
    vector<int>arr1{9, 6, 4, 2, 1, 6, 0};

    cout<<"conver array1 into linkedlist:- ";
    Node* head1 = converArrIntoLinkedList(arr1);
    traverseLinkedList(head1);


    cout<<endl;

    vector<int>arr2{3, 4, 5, 6, 2};

    cout<<"convert array2 into linkedlist:- ";
    Node* head2 = converArrIntoLinkedList(arr2);
    traverseLinkedList(head2);

    cout<<endl;

    cout<<"Add to linkedlist as arithmatic stander from left to right:- ";
    Node* head3 = addTwoLinkedList(head1, head2);
    traverseLinkedList(head3);

    return 0;
}