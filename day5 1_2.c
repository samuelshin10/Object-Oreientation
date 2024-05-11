
#include<stdio.h>
#include<string.h>
int main(){

    char s[1001];
    int cnt = 0;
    int i = 0;
    scanf("%s",s);

    for(i = 0; i<strlen(s); i++)
    {
        if(s[i]=='1'){
            cnt ++;
        }
    }
    printf("%d",cnt);
    return 0;
}
