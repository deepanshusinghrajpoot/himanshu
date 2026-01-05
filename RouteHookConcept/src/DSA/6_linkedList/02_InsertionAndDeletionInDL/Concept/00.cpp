
/*


Ques 1:- How to create self define data type in Doubly LinkedList




*/





#include<bits/stdc++.h>
using namespace std;


class Node{

    public:
       int data;
       Node* prev;
       Node* next;
       

    
    public:
       Node(int data1,Node* prev1, Node* next1){
           data = data1;
           prev = prev1;
           next = next1;
       }


    public:
       Node(int data1){
         data = data1;
         prev = nullptr;
         next = nullptr;
       }
};