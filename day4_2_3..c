

#include<stdio.h>
int main(){

    char s[101];
    int a1;

    scanf("%s",s);

    a1 = strlen(s);

    for(int i=0; i<a1; i++){
        if(i% 2 == 1){
            printf("%c",s[i]);
        }
    }








    return 0;
}
