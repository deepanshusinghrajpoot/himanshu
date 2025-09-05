
/*

✅ Floyd’s Triangle Definition
-------------------------------

It is a right-angled triangular array of natural numbers.
Numbers are filled row-wise starting from 1.

For n = 5, the output looks like:

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15



*/







#include<iostream>
using namespace std;



int floydTriangle(int n){

    int num = 1;
    int count = 1;
    for(int i=1; i<=n; i++){
        
        for(int j=1; j<=num; j++){
            cout<<count<<" ";
            count++;
        }

        cout<<endl;

        num +=1;
    }
}


int main(){

    int n;
    cout<<"Enter a number : ";
    cin>>n;


    floydTriangle(n);

    return 0;
}


/*

⏳ Complexity

Time Complexity: O(n²) → two nested loops.

Space Complexity: O(1) → just counter variable.



*/