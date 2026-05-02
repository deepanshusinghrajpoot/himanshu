
/*







| Test Case | Input            | Output |
| --------- | ---------------- | ------ |
| 1         | `2 3 -2 4`       | `6`    |
| 2         | `-2 0 -1`        | `0`    |
| 3         | `-2 3 -4`        | `24`   |
| 4         | `0 0 0`          | `0`    |
| 5         | `-1 -3 -10 0 60` | `60`   |
| 6         | `-2 -3 0 -2 -40` | `80`   |
| 7         | `1`              | `1`    |
| 8         | `-1`             | `-1`   |




*/





#include<bits/stdc++.h>
using namespace std;


int max_product_sub_array(vector<int>&arr){

    int maxProduct = INT_MIN;

    int prefixProduct = 1;
    int suffixProduct = 1;

    for(int i=0; i<arr.size(); i++){

        if(prefixProduct == 0) prefixProduct = 1;
        if(suffixProduct == 0) suffixProduct = 1;

        prefixProduct *= arr[i];
        suffixProduct *= arr[arr.size()-i-1];

        maxProduct = max(maxProduct, max(prefixProduct, suffixProduct));
    }

    return maxProduct;
}


int main(){

    vector<vector<int>> testCases = {
        {2, 3, -2, 4},
        {-2, 0, -1},
        {-2, 3, -4},
        {0, 0, 0},
        {-1, -3, -10, 0, 60},
        {-2, -3, 0, -2, -40},
        {1},
        {-1}
    };

    for(int i = 0; i < testCases.size(); i++){
        cout << "Test Case " << i + 1 << ": ";
        for(int x : testCases[i]) cout << x << " ";
        cout << "\nMax Product = "
             << max_product_sub_array(testCases[i]) << "\n\n";
    }

    return 0;
}