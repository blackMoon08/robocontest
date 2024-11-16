#include <iostream>
#include <iomanip>
using namespace std;
int main(){

    double n;
    cin >> n;
    double k,f;
    k = n + 273.15;
    f = 1.80 * n + 32.00;
    cout << fixed << setprecision(5) << k << endl;
    cout << fixed << setprecision(5)  << f << endl;

    return 0;
}