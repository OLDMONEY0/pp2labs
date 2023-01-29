#include <iostream>
#include <deque>
using namespace std;
int main(){
    deque <int> Boris;
    deque <int> Nursik;
    int i=0;
    while(i<10){
        int s;
        cin >> s;
        if(i<5){
            Boris.push_back(s);
        }
        else Nursik.push_back(s);
        i++;
    }
    int a = 0;
    while(true){
        if (a >= 1000000){
            cout<<"blin nichya"<<endl;
            return 0 ;
        }
        if(Boris.front() == 0 and Nursik.front() == 9){
            Boris.push_back(Boris.front());
            Boris.push_back(Nursik.front());
            Boris.pop_front();
            Nursik.pop_front();
        }
        else if(Nursik.front() == 0 and Boris. front() == 9){
            Nursik.push_back(Boris.front());
            Nursik.push_back(Nursik.front());
            Nursik.pop_front();
            Boris.pop_front();
        }
        else if(Boris.front() < Nursik.front()){
            Nursik.push_back(Boris.front());
            Nursik.push_back(Nursik.front());
            Boris.pop_front();
            Nursik.pop_front();
        }
        else if(Boris.front() > Nursik.front()){
            Boris.push_back(Boris.front());
            Boris.push_back(Nursik.front());
            Nursik.pop_front();
            Boris.pop_front();
        }
        if (Nursik.empty()){
            cout << "Boris " << a+1<<endl;
            break;
        }
        else if (Boris.empty()){
            cout<<"Nursik " << a+1<<endl;
            break;
        }
        
        a++;
    }
}