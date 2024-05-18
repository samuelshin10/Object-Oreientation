#include<stdio.h>
#include<string.h>
int main(){

    int n;
    char s1[101];
    int max = 0;
    int sum  = 0;
    int r,i;
    scanf("%d",&n);

    for(i=0; i<n; i++){
        scanf("%d",&s1[i]);
        sum = sum + s1[i];
        if(s1[i]>max){
            max = s1[i];
        }
    }
    sum = sum - max;
    r = sum  / (n -1);
    printf("%d\n",sum);
    printf("%d",r);



    return 0;
}
