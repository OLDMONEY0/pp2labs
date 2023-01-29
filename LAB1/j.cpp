#include<iostream>
#include<deque>

using namespace std;

int main()
{
    deque <int> deq;
    char belgi; 
    while(cin >> belgi){
        if(belgi== '+'){
            int san; cin >> san;
            deq.push_front(san);
        }
        else if(belgi== '-'){
            int san; cin >> san;
            deq.push_back(san);
        }
        else if(belgi == '*'){
            
            if(deq.size() >= 2){
                cout << deq.front() + deq.back() << endl;
                deq.pop_front();
                deq.pop_back();
            }
            else if (deq.size()==1){
                cout << deq.front() * 2<<endl;
                deq.pop_front();
            }
            else cout << "error" << endl;
        }
        else if(belgi == '!'){
            return 0;
        }
    }
}

