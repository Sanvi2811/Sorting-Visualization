
import sys
import time
import matplotlib.pyplot as plt
import numpy as np

# Defining text for animated text writer

def text(t):
  for char in t:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
    
text("Choose the sorting you would like to visualize via animation: ")
print()
print("A. Bubble Sort")
print("B. Selection Sort")
print("C. Insertion Sort")
print("D. QuickSort")
answer =input("")
ans = answer.capitalize().strip(" ")



    
 # Creating a list   

amount = 15
lst = np.random.randint(0, 100, amount)
x = np.arange(0, amount, 1)
n = len(lst)

#plot.ion - Turing on the interactive mode in the graph. It will enable the interaction between the bars (Sorting)
plt.ion() 
fig, ax = plt.subplots()  # It is used to draw bars


if (ans == "A"):
  text("Bubble Sorting")
# Bubble Sorting Algorithm

  for i in range(n-1):
    for j in range(n- i - 1):
        ax.clear() 
        ax.bar(x, lst)
        plt.pause(1)
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

  plt.ioff()  # Turning off the interaction mode
  plt.show() # Showing the animation

# Code for animation of Selection Sort
elif (ans == "B"):
  text("Selection Sorting")
  for i in range(n):
    minindex = i
    for j in range(i + 1, n):
        if lst[j] < lst[minindex]:
            minindex = j
    lst[i], lst[minindex] = lst[minindex], lst[i]
    ax.clear()
    ax.bar(x, lst)
    plt.pause(1)

  plt.ioff() 
  plt.show()

# code for animation of Insertion Sort

elif (ans == "C"):
  text("Insertion Sorting")
  for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
        ax.clear()
        ax.bar(x, lst)
        plt.pause(1)

  plt.ioff() 
  plt.show()
  

elif (ans == "D"):
  text("Quick Sort")
  if len(lst) > 1:
    stack = [(0, len(lst) - 1)]

    while stack:
        start, end = stack.pop()
        pivot = lst[(start + end) // 2]
        low = start
        high = end

        while low <= high:
            while lst[low] < pivot:
                low += 1
            while lst[high] > pivot:
                high -= 1

            if low <= high:
                lst[low], lst[high] = lst[high], lst[low]
                low += 1
                high -= 1

        if start < high:
            stack.append((start, high))
        if low < end:
            stack.append((low, end))
        ax.clear()
        ax.bar(x, lst)
        plt.pause(1)
  plt.ioff() 
  plt.show()      
