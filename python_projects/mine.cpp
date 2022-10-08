#include <iostream>
#include <sstream>
#include <conio.h>

using namespace std;

int str_to_int(string MyString){
    istringstream converter(MyString);
    int result;
    converter >> result;
    return result;
}

string input(){
    string numAsString = "";
    char ch = getch();
    while (ch != '\r'){
        numAsString += ch;
        cout << ch;
        ch = getch();
    }

    cout << endl;

    return numAsString;
}

int main(){
    cout << "Hello World!" << endl;
    cout << str_to_int("1352") + 5 << endl;
    string result;
    result = input();
    cout << result << endl;
}