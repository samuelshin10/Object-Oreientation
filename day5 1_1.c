
#include<string.h>
#include<stdio.h>
int main(){

    char s[20] = "abcdedcbacc";
    int cnt = 0;

    for(int i = 0; i<strlen(s); i++){
        if(s[i] == 'c') cnt++;
    }

    printf("%d\0",cnt);

    return 0;
}
