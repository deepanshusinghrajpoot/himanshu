/*


✅ Pascal’s Triangle Definition

Each number is the sum of the two numbers directly above it.




            n!
nCr =  ------------
        r! (n-r)!




              5!             5 * 4
c(5, 2) = ---------- =  --------------
           2! 3!             1 * 2





✅ Code Breakdown
-------------------


int nCr(int n, int r) {
    if (r == 0 || r == n) return 1;  // base case

    int res = 1;
    for (int i = 0; i < r; i++) {
        res = res * (n - i) / (i + 1);
    }
    return res;
}







✅ Output for n = 5


    1 
   1 1 
  1 2 1 
 1 3 3 1 
1 4 6 4 1 




*/



#include<iostream>
using namespace std;


int ncr(int n, int r){

    if(r == 0 || r == n)  return 1;

    int res  = 1;

    for(int i=0; i<r; i++){

        res  = res * (n - i) / (i + 1);

    }

    return res;
}



void pascalsTriangle(int n){

    int space = n-1;
    int stars = 1;

    for(int i=0; i<n; i++){
      
        for(int j=0; j<space; j++){
            cout<<" ";
        }

        for(int k=0; k<stars; k++){
            cout<<ncr(i, k)<<" ";
        }

        cout<<endl;

        space -= 1;
        stars += 1;
    }
}


int main(){

    int n;
    cout<<"Enter a number";
    cin>>n;

    
    pascalsTriangle(n);

    return 0;
}



/*



⏳ Complexity

Time Complexity: O(n²) (double loop, each row up to n)

Space Complexity: O(1) (only variables, no extra storage)




*/


