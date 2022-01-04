"""
Collection of basic sorting methods.
"""

def bubbleSort(array: list) -> list:
    """
    Sort array using simple bubble sort.
    """
    for i in range(len(array)):
        for j in range(len(array)):
            if array[j] > array[i]:
                array[j], array[i] = array[i], array[j]

def bubbleSortOptimized(array: list) -> list:
    """
    Sort array using optimized bubble sort.
    """
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[j] < array[i]:
                array[j], array[i] = array[i], array[j]

def selectionSort(array: list) -> list:
    """
    Sort array using selection sort.
    """
    for i in range(len(array)):
        mini = i
        for j in range(i, len(array)):
            if array[j] < array[mini]:
                mini = j
        array[i], array[mini] = array[mini], array[i]