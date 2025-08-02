def dynamic_array_operations():
    arr = []
    while True:
        print("\nDynamic Array Menu:")
        print("1. Append")
        print("2. Insert at index")
        print("3. Delete by value")
        print("4. Display")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            val = int(input("Enter value to append: "))
            arr.append(val)
        elif choice == '2':
            idx = int(input("Enter index: "))
            val = int(input("Enter value: "))
            arr.insert(idx, val)
        elif choice == '3':
            val = int(input("Enter value to delete: "))
            if val in arr:
                arr.remove(val)
            else:
                print("Value not found!")
        elif choice == '4':
            print("Array:", arr)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

# Run function
dynamic_array_operations()
