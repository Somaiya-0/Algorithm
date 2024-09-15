#include<iostream>
#include<vector>
using namespace std;

int main() {
    int size, sum = 0, even_sum = 0, odd_sum = 0;
    vector<int> n;  // Vector to store input integers
    
    // Input the number of elements
    cin >> size;

    // Input elements into the vector
    for (int i = 0; i < size; i++) {
        int num;
        cin >> num;
        n.push_back(num);
    }

    // Print all elements of the vector
    for (int i : n) {
        cout << i << "  ";
    }
    cout << endl;

    // Calculate sums and categorize based on index parity
    for (int i = 0; i < size; i++) {
        sum += n[i];
        if (i % 2 == 0) {
            // Even index
            even_sum += n[i];
        } else {
            // Odd index
            odd_sum += n[i];
        }
    }

    // Output the results
    cout << "Sum of elements: " << sum << endl;
    cout << "Sum of even index elements: " << even_sum << endl;
    cout << "Sum of odd index elements: " << odd_sum << endl;

    // Compare sums and print result
    if (even_sum < odd_sum) {
        cout << "Sum of even index elements is smaller" << endl;
    } else {
        cout << "Sum of odd index elements is smaller" << endl;
    }

    return 0;
}
