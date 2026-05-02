
/*




=========== MOVE ALL ZEROS TO END (TWO POINTER – IN-PLACE) ===========

Problem:
-----------------------------------------------------------
Move all 0s to the END of the array
while maintaining the RELATIVE ORDER
of non-zero elements.

-----------------------------------------------------------
Approach Used:
-----------------------------------------------------------

• Two pointers (left & right)
• In-place swapping
• Stable order preserved

-----------------------------------------------------------
Pointers Meaning:
-----------------------------------------------------------

left  → points to FIRST zero position  
right → scans elements after left

-----------------------------------------------------------
Core Idea:
-----------------------------------------------------------

• First, find the FIRST zero → mark it as left
• Then move right pointer ahead
• Whenever a NON-ZERO is found:
  → swap with arr[left]
  → move left forward

-----------------------------------------------------------
Algorithm Steps:
-----------------------------------------------------------

1️⃣ Traverse array to find first zero  
   → set left = index of first zero  
   → if no zero found, return

2️⃣ Set right = left + 1

3️⃣ While right < n:
   • If arr[right] != 0
     → swap(arr[left], arr[right])
     → left++
   • right++

-----------------------------------------------------------
Dry Run Example:
-----------------------------------------------------------

I





*/


#include<bits/stdc++.h>
using namespace std;


void move_all_zero_to_end(vector<int>&arr){

    int left = -1;
    int right = 0;

    while(right < arr.size()){

        if(arr[right] == 0){
            left = right;
            break;
        }
        right++;
    }

    if(left == -1) return;

    
    right = left + 1;
    while(right < arr.size()){
        
        if(arr[right] != 0){
            swap(arr[left], arr[right]);
            left++;
        }
        right++;
    }
}


int main(){

    vector<int>arr{2, 0, 4, 0, 4, 0, 2, 5, 6, 0, 0, 0, 1, 9};
    cout<<"Move all zero to the end :- ";
    move_all_zero_to_end(arr);
    for(int i=0; i<arr.size(); i++){
        cout<<arr[i]<<" ";
    }

    return 0;
}