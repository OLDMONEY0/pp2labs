#include <bits/stdc++.h>

using namespace std;

int main()
{
    deque <int> s,k;
    int n; cin >> n;
    for(int i = 0 ; i < n; i++){
        char c; cin >> c;
        if(c == 'S')s.push_back(i);
        else k.push_back(i);
    }
    
    while(true){
        if(s.empty()){
            cout << "KATSURAGI";
            break;
        }
        else if(k.empty()){
            cout << "SAKAYANAGI";
            break;
        }

        if(s.front() > k.front()){
            s.pop_front();
            k.push_back(k.front() + n);
            k.pop_front();
        }
        else if(k.front() > s.front()){
            k.pop_front();
            s.push_back(s.front() + n);
            s.pop_front();
        }
    }
}