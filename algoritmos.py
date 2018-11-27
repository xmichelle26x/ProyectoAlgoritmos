# Referencias:
# http://interactivepython.org/courselib/static/pythonds/SortSearch/TheQuickSort.html

import time
from random import randint
import xlsxwriter

def insertionSort(alist):
   for index in range(1,len(alist)):
     currentvalue = alist[index]
     position = index
     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1
     alist[position]=currentvalue




def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)





tiempo = time.time()

lista = [10, 12, 4, 1, 7, 50, 24, 14, 34, 2, 5, 26, 18, 20, 3, 47, 5, 23, 37, 9, 44, 32, 17, 31, 49, 13]

quickSort(lista)

print(time.time() - tiempo)
print("segundos")

