#include<iostream>

using namespace std;

int main(){
    int prime;
    cin >> prime;
    if(prime == 1){
        cout<<3;
        return 0;
    }
    int nth = 2;
    int nth2 = 1;
    int n = 5;
    bool r = true;
    bool r2 = true;
    while(nth2!=prime){
        for(int i = 2;i <n/2 + 1;i++){ 
            if( n % i == 0){
                r = false;
            }
        }
        if( r == true){
            nth++;
            for(int i = 2;i < nth / 2 + 1; i++){
                if(nth%i == 0){
                    r2 =false;
                }
            }
            if(r2 == true){
                nth2++;
                if(nth2 == prime){
                    cout<<n;
                }
            }else{
                r2 = true;
            }
        }else{
            r = true;
        }
        n += 2;
        
    }
    return 0;
}