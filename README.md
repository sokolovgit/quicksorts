# Quicksort Variations in Python

This repository contains implementations of different variations of the Quicksort algorithm in Python. The variations include:

1. Standard Quicksort
2. Median of Three Quicksort
3. Multi-Pivot Quicksort

## Standard Quicksort

The standard Quicksort algorithm is implemented in the `quick_sort.py` file. It uses the last element as the pivot and partitions the array around the pivot.

## Median of Three Quicksort

The Median of Three Quicksort algorithm is implemented in the `median_of_three_quick_sort.py` file. It uses the median of the first, middle, and last elements as the pivot.

## Multi-Pivot Quicksort

The Multi-Pivot Quicksort algorithm is implemented in the `multi_pivot_quick_sort.py` file. It uses three pivots and partitions the array around these pivots.

## Usage

To use these implementations, simply import the required function from the respective file and call it with the array to be sorted and the start and end indices as arguments. For example:

```python
from quick_sort import quick_sort

arr = [3, 7, 8, 5, 2, 1, 9, 5, 4]
quick_sort(arr, 0, len(arr) - 1)
print(arr)  # Output: [1, 2, 3, 4, 5, 5, 7, 8, 9]