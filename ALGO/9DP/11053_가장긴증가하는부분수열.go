package main

import (
	"fmt"
)

type S struct {
	slice []int
	N     int
	dp    [][]int
}

func (s *S) recur(idx int, prev int, temp []int) int {

	if idx == s.N+1 {
		return 0
	}

	if s.dp[idx][prev] != -1 {
		return s.dp[idx][prev]
	}

	ret1 := s.recur(idx+1, prev, temp) // 고르지 않는 경우
	ret2 := 0
	if s.slice[prev] < s.slice[idx] {
		ret2 = 1 + s.recur(idx+1, idx, append(temp, idx)) // 고르는 경우
	}

	if ret1 < ret2 {
		s.dp[idx][prev] = ret2
	} else {
		s.dp[idx][prev] = ret1
	}
	return s.dp[idx][prev]
}

func main() {
	s := S{}
	fmt.Scan(&s.N)
	s.slice = make([]int, s.N+1)
	for n := 0; n < s.N; n++ {
		fmt.Scan(&s.slice[n+1])
	}
	s.dp = make([][]int, s.N+1)
	for i := range s.dp {
		s.dp[i] = make([]int, s.N+1)
		for j := 0; j < s.N+1; j++ {
			s.dp[i][j] = -1
		}
	}
	temp := make([]int, 0)
	fmt.Println(s.recur(0, 0, temp))
}
