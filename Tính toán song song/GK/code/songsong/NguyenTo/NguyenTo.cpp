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
int main()
{
    int prime[90000], i, j, n;
    double Start, Finish, Duration;
    printf("\nIn order to find prime numbers from 1 to n, enter the value of n:");
    scanf_s("%d", &n);
    Start = GetTime();
//#pragma omp parallel for
    for (i = 2;i <= n;i++)
    {
        prime[i] = 1;
    }
    //prime[1] = 0;
    for (i = 2;i * i <= n;i++)
    {
        /* multi-threading to remove multiples of prime number i from the list (array) */

//#pragma omp parallel for
        for (j = i * i;j <= n;j = j + i)
        {
            if (prime[j] == 1)
                prime[j] = 0;
        }

    }
    printf("\nPrime numbers from 1 to %d are\n", n);
    Finish = GetTime();
    Duration = Finish - Start;
    for (i = 2;i <= n;i++)
    {
        if (prime[i] == 1)
        {
            printf("%d\t ", i);
        }
    }
    printf("\n");
    cout << "time of execution: " << Duration;
}