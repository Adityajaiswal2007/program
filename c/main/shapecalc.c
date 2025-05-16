
#include<stdio.h>
int main (){
    int a,c,loop=1;
    while(loop==1){
        loop=0;
        printf("\033[0;36m\n"); // Cyan
        printf("*MADE BY ADITYA JAISWAL*\n");
        printf("This program will help you to find perimeter and area of shapes\n");
        printf("\033[0;33m");// Yellow text
        printf("Select the shape you want to find area or perimeter:\n");
        printf("\n1 SQUARE\n2 RECTANGLE\n3 TRIANGLE\n4 CIRCLE\n");
        printf("Enter your choice (1-4):");
        printf("\033[0m"); // Reset color

        scanf("%i",&c);

        if(c==1){
            printf("\033[0;34m"); // Blue
            printf("what do you want to find\n");  // SQUARE
            printf("1 AREA\n2 PERIMETER\n");
            printf("select:");
            printf("\033[0m"); // Reset color
            scanf("%i",&a);
            int side;
            if(a==1){ 

                printf("enter the side of square:");
                scanf("%i",&side);
                int area= side*side;
                printf("\033[0;32m\n"); // Green
                printf("The area of square is =%i",area);
                printf("\033[0m"); // Reset color
            }
            else if (a==2){
                printf("enter the side of square:");
                scanf("%i",&side);
                int perimeter= 4*side;
                printf("\033[0;32m\n"); // Green
                printf("The perimeter of square is :%i",perimeter);
                printf("\033[0m"); // Reset color

            }
            else{
                printf("\033[0;31m");//red
                printf("invalid input try again");
            }  
        }      
        else if(c==2){
            printf("\033[0;34m"); // Blue
            printf("select what you want to do find :\n");        //RECTANGLE
            printf("\n1 AREA\n2 PERIMETER\n");
            printf("select:");
            printf("\033[0m"); // Reset color
            scanf("%i",&a);
            int l,b;
            if (a==1){
                printf("enter the length of rectangle :");
                scanf("%i",&l);
                printf("enter the breath of rectangle :");
                scanf("%i",&b);
                int area = l*b;
                printf("\033[0;32m\n"); // Green
                printf("The area of rectangle is :%i",area);
                printf("\033[0m"); // Reset color
            }
            else if (a==2){
                printf("enter the length of rectangle :");
                scanf("%i",&l);
                printf("enter the breath of rectangle :");
                scanf("%i",&b);
                int perimeter = 2*(l + b);
                printf("\033[0;32m\n"); // Green
                printf("The perimeter of rectangle is :%i",perimeter);
                printf("\033[0m"); // Reset color

            }
            else{
                printf("\033[0;31m");//red
                printf("invalid input try again");
            }
        }

        else if(c==3){
            printf("\033[0;34m"); // Blue
            printf("select what you want to do find:\n ");        // TRIANGLE
            printf("\n1 AREA\n2 PERIMETER\n");
            printf("select:");
            printf("\033[0m"); // Reset color
            scanf("%i",&a);
            int l,b;
            if(a==1){
                printf("enter the length of triangle :"); 
                scanf("%i",&l);
                printf("enter the breath of triangle :");
                scanf("%i",&b);
                float area= 0.5*l*b;
                printf("\033[0;32m\n"); // Green
                printf("The area of triangle is :%f",area);
                printf("\033[0m"); // Reset color

            }
            else if (a==2){
                printf("enter the length of triangle :");
                scanf("%i",&l);
                printf("enter the breath of triangle :");
                scanf("%i",&b);
                int h ;
                printf("enter the height of triangle :");
                scanf("%i",&h);
                int perimeter = l+b+h;
                printf("\033[0;32m\n"); // Green
                printf("The perimeter of triangle is :%i",perimeter);
                printf("\033[0m"); // Reset color
            }
            else{
                printf("\033[0;31m");//red
                printf("invalid input try again");
            }
        }

        else if(c==4){  
            printf("\033[0;34m"); // Blue                              //CIRCLE
            printf("select what you want to do find\n ");
            printf("\n1 AREA\n2 PERIMETER:\n");
            printf("select:");
            printf("\033[0m"); // Reset color
            scanf("%i",&a);
            int r;
            if(a==1){
                printf("enter the radius of circle :");
                scanf("%i",&r);
                float pi = 3.14;
                float radius= pi*r*r;
                printf("\033[0;32m\n"); // Green
                printf("the area of circle is :%f",radius);
                printf("\033[0m"); // Reset color
            }
            else if (a==2){
                printf("enter the radius of circle :");
                scanf("%i",&r);
                float pi = 3.14;
                float perimeter=2*r*pi;
                printf("\033[0;32m\n"); // Green
                printf("the perimeter of circle is :%f",perimeter);
                printf("\033[0m"); // Reset color
            }  
            else{
                printf("\033[0;31m");//red
                printf("invalid input try again");
            }  


        }
        
        else{
            printf("\033[0;31m");//red
            printf("invalid input try again");
            printf("\033[0m"); // Reset color
        }

        printf("\033[0;36m");//Cyan
        printf("\nDo you want to use it again\nYES= 1\nNO=2\n");
        printf("select:");
        printf("\033[0m"); // Reset color
        scanf("%d",&loop);
    }
        printf("\033[0;31m");//red
        printf("\n{THANKS FOR USING}\n");
        printf("\033[0m"); // Reset color
        return 0;
}
