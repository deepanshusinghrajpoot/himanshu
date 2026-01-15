


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
9 --------> 8 ------------

Intersection Node = 3


Approach:
Hashing using map<Node*, int>


Time Complexity (T.C):
O(N log N + M log N)


Space Complexity (S.C):
O(N)


Working:
1) Store addresses of all nodes of List A in map
2) Traverse List B
3) First node whose address is found in map is intersection


Why it works:
Intersection means same memory address, not same value


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



// Find Intersection Node using map
Node* IntersectionNode(Node* head1, Node* head2){
    map<Node*, int> mp;

    Node* temp = head1;
    while(temp){
        mp[temp] = 1;
        temp = temp->next;
    }

    temp = head2;
    while(temp){
        if(mp.find(temp) != mp.end())
            return temp;
        temp = temp->next;
    }
    return NULL;
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
