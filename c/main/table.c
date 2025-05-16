#include<stdio.h>
int main (){
    int n,a ;
    printf("enter the value of n: ");
    scanf("%d",&n);
    printf("enter the value of a: ");
    scanf("%d",&a);
    printf("the table of %d is:\n",n);
    for(int i=1;i<=a;i++){
        int product = n*i;
        printf("%d\n",product);
    }
    return 0;
}


