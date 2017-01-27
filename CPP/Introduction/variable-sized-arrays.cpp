#include <iostream>
using namespace std;

int main() {
    int n,q;
    cin >> n >> q;

    int *a[n];        
    int k;

    for(int i=0;i<n;i++){
        cin >> k;
        a[i] = new int[k];
        for(int j=0;j<k;j++)
            cin >> a[i][j];
    }

    int i,j;
    for(int l=0;l<q;l++){
        cin >> i >> j;
        cout << a[i][j] << endl;
    }
	return 0;
}
