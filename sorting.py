def main():
    numbers = [4,6,1,0,7,9,2,5,8,3]
    print(bubble_sort(numbers))

def bubble_sort(list):
    swap = True
    upper = len(list)
    lower = 0

    #idt we need to compare lower w/ upper cuz even w/out it the code works just fine
    while swap == True and upper > lower:
        swap = False
        for i in range(upper-1):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i]= list[i+1]
                list[i+1] = temp
                swap=True
        upper-=1

    return list

if __name__ == '__main__':
    main()