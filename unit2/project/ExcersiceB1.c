#include<stdio.h>

void main(){
char nick[20];
int x;

printf("Enter your nickname: \n"); scanf("%s",&nick);
printf("Enter your age: \n"); scanf("%d",&x);

if(x < 18){
    printf("Warning this page is just for +18\n");
}
else{
    printf("Welcome to your Profile\n");
}
}