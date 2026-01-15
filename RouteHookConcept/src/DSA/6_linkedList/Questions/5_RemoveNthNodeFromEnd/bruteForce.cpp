

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







Explanation (as per code logic):

Step 1: Count total nodes
--------------------------------
Linked List: 1 → 2 → 3 → 4 → 5
count = 5


Step 2: Find position from start
--------------------------------
res = count - n
res = 5 - 2 = 3

→ We need to stop at the 3rd node (just before the node to delete)


Step 3: Traverse again and delete
--------------------------------
temp moves until res becomes 0


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

    Node* temp = head;
    int count = 0;

    while(temp){
        count++;
        temp = temp->next;
    }

    if(count == n){
        Node* deleteNode = head;
        head = head->next;
        deleteNode->next = NULL;
        delete deleteNode;
        return head;
    }

    int res = count - n;
    temp = head;

    while(temp){

        res--;

        if(res == 0) break;

        temp = temp->next;
    }

    Node* deleteNode = temp->next;
    temp->next = temp->next->next;
    deleteNode->next = NULL;
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
    head = RemoveNthNodeFromEndList(head, 2);
    traverseLinkedList(head);

    return 0;
}