

#include<stdio.h>
#include<string.h>

int main(){

    int s[] = { 77, 88, 99, 66, 44, 55};
    int cnt =0;


    //�迭 s ���� 70�� ���� �л���(cnt) ����

    for(int i=0; i<6; i++){
        if(s[i] <=70){
            cnt ++;
        }
    }
    printf("%d",cnt);
    return 0;
}
