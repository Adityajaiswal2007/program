#include<stdio.h>
int main(){
    int age;
    age=22;
    int*ptr=&age;
    int **pptr=&ptr;

    printf("%u",*ptr);
    printf("%u",**pptr);
return 0;
}
