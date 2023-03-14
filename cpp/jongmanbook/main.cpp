#include <iostream>

int solve(bool(*areFriends)[10], int *mates, int n, int now)
{
	if (now == n)
	{
		return 1;
	}
	int ret = 0;
	for (int i = 0; i < 10; i++)
	{
		if (areFriends[now][i])
		{
			mates[now] = i;
			ret += solve(areFriends, mates, n, ++now);
		}

	}
	return ret;
}

void print(bool(*areFriends)[10], int *mates)
{
	for (int i = 0; i < 10; i++)
	{
		for (int j = 0; j < 10; j++)
		{
			std::cout << areFriends[i][j] << ' ';
		}
		std::cout << "\n";
	}
}

int main(void)
{
	int T;
	std::cin >> T;
	for (int t = 0; t < T; t++)
	{
		int n, m;
		std::cin >> n;
		std::cin >> m;

		bool areFriends[10][10];
		for (int i = 0; i < 10; i++)
		{
			for (int j = 0; j < 10; j++)
			{
				areFriends[i][j] = false;
			}
		}

		int mates[10];
		for (int i = 0; i < 10; i++)
		{
			mates[i] = -1;
		}
		for (int i = 0; i < m; i++)
		{
			int a, b;
			std::cin >> a >> b;
			areFriends[a][b] = true;
			areFriends[b][a] = true;
		}
		int answer = solve(areFriends, mates, n, 0);
		std::cout << answer << '\n';
	}
	system("pause");
}