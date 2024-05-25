#include<stdio.h>
#include<string.h>

int main(){

    char s[100];
    int c;

    scanf("%s",s);
    c = strlen(s);

    for(int i=0; i<c; i++){
        for(int j= 0; j<=i; j++){
            printf("%c",s[i]);
        }
        printf("\n");
    }






    return 0;
}
