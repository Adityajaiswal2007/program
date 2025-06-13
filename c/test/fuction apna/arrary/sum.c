#include<stdio.h>
int main(){
    int size,sum=0;
    printf("enter the size of array:");
    scanf("%d",&size);
    int arr[size];
    printf("enter %d elements of array",size);
    for(int i=0;i<size;i++){
        scanf("%d",&arr[i]);
    }
    printf("elements of array are:");
    for(int i=0;i<size;i++){
        printf("%d\n",arr[i]);
    }
    for(int i=0;i<size;i++){
        sum = arr[i]+sum;


    }
    int avg=sum/size;
    printf("The sum is %d\n",sum);
    printf("The average is %d",avg);

    return 0;
}