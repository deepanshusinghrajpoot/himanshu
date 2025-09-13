/*



4. Diamond
----------


Example (n = 5)


    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *




*/







#include<iostream>
using namespace std;



void diamond(int n){

    // upper part

    int spaces = n-1;
    int stars = 1;

    for(int i=1; i<=n; i++){

        for(int j=1; j<=spaces; j++){
            cout<<" ";
        }

        for(int k=1; k<=stars; k++){
            cout<<"*";
        }

        cout<<endl;

        spaces -=1;
        stars +=2;
    }



    // lower part


    spaces = 1;
    stars = 2*n - 3;

    for(int i=1; i<=n-1; i++){

        for(int j=1; j<=spaces; j++){
            cout<<" ";
        }

        for(int k=1; k<=stars; k++){
            cout<<"*";
        }

        cout<<endl;

        spaces += 1;
        stars -= 2;
    }
}


int main(){
    
    int n;
    cout<<"Enter a number";
    cin>>n;

    diamond(n);


    return 0;
}