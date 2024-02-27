package main

import "fmt"

func main() {
	var (
		S1 string
		S2 string
    L1 int
    L2 int
	)
	fmt.Scan(&S1)
  fmt.Scan(&S2)

  L1, L2 = len(S1), len(S2)
  dp := make([][]int, L1 + 1)
  for i := range dp {
    dp[i] = make([]int, L2 + 1)
  }

  for i := range dp {
    for j := range dp[i] {
      if i * j == 0 {
        continue
      }
      if S1[i - 1] == S2[j - 1] {
        dp[i][j] = dp[i - 1][j - 1] + 1
      } else {
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
      }
    }
  }
  fmt.Println(dp[L1][L2])
}