/*

  Compile Time Polymorphism
  -------------------------

  (2):- Function Overloading

  When two or more functions in the same class (or scope) have the same name but different number or type of parameters, 
  it is called function overloading.
  
  lll When a class has more than one function with same name but different number or type of parameters, 
  it is called function overloading.
  

*/


#include<bits/stdc++.h>
#include<iostream>
using namespace std;



class Print{

    public:
       
       void show(int x){
        cout<<"int: "<< x <<endl; 
       }

       void show(char ch){
        cout<<"int: "<< ch <<endl;
       }
};


int main(){

    Print p1;
    
    p1.show(5);

    p1.show('&');

    return 0;
}