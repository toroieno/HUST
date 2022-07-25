#include <iostream>
#include <omp.h>
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
void PrimeNumberParallel(int n, int Prime[]) {
    int i, j;
#pragma omp parallel
    {
        size_t thread = omp_get_thread_num();
        size_t threads = omp_get_num_threads();
        int start = (thread + 0) * n / threads;
        int end = (thread + 1) * n / threads;
        if ((start == 0) or (start == 1)) start = 2;
        for (i = start; i <= end; i++) {
            for (j = 2; j * i <= n; j++)
                Prime[i * j] = 0;
        }
    }
}
int main()
{
    int i, n;
    double Start, Finish, Duration;

    cout << "n = ";
    cin >> n;
    int* Prime = new int[n];
    for (i = 2; i <= n; i++)
        Prime[i] = 1;
    Start = GetTime();
    //program
    PrimeNumberParallel(n, Prime);
    Finish = GetTime();
    Duration = Finish - Start;

    /*cout << "result: ";
    for (i = 2; i <= n; i++)
        if (Prime[i] == 1)
            cout << i << " ";*/
    cout << "\ntime of execution: " << Duration;
    return 0;
}