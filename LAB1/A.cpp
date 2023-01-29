#include <iostream>
#include <deque>

using namespace std;

int main()
{
    int t; cin >> t;
    while(t--){
        int n; cin >> n;
        deque <int> dq;
        dq.push_front(n);   
        for(int i = n- 1; i > 0;i--){
            dq.push_front(i);
            int j = i;
            while(j > 0){
                dq.push_front(dq.back());
                dq.pop_back();
                j--;
            }
        }

        for (auto i : dq)cout << i << " ";
        cout << endl;
    }
}
