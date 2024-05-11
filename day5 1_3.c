

#include<stdio.h>
#include<string.h>

int main(){

    int s[] = { 77, 88, 99, 66, 44, 55};
    int cnt =0;


    //배열 s 에서 70점 이하 학생수(cnt) 세기

    for(int i=0; i<6; i++){
        if(s[i] <=70){
            cnt ++;
        }
    }
    printf("%d",cnt);
    return 0;
}
