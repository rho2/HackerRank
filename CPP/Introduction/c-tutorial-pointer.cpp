#include <stdio.h>

void update(int *a,int *b) {
    int ta = (*a);
    int tb = (*b);
    
    (*a) = ta + tb;
    (*b) = ( (ta>tb) ? (ta-tb) : (tb-ta) );
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
