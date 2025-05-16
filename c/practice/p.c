#include<stdio.h>
int main(){
    int n;
    printf("enter a number");
    scanf("%d",&n);
    for(int i=1;n>=i;i++){
        for(int j =1;n-i>=j;j++){
            printf(" ");
        }
        for(int k=1;k<=i;k++){
            printf("*");

        }
        printf("\n");
    }
return 0;    
}
