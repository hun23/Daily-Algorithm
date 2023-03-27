#include <iostream>

using namespace std;

int n;
int graph[100][100];
int result[100][100];

int dfs(int s, int g) {
    if (graph[s][g] != 0) {
        for (int i = 0; i < n; i++) {
            if (!result[i][g] && !result[i][g]) {
                result[i][g] = 1;
                dfs(i, g);
            }
            if (!result[s][i] && !result[s][i]) {
                result[s][i] = 1;
                dfs(s, i);
            }
        }
    }
    return 0;
}

int main() {
    cin >> n;
    graph[100][100] = {};
    result[100][100] = {};
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> graph[i][j];
            graph[j][i] = graph[i][j];
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (!result[i][j]) dfs(i, j);
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << result[i][j] << " ";
        }
        cout << "\n";
    }
    
    cin.get();
    return 0;
}