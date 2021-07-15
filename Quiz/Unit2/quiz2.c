#include <stdio.h>
#include "./excersise7.h"

int main(){
    ROBOT markovito;
    markovito.name = "Markovito";
    markovito.type = "ServiceRobot";
    markovito.height = 1.2;
    markovito.weight = 2.5;
    markovito.degreeOffreedom = 3;

    markovito.SayHelloToRobot = SayHelloToRobot;

    ROBOT tiago;
    tiago.name = "Tiago";
    tiago.type = "ServiceRobot";
    tiago.height = 1.7;
    tiago.weight = 2.8;
    tiago.degreeOffreedom = 7;
    tiago.SayHelloToRobot = SayHelloToRobot;

    markovito.SayHelloToRobot(tiago);

}