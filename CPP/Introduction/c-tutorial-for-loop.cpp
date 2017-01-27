#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int a, b;
    string n[] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    string p[] = {"even", "odd"};
    
    cin >> a >> b;
    
    for(int i=a; i <= b; i++){
        if(i <= 9){
            cout << n[i-1] << endl; 
        }
        else{
            cout << p[i%2] << endl;
        }
    }
    
    return 0;
}
