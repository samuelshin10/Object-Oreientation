
#include<stdio.h>

int main(){

    int n[11];
    int i=0;
    int sum = 0;
    int count =0;

    for(i=0; i<10; i++){
        scanf("%d",&n[i]);
    }
    for(i = 0; i<10; i++){
        if(n[i]>0){
            count +=1;
            sum = sum + n[i];
        }
    }
    printf("%d %d",sum,count);

    return 0;
}
