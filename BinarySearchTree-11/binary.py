def naive_search(l,target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search(l,target,low=None,high=None):
    if low is None:
        low=0
    if high is None:
        high = len(l) - 1  # FIXED: Corrected the assignment

    if high<low:
        return -1 
    midpoint = (low+high) // 2
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l,target,low,midpoint-1)
    else:
        return binary_search(l,target, midpoint+1,high)

if __name__ == '__main__':
    user_input = input("Enter a list of numbers separated by spaces: ")
    try:
        l = list(map(int, user_input.strip().split()))
        target = int(input("Enter the target number: "))
        choice = input("Choose search method - (n)aive or (b)inary: ").lower()

        if choice == 'n':
            print("Naive Search Result:", naive_search(l, target))
        elif choice == 'b':
            l.sort()  # Make sure list is sorted for binary search
            print("Binary Search Result:", binary_search(l, target))
        else:
            print("Invalid choice. Please select 'n' or 'b'.")
    except ValueError:
        print("Please enter valid integers only.")
    #l=[1,3,5,10,12]
    #target = 10
    #print(naive_search(l,target))
    #print(binary_search(l,target))