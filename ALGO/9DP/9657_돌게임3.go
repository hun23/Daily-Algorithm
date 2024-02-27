package main

import "fmt"

func main()  {
  var N int;
  fmt.Scan(&N)

  dp := make([]bool, 1001)
  for i, v := range []bool{true, true, false, true, true} {
    dp[i] = v
  }
  for i := 5; i <= 1000; i++ {
    dp[i] = !(dp[i - 1] && dp[i - 3] && dp[i - 4])
  }
  if dp[N] {
    fmt.Println("SK")
  } else {
    fmt.Println("CY")
  }
}