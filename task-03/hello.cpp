#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int n;
    bool is_prime = true;

    cout << "Enter a positive integer: ";
    cin >> n;

    if (n <= 1) {
        is_prime = false;
    } else {
        for (int i = 2; i <= sqrt(n); i++) {
            if (n % i == 0) {
                is_prime = false;
                break;
            }
        }
    }

    if (is_prime) {
        cout << n << " is a prime number" << endl;
    } else {
        cout << n << " is not a prime number" << endl;
    }

    return 0;
}

