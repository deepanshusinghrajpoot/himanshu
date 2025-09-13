
/*

2. Inverted triangle
--------------------

🔹 Your Code Output (if n = 5)


*****
****
***
**
*




*/


#include<iostream>
using namespace std;



void invertedTringle(int n){
    int col = n;
    for(int i=1; i<=n; i++){
        for(int j=1; j<=col; j++){
            cout<<"*";
        }
        col -=1;
        cout<<endl;
    }
}


int main(){

    int n;
    cout<<"Enter a number : ";
    cin>>n;

    invertedTringle(n);


    return 0;
}