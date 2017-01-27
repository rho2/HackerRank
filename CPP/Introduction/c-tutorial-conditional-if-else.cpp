#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;


int main(){
    int n;
    cin >> n;
    
    string a[] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "Greater than 9"};
    
    if(n < 10){
        cout << a[n-1];
    }
    else{
        cout << a[9];
    }
    
    return 0;
}
