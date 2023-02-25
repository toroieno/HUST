#include <iostream>
#include <math.h>
#include <string> 
#include <vector>
using namespace std; 

/*  Integral Approximating
    Coded by Le Nguyen Bach - CTTN MI K64
    For any question, feel free to text directly through Messenger or mail me at bach.ln195841@sis.hust.edu.vn */

class function {
    private:
        // PRIVATE STUFF, KEEP OUT
        const int mx = 15;
        const int my = 15; 
        const int mz = 15;  
        const vector<vector<double>> NewtonCotes_coeff = {
            {      0.0}, 
            {      1.0}, 
            { 0.333333,  0.666667}, 
            {     0.25,     0.375,      0.375}, //  ┗( @﹏@ )┛ 
            { 0.155556,  0.355556,   0.133333,  0.355556}, 
            { 0.131944,  0.260417,   0.173611,  0.173611,   0.260417}, 
            { 0.097619,  0.257143,  0.0321429,   0.32381,  0.0321429,   0.257143},
            {0.0869213,  0.207002,  0.0765625,  0.172975,   0.172975,  0.0765625,    0.207002},
            {0.0697707,   0.20769, -0.0327337,  0.370229,  -0.160141,   0.370229,  -0.0327337,  0.20769} 
        }; 

    public:
        double (*value)(double); // Evaluate value of function at a given point
        int    integral_layers;    
        int    n = 3;  
        /*  n = 1 : Trapezoidal rule
            n = 2 : Simpson's 1/3 rule 
            n = 3 : Simpson's 3/8 rule (default) */

        double single_integral(vector<vector<double>> domain) {
            vector<double> yHat; 
            vector<double> hHatT = NewtonCotes_coeff[n]; 
            double         a     = domain[0][0]; 
            double         b     = domain[0][1]; 
            double         dot_product = 0;  
    
            double h = (b - a) / mx;
    
            for (double i = 0; i < n; i++) {
                double element = 0; 
                
                for (double j = 0; j < mx; j++) {
                    element += value(a + (j + i / n) * h);
                }

                yHat.push_back(element); 
            }
    
            for (int i = 0; i < n; i++) dot_product += yHat[i] * hHatT[i]; 
            
            return h * (dot_product + hHatT[0] * (value(b) - value(a)) * 0.5); 
        }

        double double_integral(vector<vector<double>> domain) {
            return 0; // Developing
        }

        double triple_integral(vector<vector<double>> domain) {
            return 0; // Not yet! 
        }
};

// INSERT INPUT HERE
vector<vector<double>> domain    = {{1, 2}};
int                    dimension = 1;
double func_init(double x) {  
    return pow(x, x) - x * log(x); // f(x) = x^x - ln(x^x) 
}

// DON'T EDIT THESE LINES 
int main() {    
    function func; 
    func.value          = func_init; 
    func.integral_layers = 1; 

    cout << func.single_integral(domain); 
    return 0;
}
