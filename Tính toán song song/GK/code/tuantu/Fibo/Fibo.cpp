#include <iostream>
#include <math.h>
#include <inttypes.h>
#include <windows.h>

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

void fibo(uint64_t n, uint64_t *f) {
    for (int i = 1; i <= n; i++)
        f[i] = fib(i);
}
int main()
{
    uint64_t f[100], n;
    double Start, Finish, Duration;

    cout << "n = ";
    cin >> n;
    Start = GetTime();
    fibo(n, f);
    Finish = GetTime();
    Duration = Finish - Start;
    //print result
    cout << "result: ";
    for (int i = 1; i <= n; i++)
        cout << f[i] << " ";
    cout << endl;
    cout << "time of execution: " << Duration << endl;
    return 0;
}
