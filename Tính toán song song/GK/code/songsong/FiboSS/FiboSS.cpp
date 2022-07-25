#include <iostream>
#include <math.h>
#include <inttypes.h>
#include <omp.h>
#include <Windows.h>

using namespace std;

// Function that converts numbers form LongInt type to double type
double LiToDouble(LARGE_INTEGER x) {
    double result =
        ((double)x.HighPart) * 4.294967296E9 + (double)((x).LowPart);
    return result;
}
// Function that gets the timestamp in seconds
double GetTime() {
    LARGE_INTEGER lpFrequency, lpPerfomanceCount;
    QueryPerformanceFrequency(&lpFrequency);
    QueryPerformanceCounter(&lpPerfomanceCount);
    return LiToDouble(lpPerfomanceCount) / LiToDouble(lpFrequency);
}

uint64_t fib(unsigned m) { // Direct Calculation, correct for abs(m) <= 92
    double sqrt5r = 1.0 / sqrt(5.0);
    double golden = (1.0 + sqrt(5.0)) / 2.0;
    return rint(pow(golden, m) * sqrt5r);
}

void fib_sequence_parallel(uint64_t n, uint64_t* f) {
#pragma omp parallel
    {
        size_t thread = omp_get_thread_num();
        size_t threads = omp_get_num_threads();
        int start = (thread + 0) * n / threads;
        int end = (thread + 1) * n / threads;
        for (int i = start; i < end; i++) {
            f[i] = fib(i);
        }
    }
}
// max 92
int main(void) {
    uint64_t n;
    uint64_t f[1000];
    double Start, Finish, Duration;

    cout << "n = ";
    cin >> n;
    //program
    Start = GetTime();
    fib_sequence_parallel(n+1, f);
    Finish = GetTime();
    Duration = Finish - Start;
    //end
    for (int i = 1; i <= n; i++)
        cout << f[i] << " ";
    cout << "\n time of execution: " << Duration;

    return 0;
}