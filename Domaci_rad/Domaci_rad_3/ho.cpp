#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;


class HarmonicOscillator{
    public:
            double m;
            double k;
            double x;
            double v;
            double a = -k*x/m;
            double t = 0;
            vector<double> a_lista={a};
            vector<double> x_lista={x};
            vector<double> v_lista={v};
            vector<double> t_lista={t};
            
            HarmonicOscillator(double m_, double k_, double x_, double v_)
            {
                m = m_;
                k = k_;
                x = x_;
                v = v_;
            }

            void move (double dt, double T){
                
                while (t<=T)
                {
                    a = -k*x/m;
                    a_lista.push_back(a);
                    x = x + v*dt;
                    x_lista.push_back(x);
                    v = v + a*dt;
                    v_lista.push_back(v);
                    t = t + dt;
                    t_lista.push_back(t);
                }
            }

            void print(vector <double> vektor){
                for(int i=0; i < vektor.size(); i++)
                {
                    std::cout << vektor[i] << ',';
                }
                std::cout<<std::endl;
}
};
int main(){
    HarmonicOscillator ho(2,10,5,3);
    ho.move(0.5,10);
    ho.print(ho.a_lista);
    ho.print(ho.v_lista);
    ho.print(ho.x_lista);
    ho.print(ho.t_lista);
    return 0;
}