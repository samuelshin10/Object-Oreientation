#include<stdio.h>
#include<string.h>
int main(){

    char s1[1001];
    int count =0;
    scanf("%s",s1);
    int a1 = strlen(s1);
    for(int i = 0; i<a1; i++){
        if(s1[i] == '7'){
            count +=1;
        }
    }
    printf("%d",count);


    return 0;
}
