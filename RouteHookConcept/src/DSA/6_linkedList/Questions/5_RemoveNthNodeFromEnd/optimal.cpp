

/*


19. Remove Nth Node From End of List
======================================


Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example:

Input Linked List:
1--------->2--------->3--------->4--------->5

n = 2  (remove 2nd node from end)
--------------------------------
Output Linked List:
1--------->2--------->3--------->5






Time Complexity (T.C):
O(2N)

Space Complexity (S.C):
O(1)






Step-by-step pointer movement (as per code):

Step 1: Move fast pointer n steps ahead
---------------------------------------
fast moves 2 steps

fast → 3
slow → 1



Step 2: Move both pointers together
-----------------------------------

fast->next != NULL

Iteration 1:
slow → 2
fast → 4

Iteration 2:
slow → 3
fast → 5

Now fast->next == NULL → stop


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



Node* RemoveNthNodeFromEndList(Node* head, int n){

      Node* fast = head;
      for(int i=1; i<=n; i++) fast = fast->next;

      if(fast == NULL) return head->next;

      Node* slow = head;

      while(fast->next){
        slow = slow->next;
        fast = fast->next;
      }

      Node* deleteNode = slow->next;
      slow->next = slow->next->next;
      delete deleteNode;

      return head;
}






int main(){


    vector<int>arr{2, 3, 4, 5, 1, 0, 6, 2, 5};

    cout<<"Convert Arr Into LinkedList :- ";
    Node* head = convertArrIntoLinkedList(arr);
    traverseLinkedList(head);

    cout<<endl;

    cout<<"Remove Nth Node From End of List :- ";
    head = RemoveNthNodeFromEndList(head, 9);
    traverseLinkedList(head);

    return 0;
}