
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

    if(a1>=a2){
        for(int i=0; i<a1; i++)
        {
            printf("%c",s1[a1-i-1]);
        }
    }else{
        for(int i=0; i<a2; i++){
            printf("%c",s2[a2-i-1]);
            }
    }


    return 0;
}
