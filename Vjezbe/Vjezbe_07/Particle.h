#include <iostream>
#include <math.h>

class Particle{
    public:
        double v;
        double alpha;
        double x;
        double y;
        double g=-9.81;
        double t=0;
        double vx;
        double vy;
        Particle(double v, double alpha, double x, double y);
    private:
        void evolve(double dt);
    public:
        double range(double dt);
        double time(double dt);
};