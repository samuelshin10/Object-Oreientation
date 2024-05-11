

#include<stdio.h>

int main(){

    int n;
    int i = 0;
    int arr1[51];
    int arr2[51];
    int arr3[51];

    scanf("%d",&n);

    for(i=0; i<n; i++){
        scanf("%d",&arr1[i]);
    }
    for(i=0; i<n; i++){
        scanf("%d",&arr2[i]);
    }
    for(i=0; i<n; i++){
        arr3[i] = arr1[i] + arr2[i];
    }
    for(i=0; i<n; i++){
        printf("%d",arr3[i]);
    }
    return 0;
}
