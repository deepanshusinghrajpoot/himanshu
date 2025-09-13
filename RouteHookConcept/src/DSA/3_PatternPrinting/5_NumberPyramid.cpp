/*


✅ Number Pyramid Pattern

For n = 5:

    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5






*/





#include<iostream>
using namespace std;


void numberPyramid(int n){
    
    int spaces = n-1;
    int num = 1;

    for(int i=1; i<=n; i++){

        int count = 1;
        for(int j=1; j<=spaces; j++){
           cout<<" ";
        }

        for(int k=1; k<=num; k++){
            cout<<count<<" ";
            count++;
        }

        cout<<endl;

        spaces -= 1;
        num +=1;

    }

}


int main(){

    int n;
    cout<<"Enter a number : ";
    cin>>n;

    numberPyramid(n);

    return 0;
}