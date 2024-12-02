def A():
    try:
        with open("./files/day1.txt", "r") as f:
            leftList = []
            rightList = []
            distance = 0

            for line in f:
                split = line.split()
                if len(split) != 2:
                    continue  # Skip lines that do not have exactly two elements
                left, right = split
                print(left, right)
                leftList.append(int(left))
                rightList.append(int(right))

        leftList.sort()
        rightList.sort()

        for i in range(len(leftList)):
            distance += abs(leftList[i] - rightList[i])
        
        print(distance)
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except ValueError:
        print("File contains non-integer values.")
    except Exception as e:
        print(f"An error occurred: {e}")

A()