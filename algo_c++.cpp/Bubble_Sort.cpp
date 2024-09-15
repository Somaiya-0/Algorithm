#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    vector<int> a;

    // Input the number of elements
    cout << "Enter range: ";
    cin >> n;

    // Input elements into the vector
    cout << "Enter " << n << " numbers: ";
    for (int j = 0; j < n; ++j) {
        int b;
        cin >> b;
        a.push_back(b);
    }

    // Print elements before sorting
    cout << "Before sorting: ";
    for (int num : a) {
        cout << num << " ";
    }
    cout << endl;

    // Bubble Sort algorithm
    for (int i = 0; i < n - 1; ++i) {
        for (int j = 0; j < n - i - 1; ++j) {
            if (a[j] > a[j + 1]) {
                // Swap elements
                int temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
            }
        }
    }

    // Print elements after sorting
    cout << "Sorted: ";
    for (int num : a) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
