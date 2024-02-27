package main

import (
	"fmt"
	"strconv"
)

func main() {
	var N int
	fmt.Scan(&N)

	const MAX_N = 1_000_001

	// dp값이 -1: 이길 수 없다, n: 이기기 위해 골라야 하는 가장 작은 수
	dp := [MAX_N]int{}

	// initialize
	for i := 0; i < MAX_N; i++ {
		dp[i] = -1
	}

	for i := 10; i < MAX_N; i++ {
		var (
			stringI        = strconv.Itoa(i) // 문자열로 i를 변환
			length         = len(stringI)    // 변환된 길이
			minValToChoose = MAX_N           // 골라야 할 가장 작은 수 초기값
		)
		for left := 0; left < length; left++ {
			for right := left; right < length; right++ {
				// left ~ right까지 부분수열
				a, _ := strconv.Atoi(stringI[left : right+1])
				// 부분수열을 숫자로 변환 후 0과 자기자신 제외
				if a == 0 || a == i {
					continue
				}
				// dp[i-a] == -1이라는 것은 부분수열을 고르고 난 뒤(i - a가 된 뒤) 상대가 진다는 뜻
				if dp[i-a] == -1 && a < minValToChoose {
					minValToChoose = a // 골라야 할 최소값 업데이트
				}
			}
		}

		if minValToChoose == MAX_N { // 상대가 지는 경우가 없으면 = minValToChoose가 업데이트 되지 않으면
			dp[i] = -1 // 이길 수 없다
		} else {
			dp[i] = minValToChoose
		}
	}
	fmt.Println(dp[N])
}
