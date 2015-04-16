#include <iostream>
using namespace std;

int main() {

	// Задание сетки по х
	float x_min = 0.0;
	float x_max = 60.0;
	float dx = 0.1;
	int Nx = int((x_max - x_min) / dx);
	float x[Nx];
	x[0] = x_min;
	for(int i = 1; i < Nx; i++) {

		x[i] = x[i-1] + dx;
	}
	
return 0;
}
	
	
