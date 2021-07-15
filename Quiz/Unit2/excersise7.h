#include <stdio.h>
#include <stdlib.h>

typedef struct robot{

    char *name;
    char *type;
    float height;
    float weight;
    int degreeOffreedom;

    void (*SayHelloToRobot)(struct robot);

}ROBOT;

void SayHelloToRobot(ROBOT a_robot ){
    printf("\n %s %s", "Hello World my name is", a_robot.name);
}
