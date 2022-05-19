#include <iostream>
#include <math.h>
#include "particle.h"
Particle::Particle(double v_, double alpha_, double x_, double y_)
{
   v=v_;
   alpha=alpha_;
   x=x_;
   y=y_;
   vx=v*cos(alpha);
   vy=v*sin(alpha);
}
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
   