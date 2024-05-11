

#include<stdio.h>

int main(){

    int n;
    int num[51];
    int i = 0;

    scanf("%d",&n);

    for(i = 0; i<n; i++){
        scanf("%d",&num[i]);
    }

    for(i = 1; i<n; i++){
        printf("%d\n",num[i] - num[i-1]);
    }

    return 0;
}
