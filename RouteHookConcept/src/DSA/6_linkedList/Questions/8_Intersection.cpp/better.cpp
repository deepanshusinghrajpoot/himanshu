


/*

160. Intersection of Two Linked Lists
=======================================

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.
For example, the following two linked lists begin to intersect at node c1:


Example (one frame):

Example (one frame):

Input Linked Lists:

List A:
1 --------> 2 --------> 3 --------> 4 --------> 5
                         ↑
                         |
List B:
9 --------> 8 ------------

Intersection Node = 3


Approach Used:
Length Difference Method (No extra space)


Time Complexity (T.C):
O(N + M)

Space Complexity (S.C):
O(1)


Step-by-Step Explanation
=======================

Step 1: Find lengths of both lists
----------------------------------
List A length = n1  
List B length = n2  

Example:
n1 = 5  
n2 = 4  


Step 2: Move pointer of longer list by |n1 − n2|
------------------------------------------------
Difference = |5 − 4| = 1  

Advance pointer of longer list by 1 node so that
both pointers have **equal nodes left**.

After shifting:
temp1 → 2 → 3 → 4 → 5  
temp2 → 9 → 8 → 3 → 4 → 5  


Step 3: Move both pointers together
-----------------------------------
Move temp1 and temp2 one step at a time:

temp1 = 2 , temp2 = 9  ❌  
temp1 = 3 , temp2 = 8  ❌  
temp1 = 3 , temp2 = 3  ✅ FOUND  


Step 4: Return intersection node
--------------------------------
First node where:
temp1 == temp2 (same memory address)

Returned Node:
3 --------> 4 --------> 5


Why This Works
==============
✔ Intersection means same **node address**, not value  
✔ Aligning both lists makes remaining length equal  
✔ First match while moving together is intersection  


Final Output:
Intersection Node = 3



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



    Node* findIntersection(Node* shortList, Node* longList, int d) {

        // move longer list ahead by d nodes
        while(d--) {
            longList = longList->next;
        }

        // move both pointers together
        while(shortList && longList) {
            if(shortList == longList)
                return shortList;

            shortList = shortList->next;
            longList = longList->next;
        }

        return NULL;
    }

    Node* getIntersectionNode(Node *headA, Node *headB) {

        int lenA = 0, lenB = 0;
        Node* tempA = headA;
        Node* tempB = headB;

        while(tempA) { lenA++; tempA = tempA->next; }
        while(tempB) { lenB++; tempB = tempB->next; }

        if(lenA > lenB)
            return findIntersection(headB, headA, lenA - lenB);
        else
            return findIntersection(headA, headB, lenB - lenA);
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

    Node* intersection = getIntersectionNode(headA, headB);

    if(intersection)
        cout << "Intersection Node: " << intersection->data << endl;
    else
        cout << "No Intersection Found" << endl;

    return 0;
}
