/*



=========== INSERTION SORT (ONE-FRAME EXPLANATION) ===========

Definition:
Insertion Sort places each element
into its correct position in the sorted part of the array.

-----------------------------------------------------------
Core Idea:
-----------------------------------------------------------
• Left part is assumed sorted
• Pick one element from unsorted part
• Shift larger elements to the right
• Insert element at correct position

-----------------------------------------------------------
Example:
-----------------------------------------------------------
Initial Array:
[5, 3, 4, 1, 2]

-----------------------------------------------------------
Step-by-Step:
-----------------------------------------------------------
i = 0 → [5 | 3, 4, 1, 2]
i = 1 → [3, 5 | 4, 1, 2]
i = 2 → [3, 4, 5 | 1, 2]
i = 3 → [1, 3, 4, 5 | 2]
i = 4 → [1, 2, 3, 4, 5]

-----------------------------------------------------------
Final Output:
-----------------------------------------------------------
[1, 2, 3, 4, 5]

-----------------------------------------------------------
Why This Works:
-----------------------------------------------------------
Each element is inserted into its correct position
in the already sorted left portion.

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------
Best Case  : O(N)
Worst Case : O(N²)

-----------------------------------------------------------
Why O(N²)?
-----------------------------------------------------------
• Outer loop runs N times
• Inner loop can run up to N times
• Nested loops → N × N

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------
O(1) (In-place sorting)

-----------------------------------------------------------
Stability:
-----------------------------------------------------------
Stable Sort

-----------------------------------------------------------
One-Line Interview Answer:
-----------------------------------------------------------
"Insertion sort builds the sorted array by inserting
each element into its correct position."

===========================================================



*/


#include<iostream>
#include<bits/stdc++.h>
using namespace std;


void insertionSort(int arr[], int n){
    
    for(int i=0; i<=n-1; i++){
        int j = i;
        while(j>0){
            if(arr[j-1] > arr[j]){
                int temp = arr[j - 1];
                arr[j-1] = arr[j];
                arr[j] = temp;
            }
            j--;
        }
    }
 
}


int main(){
    int n;
    cout<<"Enter a the size of arr : ";
    cin>>n;
    int arr[n];

    cout<<"Enter the all elements of arr : ";
    for(int i=0; i<n; i++){
        cin>>arr[i];
    }

    insertionSort(arr, n);


    for(int i=0; i<n; i++){
        cout<<arr[i]<<" ";
    }

    return 0;
}


/*


T.C = O(n^2)
S.C = O(1)



*/