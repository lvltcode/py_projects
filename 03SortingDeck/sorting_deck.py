#!/usr/bin/env python3
import argparse


def check_arguments():
    parser = argparse.ArgumentParser(description='Soring Deck')
    parser.add_argument('--algo', help='specify which algorithm to use for'
                        + 'collection among [bubble|insert|quick|merge],'
                        + 'default bubble', default="bubble")
    parser.add_argument('--gui', action='store_true',
                        help='visualise the algorithm in GUI mode')
    parser.add_argument('integers', metavar='N', nargs='+', type=int,
                        help='an integer for the list to sort')
    return parser.parse_args()


# return the same collection ordered by ascending
def bubble_sort(collection):
    length = len(collection)
    for i in range(length-1):
        swapped = False
        # index of last unsorted element -1
        for j in range(length-1-i):
            # swap if left element greater than right element
            if collection[j] > collection[j+1]:
                swapped = True
                collection[j], collection[j+1] = collection[j+1], collection[j]
                for pos in range(len(collection)):
                    if pos == len(collection) - 1:
                        print(collection[pos])
                    else:
                        print(collection[pos], end=' ')
        # Stop iteration if the collection is sorted.
        if not swapped:
            break
    return collection


# return the same collection ordered by ascending
def insertion_sort(collection):
    # mark first element as sorted
    for index in range(1, len(collection)):
        # check from left to right unsorted elements
        # if current element > the next-right element
        check = False
        while index > 0 and collection[index - 1] > collection[index]:
            # swap to the right if element > marked-element
            # create correct position and shift the unsorted element
            collection[index], collection[index - 1] = collection[
                index - 1], collection[index]
            # return new index - advance the marker to the right one element
            index -= 1
            check = True
        if check:
            for pos in range(len(collection)):
                if pos == len(collection) - 1:
                    print(collection[pos])
                else:
                    print(collection[pos], end=' ')
    return collection


def partition(collection, low, high):
    # low  --> Starting index
    # high  --> Ending index
    # index of smaller element
    i = low
    # takes last element as pivot
    pivot = collection[high]     # pivot
    print('P:', pivot)
    for j in range(low, high):
        # compare current element to pivot
        if collection[j] <= pivot:
            # increment index of smaller element
            # places all smaller (smaller than pivot) to left of pivot
            # and all greater elements to right of pivot
            collection[i], collection[j] = collection[j], collection[i]
            i = i+1
    collection[i], collection[high] = collection[high], collection[i]
    for pos in range(len(collection)):
        if pos == len(collection) - 1:
            print(collection[pos])
        else:
            print(collection[pos], end=' ')
    return i

# main function do quick sort
def quick_sort_helper(collection, low, high):
    if low < high:
        check = True
        # p_i is partitioning index, collection[p] is now
        # at right place
        p_i = partition(collection, low, high)
        # Separately sort elements before
        # partition and after partition
        quick_sort_helper(collection, low, p_i - 1)
        quick_sort_helper(collection, p_i + 1, high)


def quick_sort(collection):
    quick_sort_helper(collection, 0, len(collection) - 1)


def merge_sort(collection):
    length = len(collection)
	#Divide input array in two halves
    if length > 1:
        midpoint = length // 2
		# Recursively calls itself to divine the array till the size become one
		# and sorted
        left_half = merge_sort(collection[:midpoint])
        right_half = merge_sort(collection[midpoint:])
        i = 0 # Initial index of first subarray 
        j = 0 # Initial index of second subarray
        k = 0 # Initial index of merged subarray 
		# i is for left index and j is right index of the sub-array of arr to be sorted
        left_length = len(left_half)
        right_length = len(right_half)
		# comparison of elements
		# Merge the temp arrays back into the full-array
        while i < left_length and j < right_length:
            if left_half[i] < right_half[j]:
                collection[k] = left_half[i]
                i += 1
            else:
                collection[k] = right_half[j]
                j += 1
            k += 1
		# Copy the remaining elements of Left, if there are any
        while i < left_length:
            collection[k] = left_half[i]
            i += 1
            k += 1
		# Copy the remaining elements of Rỉght, if there are any
        while j < right_length:
            collection[k] = right_half[j]
            j += 1
            k += 1
        for pos in range(len(collection)):
            if pos == len(collection) - 1:
                print(collection[pos])
            else:
                print(collection[pos], end=' ')
    return collection


if __name__ == '__main__':
    args = check_arguments()
    # if len(args.integers) > 15:
    #     print('Input too large')
    if args.algo == 'bubble':
        bubble_sort(args.integers)
    elif args.algo == 'insert':
        insertion_sort(args.integers)
    elif args.algo == 'quick':
        quick_sort(args.integers)
    elif args.algo == 'merge':
        merge_sort(args.integers)
