#include<stdio.h>
int main(){

    int a1,a2;

    scanf("%d",&a1);
    scanf("%d",&a2);

    if(a1!=a2){
        printf("%d",a2-a1);
    }else{
        printf("%d",a1+a2);
    }

    return 0;
}
