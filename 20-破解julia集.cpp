#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <string>
#include <iomanip>

using namespace std;

ifstream fin("6.txt");
double interiorColorMap[256];
int result[480][640];
int ans[480][640];

double Rstart = -1.251950, Rstop = -1.251950;
double Istart = -0.241274, Istop = -0.241274;
double step = 0.00001;

void init()
{
	double tmp = 1.0;
	for (int i = 0; i < 256; i++)
	{
		interiorColorMap[i] = tmp;
		tmp *= 7.0 / 8;
	}
	for (int i = 0; i < 480; i++)
		for (int j = 0; j < 640; j++)
			fin >> ans[i][j];
}

double iterateEquation(double Cr, double Ci, int iterations, double Dr, double Di)
{
	double Zr = Cr, Zi = Ci, Tr = Cr * Cr, Ti = Ci * Ci, L = min(Tr, Ti), v, e;
	int n = 0;
	while(n < iterations && (Tr + Ti <= 100))
	{
		Zi = 2 * Zr * Zi + Di;
		Zr = Tr - Ti + Dr;
		Tr = Zr * Zr;
		Ti = Zi * Zi;
		if (Tr < L)
			L = Tr;
		if (Ti < L)
			L = Ti;
		n++;
	}
	if (Tr + Ti > 100)
	{
		v = n;
		e = (Tr + Ti) / 100.0;
		if (e < 10.0)
			v -= (e - 1.0) / 18.0;
		else
			v -= 0.5 + (e - 10.0) / 180.0;
		v = v / iterations;
		v = 2.0 * v - v * v;
		v = 2.0 * v - v * v;
		return 255.0 - 255.0 * v;
	}
	int vv = 0;
	int s = 128;
	while (s >= 1)
	{
		if (L < interiorColorMap[vv + s])
			vv += s;
		s /= 2;
	}
	return vv;
}

void draw(double Dr,double Di)
{
	int steps = 256;
	double step = 3.0 / 512;
	
#pragma omp parallel for schedule(dynamic)
	for (int sy = 0; sy < 480; ++sy)
	{
		double Ci = (sy + 0.5 - 240) * step;
		for (int sx = 0; sx < 640; ++sx)
		{
			double Cr = (sx + 0.5 - 320) * step;
			double v = 0;
			for (int sr = -1; sr <= 1; ++sr)
				for (int si = -1; si <= 1; ++si)
					v += iterateEquation(Cr + sr * step / 4, Ci + si * step / 4, steps, Dr, Di);
			v = v / 9;
			result[sy][sx] = int(round(v) + 0.00001);
		}
	}
}

int main()
{
	init();
	int minD = 1<<30;
	double minR = 0, minI = 0;
	while (step >= 0.000001)
	{
		for (double R = Rstart; R <= Rstop; R += step)
		{
			for (double I = Istart; I <= Istop; I += step)
			{
				draw(R, I);
				int sum = 0;
				for (int i = 0; i < 480; i++)
					for (int j = 0; j < 640; j++)
						sum += abs(result[i][j] - ans[i][j]);
				if (sum < minD)
				{
					minD = sum;
					minR = R;
					minI = I;
				}
			}
			cout << R << " Finished" << endl;
		}
		cout << setprecision(10) << minD << ' ' << minR << ' ' << minI << ' ' << endl;
		Rstart = minR - step; Rstop = minR + step;
		Istart = minI - step; Istop = minI + step;
		step = step * 0.1;
	}
}
