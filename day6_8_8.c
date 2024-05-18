#include<stdio.h>
#include<string.h>

int main(){

    char s1[101];
    int n = 0;
    scanf("%d",&n);
    int i=0;
    int j = 0;

    for(i=0; i<n; i++){
        scanf("%d",&s1[i]);
    }

    for(j=0; j<n-1; j++){
        printf("%d ",s1[j]+s1[j+1]);
    }


    return 0;

}
