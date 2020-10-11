#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main(){
    
    int n,pd,indegree[1001]={0};
    vector<vector<int>> info;
    vector<int> result;
    cin >> n>> pd;
    info.resize(n+1);
    
    for(int i=0;i<pd;i++){
        int t;
        cin >> t;
        int prev;
        cin >> prev;
        for(int j=1;j<t;j++){
            int temp;
            cin >> temp;
            info[prev].push_back(temp);
            indegree[temp]++;
            prev= temp;
        }
    }
       
    
    queue<int> q;
    
    for(int i=1;i<=n;i++) if(indegree[i]==0)q.push(i);
    
    
    while(!q.empty()){
        int val;
        val =q.front();
        result.push_back(val);
        //cout << val << '\n';
        q.pop();
        for(int i=0;i<info[val].size();i++){
            indegree[info[val][i]]--;
            if(!indegree[info[val][i]]) q.push(info[val][i]);
            
        }
    }
    for(int i=1;i<=n;i++) {if(indegree[i]!=0) {
       cout << "0"; return 0;
    }}
    
        for(int i=0;i<result.size();i++){
            cout << result[i] << '\n';
        }
    return 0;
}
