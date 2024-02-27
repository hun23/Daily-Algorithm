package main

import "fmt"

func main() {
	var (
		N     int
		slice []int
	)
	fmt.Scan(&N)
	slice = make([]int, N)
	for i := range slice {
		fmt.Scan(&slice[i])
	}

	dp := [2][]int{}
	for i := range dp {
		dp[i] = make([]int, N)
		for j := range dp[i] {
			dp[i][j] = 1
		}
	}

	// 증가
	for i := 0; i < N; i++ {
		for j := 0; j < i; j++ {
			if slice[i] > slice[j] && dp[0][i] < dp[0][j]+1 {
				dp[0][i] = dp[0][j] + 1
			}
		}
	}

	// 감소
	for i := N - 1; i >= 0; i-- {
		for j := N - 1; j > i; j-- {
			if slice[i] > slice[j] && dp[1][i] < dp[1][j]+1 {
				dp[1][i] = dp[1][j] + 1
			}
		}
	}

	ans := 0
	for j := range dp[0] {
		if ans < dp[0][j]+dp[1][j] {
			ans = dp[0][j] + dp[1][j]
		}
	}
	fmt.Println(ans - 1)
}
