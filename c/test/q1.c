#include<stdio.h>
#include<ctype.h>
int main(){

    char ch;
    printf("enter a character");
    scanf("%s",&ch);
    ch=tolower(ch);
    switch (ch)
    {
    case 'a':
    case 'e':
    case 'i':
    case 'o':
    case 'u':
    printf("v");
    break;

    
    default:    //opt can be used  
     printf("c");
    
        break;
    }

}