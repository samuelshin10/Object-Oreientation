#include<stdio.h>
#include<string.h>

int main(){

    int n;
    char s1[101];

    scanf("%d",&n);

    for(int i=0; i<n; i++){
        scanf("%d",&s1[i]);
    }

    for(int j =0; j<n-1; j++){
        printf("%d ",s1[j] - s1[j+1]);
        printf("\n");

    }

    return 0;
}
