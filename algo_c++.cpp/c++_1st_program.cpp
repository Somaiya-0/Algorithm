#include<iostream>
#include<vector>
using namespace std;
int main ()
{
    
    // n.push_back(6);
    // char s[] = "Hello World!";
    // int money;
    // cin>>money;
    // if (money<50)
    // {
    //     for (int i : n) 
    //     {
    //     cout << i << "  ";
    //     }
    //     cout<<endl;
    //     n.pop_back();
    //     for (int i : n) 
    //     {
    //     cout << i << "  ";
    //     }
    //     cout<<"dukkho dukkho sob dukkho"<<" "<<endl<<s;
    // }

    int size,sum=0,even_sum=0,odd_sum=0;
    vector<int> n={};
    cin>>size;
    for (int i=0;i<=size;i++) 
        {
        cin>> i ;
        n.push_back(i);

        }
    for (int i : n) 
       {
        cout << i << "  ";
        }
    for (int i =0;i<size;i++) 
        {  
            sum+=n[i];
            if(i%2==0){
                even_sum+=n[i];
            }
            else{
                odd_sum+=n[i];
            }

          
        }
        cout<<endl<<"Sum of elements : "<<sum<<endl<<"Sum of even index elements: "<<even_sum<<endl<<"Sum of odd index elements : "<<odd_sum;
        if(even_sum<odd_sum){
            cout<<endl<<"Sum of even index elements is bigger";
        }
        else{
            cout<<endl<<"Sum of odd index elements is bigger";
        }

    }
