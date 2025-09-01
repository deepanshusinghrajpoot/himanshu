
/*

✅ Approach 2: Recursive (Not preferred in interview unless asked)

Each number is calculated from the sum of the previous two.

*/



#include <iostream>
using namespace std;

int fibonacci(int n) {
    if (n <= 1) return n;  
    return fibonacci(n-1) + fibonacci(n-2);
}

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cout << fibonacci(i) << " ";
    }
    return 0;
}




int main(){

    int n;
    cout<<"Print Nth term of fibbonacci series ";
    cin>>n;

    for(int i=0; i<n; i++){
        cout<<fibonacci(i)<<" ";
    }


    return 0;
}



/*

⏱ Time Complexity:

O(2^N) → exponential (very slow)

💾 Space Complexity:

O(N) → recursion stack

🔥 Interview Tip:

👉 Always write iterative approach first (O(N), O(1)),
and if interviewer asks, explain recursion and its drawback.

*/