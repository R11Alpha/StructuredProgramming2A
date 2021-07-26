#include<stdio.h>
#include<stdlib.h>

void main(int argc, char * argv[]) {

    int i, prom = 0;
    float total;

    printf("The average is: ");

    for (i = 1; i < argc; i++){
        prom = prom + atoi(argv[i]);
      }
    argc = argc - 1;
    total = prom / argc;
    printf("%.2f\n",total);

}