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

def B():
    try:
        with open("./files/day1.txt", "r") as f:
            amountOfTimesLeft = {}
            amountOfTimesRight = {}

            similarityScore = 0

            for line in f:
                split = line.split()
                if len(split) != 2:
                    continue  # Skip lines that do not have exactly two elements
                left, right = split
                if left in amountOfTimesLeft:
                    amountOfTimesLeft[left] += 1
                else:
                    amountOfTimesLeft[left] = 1

                if right in amountOfTimesRight:
                    amountOfTimesRight[right] += 1
                else:
                    amountOfTimesRight[right] = 1


        ## if 1 is 3  times in left list, and 2 times in right list, the similarity score is (1 * 2) * 3
        for key in amountOfTimesLeft:
            if key in amountOfTimesRight:
                similarityScore += int(key) * amountOfTimesLeft[key] * amountOfTimesRight[key]
        
        print(similarityScore)
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except ValueError:
        print("File contains non-integer values.")
    except Exception as e:
        print(f"An error occurred: {e}")

A()
B()
