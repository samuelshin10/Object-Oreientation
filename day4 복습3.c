#include<string.h>
#include<stdio.h>
int main(){

    char s[101];
    int a;

    scanf("%s",s);

    a = strlen(s);

    if(a%2==1){
        for(int i=0; i<a; i++){
            printf("%c",s[a-i-1]);
        }
    }else{
        for(int i=0; i<a; i++){
            if(i%2 == 1){
                printf("%c",s[i]);
            }
        }
    }





    return 0;
}
