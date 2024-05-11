
#include<stdio.h>
#include<string.h>

int main(){

    int n;
    int arr[51];

    scanf("%d",&n);

    for(int i =0; i<n; i++){
        scanf("%d",&arr[i]);
    }
    for(int i = 0; i<n - 1; i++){
        printf("%d\n",arr[i] - arr[i+1]);
    }




    return 0;
}
