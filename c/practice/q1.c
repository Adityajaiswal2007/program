//Take an integer from the user and print whether it is even or odd.
#include<stdio.h>
int main(){
    int a ;
    printf("enter a number");
    scanf("%i",&a);
    if (a%2==0){
        printf("the number is even");
    }
    else{
        printf("the number is odd");
    }
    return 0;
}
