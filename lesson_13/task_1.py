from random import randint
from sorts import bubbleSort, bubbleSortOptimized, selectionSort

bubbleSortList = [randint(0, 10) for _ in range(10)]
bubbleSortOptList = [randint(0, 10) for _ in range(10)]
selectionSortList = [randint(0, 10) for _ in range(10)]

print('Before sort:')
print('\tBubble sort            \t', bubbleSortList)
print('\tBubble sort (optimized)\t', bubbleSortOptList)
print('\tSelection sort         \t', selectionSortList)

bubbleSort(bubbleSortList)
bubbleSortOptimized(bubbleSortOptList)
selectionSort(selectionSortList)

print('After sort:')
print('\tBubble sort            \t', bubbleSortList)
print('\tBubble sort (optimized)\t', bubbleSortOptList)
print('\tSelection sort         \t', selectionSortList)