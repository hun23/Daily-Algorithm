#include <iostream>
#include <stdlib.h>
#include <queue>

int dr[4] = {-1, 0, 0, 1};
int dc[4] = {0, -1, 1, 0};
int N, M, F;

void print_arr(int **arr, int N, int M)
{
	for (int i=0; i<N; i++)
	{
		for (int j=0; j<M; j++)
		{
			std::cout << arr[i][j] << " ";
		}
		std::cout << '\n';
	}
}

int bfs(int **arr, int sr, int sc, bool is_customer)
{
	return 0;
}


void solve(int **arr, int tr, int tc, int idx)
{
	if (M == idx) return;
	// do BFS to get closest customer
	int target_customer = bfs(arr, tr, tc, false);
	int distance = bfs(arr, target_customer/N, target_customer%N, true);

	return;
}


// 1. closest, 2. up - left - right - down
int main(void)
{
	// get input(globals)
	std::cin >> N >> M >> F;
	// get arr
	int **arr = (int **)malloc(sizeof(int *) * N);
	for (int i=0; i<N; i++)
	{
		arr[i] = (int *)malloc(sizeof(int) * N);
		for (int j=0; j<N; j++)
		{
			std::cin >> arr[i][j];
		}
	}

	// get start point
	int tr, tc;
	std::cin >> tr >> tc;

	// get customers' info & apply to arr
	int sr, sc, ar ,ac;
	int customer_idx = 2;
	for (int i=0; i<M; i++)
	{
		std::cin >> sr >> sc >> ar >> ac;
		arr[sr - 1][sc - 1] = customer_idx;
		arr[ar - 1][ac - 1] = -customer_idx;
		customer_idx++;
	}

	solve(arr, tr, tc, 0);

	print_arr(arr, N, N);


}