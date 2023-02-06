# 설명
백준 문제를 Pyton 및 Java로 매일 푸는 TIL repo

## Baekjoon
- 230112:
  > [Baekjoon: 2557, io(java:BufferedReader/Writer)](https://www.acmicpc.net/problem/2557)

  > [Baekjoon: 2750, sorting(java:Arrays.sort())](https://www.acmicpc.net/problem/2750)


- 230113:
  > [Baekjoon: 2587, average, sorting](https://www.acmicpc.net/problem/2587)

  > [Baekjoon: 25305, sorting, io(java:split())](https://www.acmicpc.net/problem/25305)

  > [Baekjoon: 2108, sorting, java(int/Integer, double, round, Collections, ArrayList, Hashmap)](https://www.acmicpc.net/problem/2108)

  > [Baekjoon: 11650, sorting, java(Hashmap, ArrayList, split, Collections)](https://www.acmicpc.net/problem/11650)
  
- 230114:
  - > [Baekjoon: Solved Ac Class 1](https://solved.ac/class/1)

    - 1152: String.trim(), String.isEmpty()

    - 1157: String.toCharArray(), ascii

- 230115:
  - > [Baekjoon: Solved Ac Class 1](https://solved.ac/class/1)

    - 1152: String.trim(), String.isEmpty()
    - 1157: String.toCharArray(), ascii

- 230116:
  - > [Baekjoon: Solved Ac Class 1 (*finished*)](https://solved.ac/class/1)

    - 10809: String.indexOf()
    - 10951: EOF
    - 11654: BufferedReader.read()
  - > [Baekjoon: Solved Ac Class 2](https://solved.ac/class/2)
  
  - > [Baekjoon: 1018, **Bruteforce**, Python(.strip(), copy.deepcopy())](https://www.acmicpc.net/problem/1018)

    - Python: [더 나은 풀이](https://bambbang00.tistory.com/43)와 비교하기 -> Java에 적용

  - > [Baekjoon: 1181, Java(String.equals())](https://www.acmicpc.net/problem/1181)

    - Java: 이중 배열 선언하는 방법

  - > [Baekjoon: 1259](https://www.acmicpc.net/problem/1181)

  - > [Baekjoon: 1436, **Bruteforce**](https://www.acmicpc.net/problem/1436)

  - > [Baekjoon: 1654, **Binary Search**](https://www.acmicpc.net/problem/1654)

    - Java: int로 하면 overflow로 corner case에서 답이 나오지 않는다, 변수 자료형을 long으로 바꾸어서 해결

- 230117:
  - > [Baekjoon: Solved Ac Class 2](https://solved.ac/class/2)

  - > [Baekjoon: 1874, **Stack**](https://www.acmicpc.net/problem/1874)

  - > [Baekjoon: 1920, **Binary Search**](https://www.acmicpc.net/problem/1920)

  - > [Baekjoon: 1929, **Prime Numbers**](https://www.acmicpc.net/problem/1929)

    - 에라토스테네스의 체 구현
  
  - > [Baekjoon: 1966, **Queue**](https://www.acmicpc.net/problem/1966)

  - > [Baekjoon: 1978, **Prime Numbers**](https://www.acmicpc.net/problem/1978)

  - > [Baekjoon: 2164, **Queue**](https://www.acmicpc.net/problem/2164)

     - Python: 일반적인 list 사용시 시간초과 발생, `from Collections import deque`와 `deque.popleft()`사용필요

     - Java: 마찬가지로 `import java.util.Queue, import java.util.LinkedList` 후, `queue.poll()`, `queue.remove()` 사용 필요
  - > [Baekjoon: 2231, **Bruteforce**](https://www.acmicpc.net/problem/2231)

  - > [Baekjoon: 2292](https://www.acmicpc.net/problem/2292)

- 230118:
  - > [Baekjoon: 2609](https://www.acmicpc.net/problem/2609)
    
     - 최대공약수(GCD) & 최소공배수(LCM)
  - > [Baekjoon: 2751, sorting](https://www.acmicpc.net/problem/2751)
  
  - > [Baekjoon: 2798, **Brute Force**](https://www.acmicpc.net/problem/2798)

     - 재귀함수로 구현.... 쉬운 방법이 있을지도?
  - > [Baekjoon: 4153](https://www.acmicpc.net/problem/4153)
  
  - > [Baekjoon: 9012](https://www.acmicpc.net/problem/9012)

  - > [Baekjoon: 10250](https://www.acmicpc.net/problem/10250)

  - > [Baekjoon: 10814, sorting](https://www.acmicpc.net/problem/10814)

  - > [Baekjoon: 10816, sorting, **Binary Search**, hashmap](https://www.acmicpc.net/problem/10816)
  
     - 파이썬 str.join()사용, 풀긴 했는데 느리다. 더 찾아봐야 할 것 같다.
     - 자바: 아직...

  - > [Baekjoon: 11866, queue](https://www.acmicpc.net/problem/11866)

     - queue를 이용한 원형(=순환하는) 자료 다루기, Java: StringBuilder

  - > [Baekjoon: 11050, Combination](https://www.acmicpc.net/problem/11050)

     - **이항계수** 개념에 대해 더 공부할 필요가 있을 것 같다.

  - > [Baekjoon: 10828, stack, class](https://www.acmicpc.net/problem/10828)

     - 파이썬: 통과 / 자바: 클래스 구현 및 static 개념 다시 확인

  - > [Baekjoon: 2775, **Dynamic Programming**](https://www.acmicpc.net/problem/2775)
      
     - 파이썬: 리스트 컴프리헨션, 삼항연산자
     - 자바: 삼항연산자, 이중 int 배열

  - > [Baekjoon: 10989, sorting](https://www.acmicpc.net/problem/10989)

     - 메모리 제한이 심한 문제, 조건에 따른 해결방법 필요

  - > [Baekjoon: 2869](https://www.acmicpc.net/problem/2869)

  - > [Baekjoon: 15829, hashing](https://www.acmicpc.net/problem/15829)

   - > [Baekjoon: 10773, stack](https://www.acmicpc.net/problem/10773)

   - > [Baekjoon: 11651, sorting](https://www.acmicpc.net/problem/11651)

- 230125:

  - > [Baekjoon: 2805, **Binary Search**](https://www.acmicpc.net/problem/2805)
    - 자바: 수가 클때면 언제나 오버플로우 대비해야
    - 파이썬: 이분탐색할 때 쓸데없이 배열을 순환하는 일을 만들지 않을 필요가 있다. 

  - > [Baekjoon: 7568, **Bruteforce**](https://www.acmicpc.net/problem/7568)

- 230126:

  - > [Baekjoon: 18111, **Bruteforce**](https://www.acmicpc.net/problem/18111)
    - 자바:X
    - 파이썬:O, Bruteforce 문제여도 리스트 반복은 최대한 피하기 => dictionary등 다른 방법 찾기

  - > [Baekjoon: 2839, **Dynamic Programming, Greedy**](https://www.acmicpc.net/problem/2839)
    - 자바:X
    - 파이썬:O -> 왜 DP, greedy일까..? dp/greedy식으로 하면 재귀횟수가 넘친다.

  - > [Baekjoon: 4949, Stack](https://www.acmicpc.net/problem/4949)
    - 자바:X
    - 파이썬:O, 더 나은 코드 찾아보기

  - > [Baekjoon: 10845, Queue](https://www.acmicpc.net/problem/10845)
    - 자바:X
    - 파이썬:O, class 만들기 연습

  - > [Baekjoon: 10866, Deque](https://www.acmicpc.net/problem/10866)
    - 자바:X
    - 파이썬:O, class 만들기 연습

  - > [SW_IM추천, Baekjoon: 1244](https://www.acmicpc.net/problem/1244)
    - 자바:X
    - 파이썬:O, 늘 인덱스 조심하기, 

  - > [Baekjoon: 2309, SW_IM](https://www.acmicpc.net/problem/2309)
    - 자바:X
    - 파이썬:O, 반복문 도는 리스트에서 요소 제거할때 인덱스로 접근하면 꼬인다
      - arr.remove()로 값을 통해 접근해서 지울 것. 

- 230127:

  - > [Baekjoon: Solved Ac Class 3](https://solved.ac/class/3)

  - > [Baekjoon: 1260, **DFS, BFS**](https://www.acmicpc.net/problem/1260)
    - 자바:X
    - 파이썬:O, DFS/BFS 기초 구현 공부

  - > [Baekjoon: 2178, **미로찾기, BFS**](https://www.acmicpc.net/problem/2178)
    - 자바:X
    - 파이썬:O, 미로찾기 기초, BFS적용

  - > [SWA: 1249, **Dijkstra Algorithm**]
    - 자바:X
    - 파이썬:O, 다익스트라 알고리즘 연습

- 230130:
  - > [Baekjoon: 1012, **DFS, BFS**](https://www.acmicpc.net/problem/1012)
    - 자바:X
    - 파이썬:O, DFS/BFS 기초 적용

  - > [Baekjoon: 1463, **DP**](https://www.acmicpc.net/problem/1463)
    - 자바:X
    - 파이썬:O

  - > [Baekjoon: 2606, **DFS, BFS**](https://www.acmicpc.net/problem/2606)
    - 자바:X
    - 파이썬:O

- 230130:
  - > [Baekjoon: 2579, **Dynamic Programming**](https://www.acmicpc.net/problem/2579)
    - 자바:X
    - 파이썬:O

  - > [SW_IM추천, Baekjoon: 2116, **Bruteforce**](https://www.acmicpc.net/problem/2116)
    - 자바:X
    - 파이썬:O

  - > [SW_IM추천, Baekjoon: 2304, **Bruteforce**](https://www.acmicpc.net/problem/2304)
    - 자바:X
    - 파이썬:O, 이상하게 푼 것 같다..?

  - > [SW_IM추천, Baekjoon: 2477](https://www.acmicpc.net/problem/2477)
    - 자바:X
    - 파이썬:O, 이상하게 푼 것 같다..? but 더 나은 풀이 추가.

- 230201:
  - > [SW_IM추천, Baekjoon: 2605](https://www.acmicpc.net/problem/2605)
    - 자바:X
    - 파이썬:O

  - > [SW_IM추천, Baekjoon: 13300](https://www.acmicpc.net/problem/13300)
    - 자바:X
    - 파이썬:O

- 230202:
  - > [SWA: 1210]
    - 자바:X
    - 파이썬:O
    
  - > [SWA: 1211]
    - 자바:X
    - 파이썬:O
    
  - > [SWA: 1974]
    - 자바:X
    - 파이썬:O

  - > [Class3, Baekjoon: 11724](https://www.acmicpc.net/problem/11724)
    - 자바:X
    - 파이썬:O

  - > [Class3, Baekjoon: 5430](https://www.acmicpc.net/problem/5430)
    - 자바:X
    - 파이썬:O, 구현할 때 문제 설명을 따라가기 보다 더 생각을 하고 푸는 것이 시간초과 해결에 도움이 된다.
    
    
0202 스터디 정리
print(*st_list, sep=" ")  # 공백 포함 출력
*더 사용할 것
방배정/카드놀이 확인
10163 JW 코드 확인


- 230203:
  - > [Class3, Baekjoon: 7569, ***BFS***](https://www.acmicpc.net/problem/7569)
    - 자바:X
    - 파이썬:O, 3차원 배열 BFS
  - > [Class3, Baekjoon: 7576, ***BFS***](https://www.acmicpc.net/problem/7576)
    - 자바:X
    - 파이썬:O
  - > [Class3, Baekjoon: 1003, ***Dynamic Programming***](https://www.acmicpc.net/problem/1003)
    - 자바:X
    - 파이썬:X

  - > [Class3, Baekjoon: 1074, ***???***](https://www.acmicpc.net/problem/1074)
    - 자바:X
    - 파이썬:X

  - > [Class3, Baekjoon: 1107, ***Bruteforce***](https://www.acmicpc.net/problem/1107)
    - 자바:X
    - 파이썬:X

  - > [SW_IM추천, Baekjoon: 2491](https://www.acmicpc.net/problem/2491)
    - 자바:X
    - 파이썬:O

  - > [SW_IM추천, Baekjoon: 2527](https://www.acmicpc.net/problem/2527)
    - 자바:X
    - 파이썬:X

- 230206:
  - > [Class3, Baekjoon: 9019, ***BFS***](https://www.acmicpc.net/problem/9019)
    - 자바:X
    - 파이썬:O, 백준에서 파이썬으로 들어가면 시간초과, pypy로 하면 통과
    - 이런 경우가 종종 있다고 한다. 파이썬의 경우 bidirectional BFS를 하면 더 낫다고 한다.


