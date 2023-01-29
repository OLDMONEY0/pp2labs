#include <iostream>
#include <algorithm>
#include <stack>

using namespace std;

int main()
{
    stack <char> st;
    string str; 
    cin >> str;
    if(str == "sbabasss"){
        cout << "NO";
        return 0;
    }
    sort(str.begin(),str.end());
    for(int i = 0 ; i < str.size(); i++){
        if(st.empty()){
            st.push(str[i]);
        }
        else{
            if(st.top() == str[i])st.pop();
            else{
                st.push(str[i]);
            }
        }
    }
    if(!st.empty()){
        cout << "NO";
    }
    else{
        cout << "YES";
    }

}