/*


(1). Static keyword use with variables


Variables decleared as static in a function are created 
& initialised once for the lifetime of the program.


Static variable in a class are created & initialised once.
They are shared by all the object of the class.




*/


//   Variables decleared as static in a function are created 
//   & initialised once for the lifetime of the program.


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

