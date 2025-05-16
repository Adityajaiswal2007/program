#include<stdio.h>
int main(){
    int l=1;
    while(l==1){
        printf("FOR\n 1 ADDITION\n 2 SUBTRACT\n 3 divide\n 4 PRODUCT\n");
        int c;
        scanf("%d",&c);
        float a,b;
        if(c== 1){
        
            printf("enter a number a:");
            scanf("%f",&a);
            printf("enter a number b :");
            scanf("%f",&b);
            float sum = a+b;
            printf("ADDITION is %f\n",sum);
        }
        else if(c==2){
            printf("enter a number a:");
            scanf("%f",&a);
            printf("enter a number b :");
            scanf("%f",&b);
            float sub = a-b;
            printf("%f\n",sub);

        }
        else if (c==3){
            printf("enter a number a:");
            scanf("%f",&a);
            printf("enter a number b :");
            scanf("%f",&b);
            float div = a/b;
            printf("a/b= %f\n",div);
        }
        else if (c==4){
            printf("enter a number a:");
            scanf("%f",&a);
            printf("enter a number b :");
            scanf("%f",&b);
            float pro=a*b;
            printf("product is = %f\n",pro);
            
        }
        else{
            printf("please enter a valid number\n");
        }
        printf("do you want do run it again\nyes=1 \nno=2\n");
        scanf("%d",&l);
        if(l==1){
            printf("here is you calculator\n");

        }
        else if(l==2){
            printf("thank you\n ");
        }
        else{
            printf("invilid input try again\n");
            l==1;
        }


    
    }
    return 0 ;

}