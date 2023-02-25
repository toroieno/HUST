// Gradient Descent
// Coded by Le Nguyen Bach - CTTN MI K64

#include <iostream>
#include <math.h>
#include <vector>
#define ERROR   1e-4
#define EPSILON 1e-8
#define PI      3.141592654
#define E       2.718281828
using namespace std;

// Print an array to the console
void ArrayPrint(vector<double> arr) {
    string space;
    cout << "[";
    for (int i = 0; i < arr.size(); i++) 
    {
        space = (i == arr.size() - 1) ? "" : "  "; 
        cout << arr[i] << space;
    }
    cout << "]\n";
}

// 2 norm - Euclidean norm
double Norm2(vector<double> vec) {
    double sum;
    for (int i = 0; i < vec.size(); i++) {
        sum += vec[i] * vec[i];
    }
    return sqrt(sum); 
}


struct Function {
    int dimension;
    double (*value)(vector<double>);

    // Gradient approximation 
    vector<double> Gradient(vector<double> point) {
        vector<double> grad;
        double         f_0neg, f_0pos, df;
        
        for (int i = 0; i < point.size(); i++) {
            point[i] -= EPSILON;
            f_0neg    = value(point);
        
            point[i] += 2 * EPSILON;
            f_0pos    = value(point);

            point[i] -= EPSILON; 

            df = (f_0pos - f_0neg) / (2 * EPSILON);
            grad.push_back(df); 
        }

        return grad;
    }

    // Backtracking line search (BLS) Gradient descent
    vector<double> BLS_GradientDescent(vector<double> point) {
        int            dimension  = point.size();
        int            iteration  = 0;
        double         alpha      = 0.5; // α ∈ (0, 0.5]
        double         beta       = 0.9; // β ∈ (0, 1). BLS work best for β = 0.9 
        double         t          = 1;   // initializer 
        vector<double> new_point0 = point;
        vector<double> new_point1 (dimension, 0);
        vector<double> adjustment (dimension, 0);

        while (true) {
            iteration++;
            vector<double> grad_f = Gradient(new_point0);

            for (int i = 0; i < dimension; i++) {
                adjustment[i] = t * grad_f[i];
                new_point1[i] = new_point0[i] - adjustment[i];     
            }

            vector<double> temp = new_point1; 

            if (value(new_point1) > value(new_point0) - alpha * t * pow(Norm2(grad_f), 2)) {
                t *= beta;
                continue; 
            } else if (Norm2(adjustment) < ERROR) {
                break;
            } else {
                new_point0 = new_point1; 
            }
        }
        cout << "Number of iteration(s) is " << iteration << "\n"; 
        return new_point1;
    }
};

// INSERT INPUT HERE
vector<double> point_init = {1, 2}; // initial approximation 
int            dimension  = 3;      

double func_init(vector<double> x) {
    return -(x[0]*x[0] + 4*x[1]*x[1]) * exp(-4*x[0]*x[0] - x[1]*x[1]); // -(x^2 + 4y^2)exp(-4x^2 - y^2)
}


int main() {
    Function func{dimension, func_init};
    vector<double> minima = func.BLS_GradientDescent(point_init); 
    cout << "Function takes minimum value at ";
    ArrayPrint(minima);
    return 0;
}