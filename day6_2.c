#include<stdio.h>
#include<string.h>

int main(){

    char s1[101];
    char s2[101];

    scanf("%s",s1);
    scanf("%s",s2);

    int a1 = strlen(s1);
    int a2 = strlen(s2);

    if(a1>a2){
        printf("%s",s1);
    }else{
        printf("%s",s2);
    }


    return 0;
}
