#include <iostream>
#include <iomanip>
#include "MyFuncs.h"
#include <ctime>
#include <math.h>
#include <stdlib.h>
#include <fstream>
using namespace std;
static const int Nx = pow(2, 10);
static const int Ny = pow(2, 10);
static const int Nt = pow(2, 4);
int main() {
	const float m = 1.0 / 3.0;
	const float a = 1.0 / 12.0;
	const float sigma = 2.0 * a ;
	const float Co = 1.0e-5;
	const float pi = 3.14159265;
	srand(time(NULL));
	
	// Задание сетки по х
	float x_min = 0.0;
	float dx = 0.01;
	float *x = new float [Nx];
	for(int i = 0; i < Nx; i++) {

		x[i] = x_min + i * dx;
	}
	cout << "строка 28" << endl;
	// Задание сетки по y
	float y_min = 0.0;
	float dy = 0.01;
	float *y = new float [Ny];
	for(int i = 0; i < Ny; i++) {

		y[i] = y_min + i * dy;
	}
	cout << "строка 37" << endl;
	// Задание сетки по t
	float t_min = 0.0;
	float dt = 0.01;
	float *t = new float [Nt];
	for(int i = 0; i < Nx; i++) {

		t[i] = t_min + i * dt;
	}
	cout << "строка 46" << endl;

	// Значение отклонения h  в начальный момент времени t = n
	float *h = new float [Nx * Ny];
	cout << "строка 50" << endl;
	for(int i = 0; i < Nx; i++) {
		for(int j = 0; j < Ny; j++) {
			if( (pow(abs(i - 300), 2) + pow(abs(j - 250), 2) ) < 80) {
				h[i * Ny + j] = 0.001;
			}
			else {
				h[i* Ny + j] = 0.0;
			}
		}
	}
	cout << "строка 50" << endl;
	return 0;

}
