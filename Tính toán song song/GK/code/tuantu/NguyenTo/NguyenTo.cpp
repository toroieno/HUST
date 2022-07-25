#include <iostream>
#include<stdio.h>
#include<omp.h>
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
void PrimeNumber(int n, int Prime[]) {
    int i, j;
    for (i = 2;i * i <= n;i++)
    {
        for (j = i * i;j <= n;j = j + i)
        {
            if (Prime[j] == 1)
                Prime[j] = 0;
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
    for (i = 2;i <= n;i++)
        Prime[i] = 1;
    Start = GetTime();
    //program
    PrimeNumber(n, Prime);
    Finish = GetTime();
    Duration = Finish - Start;
    for (i = 2; i <= n; i++)
        if (Prime[i] == 1)
            cout << i << " ";
    cout << "\ntime of execution: " << Duration;
    return 0;
}