#include <iostream>
#include <omp.h>
#include <fstream>
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
void FindMax(int n, int a[], int b[]) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (a[i] >= a[j]) b[i]++;
        }
    }
}
void FindMin(int n, int a[], int c[]) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (a[i] <= a[j]) c[i]++;
        }
    }
}
int main()
{
    int flag = 0, n, i;
    fstream file;
    double Start, Finish, Duration;
    file.open("../../../array.txt", ios::in); // random array in file "array.txt"
    if (file.fail()) {
        cout << "fail to open file \"array\"";
        flag = 1;
    }
    if (flag != 1) {
        file >> n;
        int* a = new int[n];
        int* b = new int[n] {0}; // find max
        int* c = new int[n] {0}; //find min
        for (i = 0; i < n; i++)
            file >> a[i];
        Start = GetTime();
        //program
        FindMax(n, a, b);
        FindMin(n, a, c);
        Finish = GetTime();
        Duration = Finish - Start;
        for (int i = 0; i < n; i++)
            if (b[i] == n) {
                cout << "Max: " << a[i] << endl;
                break;
            }
        for (int i = 0; i < n; i++)
            if (c[i] == n) {
                cout << "Min: " << a[i] << endl;
                break;
            }
        cout << "time of execution: " << Duration;
    }
    file.close();
    return 0;
}
