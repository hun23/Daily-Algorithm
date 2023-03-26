#include <iostream>

int main(void) {
  int N;
  std::cin >> N;

  int adjList[100][100];
  for (int i=0; i<N; i++) {
    for (int j=0; j<N; j++) {
      std::cin >> adjList[i][j];
    }
  }

  for (int i=0; i<N; i++) {
    for (int j=0; j<N; j++) {
      std::cout << adjList[i][j];
    }
    std::cout << "\n";
  }

}