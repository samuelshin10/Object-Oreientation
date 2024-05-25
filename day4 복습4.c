
#include<stdio.h>
#include<string.h>

int main(){

    char s1[101];
    char s2[101];

    int a1,a2;

    scanf("%s",s1);
    scanf("%s",s2);

    a1 = strlen(s1);
    a2 = strlen(s2);

    if(a1<=a2){
        printf("%s%s",s1,s2);
    }else{
        printf("%s%s",s2,s1);
    }







    return 0;
}
