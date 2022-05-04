#include <iostream>
#include <math.h>
#include "particle.h"
void Particle::evolve(double dt)
{
    vy = vy + g*dt;
    x = x + vx*dt;
    y = y + vy*dt;
    t = t + dt;
}
double Particle::range(double dt)
{
    while (y>=0)
    {
        evolve(dt);
    }
    return(x);
}
        
double Particle::time(double dt)
{
    while (y>=0)
    {
        evolve(dt);
    }
    return(t);
}
   