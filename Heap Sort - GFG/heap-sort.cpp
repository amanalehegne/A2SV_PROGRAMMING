//{ Driver Code Starts
// C++ program for implementation of Heap Sort
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// The functions should be written in a way that array become sorted 
// in increasing order when heapSort() is called.

class Solution
{
public:
    void heapify(int arr[], int size, int idx)
    {
        while (idx > 0) {
            int parent = (idx - 1) / 2;
            if (arr[parent] > arr[idx])
                break;
            std::swap(arr[parent], arr[idx]);
            idx = parent;
        }
    }
    
    void heapifyDown(int arr[], int length, int idx)
    {
        while (idx < length) {
            int left = 2 * idx + 1;
            int right = 2 * idx + 2;
            int childIdx = left;
            if (left >= length)
                break;
            if (right < length && arr[right] > arr[left])
                childIdx = right;
            if (arr[childIdx] > arr[idx]) {
                std::swap(arr[idx], arr[childIdx]);
                idx = childIdx;
            }
            else
                break;
        }
    }
    
    void heapSort(int arr[], int size)
    {
        for (int i = 0; i < size; ++i)
            heapify(arr, i, i);
        for (int i = 0; i < size; ++i) {
            int length = size - i - 1;
            std::swap(arr[0], arr[length]);
            heapifyDown(arr, length, 0);
        }
    }
};





//{ Driver Code Starts.

/* Function to print an array */
void printArray(int arr[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

// Driver program to test above functions
int main()
{
    int arr[1000000],n,T,i;
    scanf("%d",&T);
    while(T--){
    scanf("%d",&n);
    for(i=0;i<n;i++)
      scanf("%d",&arr[i]);
    Solution ob;
    ob.heapSort(arr, n);
    printArray(arr, n);
    }
    return 0;
}

// } Driver Code Ends