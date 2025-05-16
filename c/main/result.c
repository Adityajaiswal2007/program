// Calculate and display the student’s grade based on their percentage
// using predefined grading criteria.
// by asking them how many subject they have and then ask to enter the marks and sum it 

// Below 35%: Grade F
// Below 45%: Grade E
// Below 60%: Grade D
// Below 75%: Grade C
// Below 90%: Grade B
// Above 90%: Grade A
#include<stdio.h>
int main (){
    int a,b,i,sum=0;
    int l=1;
    printf("welcome to the grading system\n");
    printf("made by ADITYA JAISWAL\n");
    printf("This program will calculate your percentage and grade\n");
    
    while (l==1)
    {
        printf("enter how many subject you have:");
        scanf("%i",&a);
        for(i=1;i<=a;i++){
            printf("enter the marks of %i subject:",i);
            scanf("%i",&b);
            sum +=b;    
        }

        float percentage = (float)sum/(a*100)*100;

        
        printf("your percentage is %f\n",percentage);
        if(percentage<35){
            printf("Grade F\n");
            printf("you are fail\n");

        }
        else if(percentage<45){
            printf("Grade E\n");
            printf("you are pass but need improvement\n");

        }
        else if(percentage<60){
            printf("Grade D\n");
            printf("pass\n");

        }
        else if(percentage<75){
            printf("Grade C\n");
            printf("good\n");
        }
        else if(percentage<90){
            printf("Grade B\n");
            printf("very good\n");
        }
        else{
            printf("Grade A\n");
            printf("excellent\n");
        }
    printf("do you want to continue? 1 for yes and 0 for no:");
    scanf("%i",&l);
    if(l==0){
        printf("thank you for using this program\n");
    }
    else if(l!=1){
        printf("invalid input\n");
    }
    
    }
return 0;
}