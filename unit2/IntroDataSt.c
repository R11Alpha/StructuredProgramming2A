#include <stdio.h>
#include <string.h>
#include <stdio.h>

#include "./test/utils.h"

//arrays
int myIntArray[5];

int myInt = 4;
float myFloat = 3.1416;


typedef struct mago{

        int vida;
        int mana;
        char* nombre;
        //mas atributos//
        //sayHello
        void (*Saludo) (char message[]);
        int (*sumaDosNumeros) (int  argumento1, int argumento2 );
}Mago;

// typedef struct mago Mago;

int main(){

        Mago mario = { 100, 100, "Mario_Canche", sayHello, addTwoNumbers };
        struct mago miguel = {200, 200, "Miguel"};

        printf( "%s\n", mario.nombre  );
        mario.Saludo( "Hola soy un mago!");
        printf( "%d\n"  , mario.sumaDosNumeros(20,25)   );

        fillArray( myIntArray, 5);
        printArray1D( myIntArray,  5   );
        printf("%d",  myIntArray[0]   );
        printf("%d",  myIntArray[1]   );
        printf("%d",  myIntArray[2]   );
        printf("%d",  myIntArray[3]   );
        printf("%d",  myIntArray[4]   );

        Array* myArray =  returnArray();
        printf(  "\n%d ", myArray->dirArray[0] );
        printf(  "\n%d ", myArray->dirArray[1] );
        printf(  "\n%d ", myArray->dirArray[2] );

        return 0;
}