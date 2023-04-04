#include <iostream>
#include <vector>

int main(void)
{
	int C;
	std::cin >> C;
	for (int i=0; i<C; i++)
	{
		int N, K;
		std::cin >> N >> K;

		std::vector<int> vec;
		for (int i=0; i< N; i++)
		{
			vec.push_back(1);
		}
		int alive = N;
		int idx = 0;
		while (alive-- != 2)
		{
			if (vec[idx] == 1)
			{
				vec[idx] = 0;
				alive--;
			}
			int cnt = 0;
			while (cnt < K)
			{
				if (vec[idx] == 1)
				{
					cnt++;
					break;
				}
				idx++;
				if (idx >= N)
				{
					idx = 0;
				}
			}
		}
		for (int i = 0; i < N; i++)
		{
			if (vec[i] == 1)
			{
				std::cout << (i + 1);
			}
		}
	}
}