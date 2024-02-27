package main

import "fmt"

func main() {
  var (
    N int
    arrArr [3][]int
  )
  fmt.Scan(&N)
  for i := range arrArr {
    arrArr[i] = make([]int, N)
    for j := range arrArr[i] {
      fmt.Scan(&arrArr[i][j])
    }
  }
  // idx 까지 고려했을 때 A가 이길 수 있는지?
  dp := make([]bool, N)
  dp[0] = false
  for i := 1; i < N; i++ {
    for j := 0; j < i; j++ {
      
    }
  }
}