def main():
    numbers = [4,6,1,0,7,9,2,5,8,3]
    number = 0
    print(linear_search(numbers,number))
    print(binary_search(numbers,number))

def linear_search(list, n):
    for i in range(len(list)):
        if list[i] == n:
            return f'found {list[i]} at postition {i}'

def binary_search(list,n):
    #uses sorted lists
    #unfortunately u HAVE to sort the list/array

    list = sorted(list)
    lowest = 0
    highest = len(list)-1

    while lowest <= highest:
        mid = lowest+ (highest-lowest)//2

        if list[mid] == n:
            return f'found {n} at position {mid} (when sorted).'

        elif list[mid]<n:
            lowest=mid+1
        
        else:
            highest = mid-1
        #return list

if __name__ == '__main__':
    main()