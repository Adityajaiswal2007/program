#include<stdio.h>
int main(){
    float bill,unit;
    printf("enter the unit");
    scanf("%f",&unit);
    if(unit<=100){
        bill=4.2*unit;

    }
    else if(unit<=200){
        bill=4.2*100 + (unit-100)*6;
    }
    else if(unit<=300){
        bill=4.2*100+100*6+(unit-200)*8;
    }
    else
        bill=4.2*100+100*6+200*8+(unit-400)*13;
    printf("Total bill = %f.Rs\n", bill);
}
