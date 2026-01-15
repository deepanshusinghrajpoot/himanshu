


/*

   141. Linked List Cycle
 =======================================
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by 
continuously following the next pointer. Internally, pos is used to denote the
index of the node that tail's next pointer is connected to. Note that pos is
not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.



 Example (one frame):

Approach Used:
Hashing using map<Node*, int>


Base Case
=========
If head == NULL  
→ No cycle possible  
→ Return false


Input 1 (Cycle Present):
-----------------------
1 --------> 2 --------> 3 --------> 4
              ^                  |
              |------------------|

Cycle Detected = true


Input 2 (No Cycle):
------------------
1 --------> 2 --------> 3 --------> 4 --------> NULL

Cycle Detected = false


Time Complexity (T.C):
O(N log N)
(map insertion + lookup)


Space Complexity (S.C):
O(N)
(extra map storage)


Why This Works
==============
✔ Each node address is stored in map  
✔ Visiting a node again means cycle  
✔ Detects cycle at first repeated node  
✔ Uses memory to avoid infinite traversal  


Final Output:
Cycle Present → true  
Cycle Absent  → false


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





bool checkCycleInList(Node* head){
      
    
     map<Node*, int>mp;

     Node* temp = head;
     
     while(temp){
        if(mp.find(temp) != mp.end()) return true;

        mp[temp] = 1;
        temp = temp->next;
     }
   
     return false;
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

    
    vector<int>arr{9, 4, 5, 6, 7, 8};

    cout<<"convert array into linkedlist:- ";
    Node* head = convertArrIntoLinkedList(arr);
    traverseLinkedList(head);


    Node* temp = head;
    while(temp->next){
        temp = temp->next;
    }

    Node* temp1 = head;
    temp1 = temp1->next->next;

    temp->next = temp1;
    

    cout<<endl;

    cout<<"Detect loop in the linkedList:- ";
    cout<<checkCycleInList(head);



    return 0;
}








