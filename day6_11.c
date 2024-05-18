#include<stdio.h>
#include<string.h>

int main(){

    int n;
    char s1[101];
    int sum = 0;
    scanf("%d",&n);
    for(int i=0; i<n; i++){
        scanf("%d",&s1[i]);
        sum = s1[i]+ sum;


    }
    printf("%d",sum);
    int r = sum / n;
    printf("\n");
    printf("%d",r);



    return 0;
}
