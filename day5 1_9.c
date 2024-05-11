

#include<stdio.h>

int main(){

    int n[7];
    int i=0;
    int sum = 0;
    int f = 1;
    for(i = 0; i<6; i++){
        scanf("%d",&n[i]);
    }

    for(i = 0; i<6; i++){
        if(n[i]> 0){
            sum +=n[i];

        }else if(n[i]<0){
            f *=n[i];
        }


    }
    printf("%d %d",sum,f);

    return 0;
}
