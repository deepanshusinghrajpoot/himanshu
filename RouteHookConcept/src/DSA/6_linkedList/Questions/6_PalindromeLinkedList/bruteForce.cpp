


/*

234. Palindrome Linked List
==============================

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.


Example:

Input Linked List:
1--------->2--------->3--------->2--------->1

Palindrome Check
----------------
Output:
true




Time Complexity (T.C):
O(2N)

Space Complexity (S.C):
O(N)





Explanation (as per code logic):

Step 1: Push all node data into stack (LIFO)
--------------------------------------------
Traversal order: 1 → 2 → 3 → 2 → 1

Stack (top at right):
[1, 2, 3, 2, 1]


Step 2: Traverse again and compare with stack top
-------------------------------------------------
Compare node data with stack.top()










Table (comparison step):

temp(data)   stack.top()   match?
---------------------------------
    1            1          ✓
    2            2          ✓
    3            3          ✓
    2            2          ✓
    1            1          ✓


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



bool isPalindrome(Node* head){
     
   Node* temp = head;
   stack<int>st;

   while(temp){
      st.push(temp->data);
      temp = temp->next;
   }

   temp = head;
   while(temp){
      if(temp->data != st.top()) return false;
      st.pop();
      temp = temp->next;
   }

   return true;
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

    
    vector<int>arr{9, 6, 4, 2, 4, 6, 9};

    cout<<"conver array into linkedlist:- ";
    Node* head = convertArrIntoLinkedList(arr);
    traverseLinkedList(head);

    
    cout<<endl;

    cout<<"Check Linked List is palindrome or not :- ";
    cout<<isPalindrome(head);


    return 0;
}








