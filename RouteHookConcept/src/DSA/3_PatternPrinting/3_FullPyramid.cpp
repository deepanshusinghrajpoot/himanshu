/*

3. Full pyramid
----------------



🔹 Example for n = 5


    *    
   ***   
  *****  
 ******* 
*********



*/




#include<iostream>
using namespace std;



void fullPyramid(int n){

    int col = n-1;

    int col1 = 1;
    for(int i=1; i<=n; i++){

        for(int j=1; j<=col; j++){
            cout<<" ";
        }
        col -=1;


        for(int k=1; k<=col1; k++){
           cout<<"*";
        }
        col1 +=2;

        cout<<endl;

    }
}


int main(){

    int n;
    cout<<"Enter a number : ";
    cin>>n;

    fullPyramid(n);


    return 0;
}