package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)

	arr := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&arr[i])
	}

	dp := make([]int, N)
	prev := make([]int, N)
	for i := range dp {
		dp[i] = 1
		prev[i] = -1
	}

	for i := 0; i < N; i++ {
		for j := 0; j < i; j++ {
			if arr[j] < arr[i] {
				if dp[i] < dp[j]+1 {
					dp[i] = dp[j] + 1
					prev[i] = j
				}
			}
		}
	}

	mx := -1
	idx := 0
	for i := range dp {
		if mx < dp[i] {
			idx = i
			mx = dp[i]
		}
	}

	// ans := make([]int, 0)
	// for idx != -1 {
	// 	ans = append(ans, arr[idx])
	// 	idx = prev[idx]
	// }

	// fmt.Println(mx)
	// for i := mx - 1; i >= 0; i-- {
	// 	fmt.Printf("%d", ans[i])
	// 	if i != 0 {
	// 		fmt.Print(" ")
	// 	}
	// }
  fmt.Println(mx)
  reversePrint(idx, arr, prev, true)
}

func reversePrint(i int, arr []int, prev []int, end bool) {
  if i == -1 {
    return
  }
  reversePrint(prev[i], arr, prev, false)
  fmt.Printf("%d", arr[i])
  if !end {
    fmt.Print(" ")
  }
}