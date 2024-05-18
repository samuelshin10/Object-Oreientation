#include<stdio.h>
int main(){

    int a1;

    scanf("%d",&a1);

    while(a1>0){
        printf("%d",a1%10);
        a1 = a1/10;
    }



    return 0;
}
