
//   Variables decleared as static in a function are created 


#include<bits/stdc++.h>
using namespace std;


void func(){
    
    static int x = 0;
    cout<<"x: "<<x<<endl;

    x++;
}


int main(){

    func();
    func();
    func();

    return 0;
}

