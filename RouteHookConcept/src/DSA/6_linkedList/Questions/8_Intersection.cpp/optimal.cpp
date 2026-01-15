


/*

160. Intersection of Two Linked Lists
=======================================

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.
For example, the following two linked lists begin to intersect at node c1:


Example (one frame):

Input Linked Lists:

List A:
1 --------> 2 --------> 3 --------> 4 --------> 5
↑
|
List B:
1 --------> 2 --------> 3 --------> 4 --------> 5

Intersection Node = 1


Approach Used:
Two Pointer Switching Method (Optimal)


Base Cases
==========

1) If either list is empty
--------------------------
head1 == NULL OR head2 == NULL  
→ No intersection possible  
→ Return NULL

2) If both lists start at the same node
---------------------------------------
head1 == head2  
→ Intersection exists at head itself  
→ Return head1 immediately


Time Complexity (T.C):
O(N + M)


Space Complexity (S.C):
O(1)


Step-by-Step Visual Explanation
===============================

Idea:
Both pointers traverse A + B length.
Switching equalizes path length.


Initial:
temp1 → headA  
temp2 → headB  

Case 1: Same starting node
--------------------------
temp1 == temp2 at start  
→ Loop not entered  
→ Return head directly


General Case Traversal:
-----------------------
temp1 = temp1->next  
temp2 = temp2->next  

If any pointer reaches NULL:
→ redirect to other list’s head


Why This Works
==============
✔ Handles same-head intersection  
✔ Handles different-length lists  
✔ No extra memory used  
✔ Guaranteed meeting point if intersection exists  


Final Output:
Intersection Node = 1


*/


#include<bits/stdc++.h>
using namespace std;

class Node{
public:
    int data;
    Node* next;

    Node(int data1){
        data = data1;
        next = nullptr;
    }
};

// Reverse Linked List
Node* reverseList(Node* head){
    Node* temp = head;
    Node* prev = NULL;

    while(temp){
        Node* front = temp->next;
        temp->next = prev;
        prev = temp;
        temp = front;
    }
    return prev;
}

// Find Intersection Node using map
Node* IntersectionNode(Node* head1, Node* head2){

    if(head1 == NULL || head2 == NULL) return NULL;

    Node* temp1 = head1;
    Node* temp2 = head2;

    while(temp1 != temp2){
       
        temp1 = temp1->next;
        temp2 = temp2->next;

        if(temp1 == temp2) return temp1;

        if(temp1 == NULL) temp1 = head2;
        if(temp2 == NULL) temp2 = head1;

    }


    return temp1;
}

// Convert array to linked list
Node* convertArrIntoLinkedList(vector<int>& arr){
    Node* head = new Node(arr[0]);
    Node* move = head;

    for(int i = 1; i < arr.size(); i++){
        move->next = new Node(arr[i]);
        move = move->next;
    }
    return head;
}

// Traverse linked list
void traverseLinkedList(Node* head){
    while(head){
        cout << head->data << " ";
        head = head->next;
    }
}

int main(){

    // List A: 1->2->3->4->5
    vector<int> arr1 = {1,2,3,4,5};
    Node* headA = convertArrIntoLinkedList(arr1);

    // List B: 9->8
    vector<int> arr2 = {9,8};
    Node* headB = convertArrIntoLinkedList(arr2);

    // Create intersection at node with value 3
    Node* tempA = headA;
    while(tempA->data != 3){
        tempA = tempA->next;
    }

    Node* tempB = headB;
    while(tempB->next){
        tempB = tempB->next;
    }
    tempB->next = tempA;   // intersection created

    cout << "List A: ";
    traverseLinkedList(headA);
    cout << endl;

    cout << "List B: ";
    traverseLinkedList(headB);
    cout << endl;

    Node* intersection = IntersectionNode(headA, headB);

    if(intersection)
        cout << "Intersection Node: " << intersection->data << endl;
    else
        cout << "No Intersection Found" << endl;

    return 0;
}
