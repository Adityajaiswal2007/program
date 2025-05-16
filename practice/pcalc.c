#include<stdio.h>
int main() {
    int a , b , choice;
    printf("WELCOME TO ADITYA CALC");
    printf("WHAT YOU WANT TO DO ");
    printf("FOR\n 1 ADDITION\n 2 SUBRATCT\n 3 divide\n 4 PRODUCT\n");
    scanf("%d", &choice );

    printf("enter a number");
    scanf("%d", &a);

    printf("enter a number");
    scanf("%d", &b);

    if (choice ==1 ){
    int sum= a+b;
        printf("sum is : %d\n", sum);
    } else if (choice==2){
        int diff = a-b;
        printf("diff is : %d\n", diff);
    } else if(choice==3){
        int qu = a/b;
        printf("qu is : %d\n", qu);
    } else if (choice==4){
        int product = a * b ;
        printf("product is : %d\n", product);
    }
    return 0;

}