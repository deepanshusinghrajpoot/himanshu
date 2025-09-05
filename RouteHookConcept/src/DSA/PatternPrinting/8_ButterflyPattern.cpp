/*



⚡ Output for n = 5



*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *



*/





#include<iostream>
using namespace std;


int butterFly(int n){

     // upper part

     int stars = 1;
     int spaces = 2*n-2;

     for(int i=1; i<=n; i++){
        
        for(int j=1; j<=stars; j++){
            cout<<"*";
        }

        for(int k=1; k<=spaces; k++){
            cout<<" ";
        }

        for(int j=1; j<=stars; j++){
            cout<<"*";
        }


        cout<<endl;

        stars += 1;
        spaces -= 2;
     }



     // lower part 

     stars = n-1;
     spaces = 2;

     for(int i=1; i<=n-1; i++){
        
        for(int j=1; j<=stars; j++){
            cout<<"*";
        }

        for(int k=1; k<=spaces; k++){
            cout<<" ";
        }

         for(int j=1; j<=stars; j++){
            cout<<"*";
        }
        
        cout<<endl;


        stars -= 1;
        spaces += 2;
     }
}




int main(){

    int n;
    cout<<"Enter a number : ";
    cin>> n;

    butterFly(n);

    return 0;
}



/*

T.C = O(n^2)
S.C = O(1)


*/