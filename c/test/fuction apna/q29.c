#include<stdio.h>
#include<ctype.h>
void indian();
void french();
int main() {
	char n;
	printf("enter:- \ni for indian\nf for french\n");
    scanf("%c",&n);
    n=tolower(n);
    if(n=='i'){
        indian();
    }
    else if (n=='f'){
        french();
    }
    else
        printf("invalid input ");
	return 0;
}
void indian(){
    printf("Namaste");
}
void french(){
    printf("Bonjour");
}