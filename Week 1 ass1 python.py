def reverseArray(arr):
    return arr[::-1]

# --------- Driver Code ---------
if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter the elements: ").split()))
    reversed_arr = reverseArray(arr)
    print("Reversed array:", *reversed_arr)
