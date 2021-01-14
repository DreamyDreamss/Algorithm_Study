#include <iostream>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

int main() {
	
	int n, m;
	cin >> n >> m;
	vector<vector<int>> graph;
	graph.resize(n+1);
	int indegree[33000] = { 0 };

	for (int i = 0; i < m; i++) {
		int st, dst;
		cin >> st >> dst;
		graph[st].push_back(dst);
		indegree[dst]++;
	}

	
	queue<int> q;
	for (int i = 1; i <= n; i++) {
		if (indegree[i] == 0) q.push(i);
	}

	while (!q.empty()) {
		int val;
		val = q.front(); q.pop();
		cout << val << " ";
		for (int i = 0; i < graph[val].size(); i++) {

			indegree[graph[val][i]]--;
			if (!indegree[graph[val][i]]) q.push(graph[val][i]);
		}
	}
}