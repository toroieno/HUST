#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <windows.h>
#include <time.h>
#include <random>
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
// Function for simple definition of matrix and vector elements
void DummyDataInitialization(double* pMatrix, double* pVector, int Size) {
	int i, j; // Loop variables
	for (i = 0; i < Size; i++) {
		pVector[i] = 1;
		for (j = 0; j < Size; j++)
			pMatrix[i * Size + j] = i;
	}
}
// Function for random definition of matrix and vector elements
void RandomDataInitialization(double* pMatrix, double* pVector, int Size) {
	int i, j; // Loop variables
	//srand(unsigned(clock()));
	srand(time(NULL));
	for (i = 0; i < Size; i++) {
		srand(time(NULL));
		pVector[i] = rand() / double(1000);
		for (j = 0; j < Size; j++) {
			srand(time(NULL));
			pMatrix[i * Size + j] = rand() / double(1000);
		}
	}
}
// Function for memory allocation and definition of object�s elements
void ProcessInitialization(double*& pMatrix, double*& pVector,
	double*& pResult, int& Size) {
	// Size of initial matrix and vector definition
	do {
		printf("\nEnter size of the initial objects: ");
		scanf_s("%d", &Size);
		printf("\nChosen objects size = %d\n", Size);
		if (Size <= 0)
			printf("\nSize of objects must be greater than 0!\n");
	} while (Size <= 0);
	// Memory allocation 
	pMatrix = new double[Size * Size];
	pVector = new double[Size];
	pResult = new double[Size];
	// Definition of matrix and vector elements
	DummyDataInitialization(pMatrix, pVector, Size);
}
// Function for formatted matrix output
void PrintMatrix(double* pMatrix, int RowCount, int ColCount) {
	int i, j; // Loop variables
	for (i = 0; i < RowCount; i++) {
		for (j = 0; j < ColCount; j++)
			printf("%7.4f ", pMatrix[i * RowCount + j]);
		printf("\n");
	}
}
// Function for formatted vector output
void PrintVector(double* pVector, int Size) {
	int i;
	for (i = 0; i < Size; i++)
		printf("%7.4f ", pVector[i]);
}
// Function for matrix-vector multiplication
void ResultCalculation(double* pMatrix, double* pVector, double* pResult,
	int Size) {
	int i, j; // Loop variables
	for (i = 0; i < Size; i++) {
		pResult[i] = 0;
		for (j = 0; j < Size; j++)
			pResult[i] += pMatrix[i * Size + j] * pVector[j];
	}
}
// Function for computational process termination
void ProcessTermination(double* pMatrix, double* pVector, double* pResult) {
	delete[] pMatrix;
	delete[] pVector;
	delete[] pResult;
}
int main() {
	double* pMatrix; // The first argument - initial matrix
	double* pVector; // The second argument - initial vector
	double* pResult; // Result vector for matrix-vector multiplication 
	int Size; // Sizes of initial matrix and vector
	double Start, Finish, Duration;
	printf("Serial matrix-vector multiplication program\n");
	// Memory allocation and definition of objects' elements
	ProcessInitialization(pMatrix, pVector, pResult, Size);
	// Matrix and vector output
	printf("Initial Matrix \n");
	//PrintMatrix(pMatrix, Size, Size);
	printf("Initial Vector \n");
	//PrintVector(pVector, Size);
	// Matrix-vector multiplication
	Start = GetTime();
	ResultCalculation(pMatrix, pVector, pResult, Size);
	Finish = GetTime();
	Duration = Finish - Start;
	// Printing the result vector
	printf("\n Result Vector: \n");
	//PrintVector(pResult, Size);
	// Printing the time spent by matrix-vector multiplication
	printf("\n Time of execution: %f\n", Duration);
	// Computational process termination
	ProcessTermination(pMatrix, pVector, pResult);
}
