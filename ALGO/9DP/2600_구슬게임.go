package main

import "fmt"

type Solve struct {
	dp    [][]int
	b_arr [3]int
}

// 1. 그냥 recur -> 3132KB, 32ms
// func recur(dp [][]int, b_arr *[3]int, left int, right int) int {

// 2. (s Solve) 3220KB, 32ms
// 3. (s *Solve) 3156KB, 28ms
func (s *Solve) recur(left int, right int) int {
	if left < 0 || right < 0 {
		return 1
	}
	if left < s.b_arr[0] && right < s.b_arr[0] {
		return 0
	}
	if s.dp[left][right] != -1 {
		return s.dp[left][right]
	}
	cnt := 0
	for _, b := range s.b_arr {
		if left-b >= 0 && s.recur(left-b, right) == 0 {
			cnt += 1
		}
		if right-b >= 0 && s.recur(left, right-b) == 0 {
			cnt += 1
		}
	}
	if cnt == 0 { // 무조건 지는 경우 == 이기는 수가 없는 경우
		s.dp[left][right] = 0
	} else {
		s.dp[left][right] = cnt
	}
	return s.dp[left][right]
}

func main() {
	solve := Solve{
		// dp: left, right만큼 남았을 때
		// 값이 -1: 아직모른다, 1이상: 이긴다(이기는 경우의 수를 센것이므로), 0: 무조건 진다
		dp:    make([][]int, 501),
		b_arr: [3]int{},
	}

	for i := range solve.b_arr {
		fmt.Scan(&solve.b_arr[i])
	}

	for i := range solve.dp {
		solve.dp[i] = make([]int, 501)
	}

	for t := 0; t < 5; t++ {
		// input
		var (
			left  int
			right int
		)
		fmt.Scan(&left)
		fmt.Scan(&right)

		// initialize
		for i := 0; i < 501; i++ {
			for j := 0; j < 501; j++ {
				solve.dp[i][j] = -1
			}
		}

		// dp
		if solve.recur(left, right) != 0 {
			fmt.Println("A")
		} else {
			fmt.Println("B")
		}
	}
}
