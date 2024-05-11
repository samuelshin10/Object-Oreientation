

#include<stdio.h>
#include<string.h>

int main(){

    int s;
    scanf("%d",&s);

    while(s>0){
        printf("%d",s%10);
        s = s/10;
    }


    return 0;
}
