//Take 3 integers from the user and print the largest one.
#include<stdio.h>
int main(){
    int a,b,c;
    printf("enter 3 numbers ");
    scanf("%i",&a);

    scanf("%i",&b);

    scanf("%i",&c);
    if(a>=b && a>=c ){
        printf("%i is grater",a);
    }
    else if (b>=a && b>=c){
        printf("%i is grater",b);
    }
    else{
        printf("%i is grater",c);
    }
    return 0;



}