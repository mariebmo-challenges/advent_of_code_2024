import re

def A():

    # 1442 too low, 2553 too low
    try:
        with open("./files/day4.txt", "r") as f:
            # find each apperance of regex mul\(\d+\,\d+\)
            total = 0

            data = f.read()

            total = findXmas(data)

            print(total)

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except ValueError:
        print("File contains non-integer values.")
    except Exception as e:
        print(f"An error occurred: {e}")

def findXmas(data):

    total = 0

    lines = data.split("\n")

    for line in range(len(lines)):
        for row in range(len(lines[line])):

            currentChar = lines[line][row]
            if(currentChar == "X"):
                # horizontal
                if(row + 3 < len(lines[line])):
                    if(currentChar == "X" and lines[line][row+1] == "M" and lines[line][row+2] == "A" and lines[line][row+3] == "S"):
                        print("Found XMAS horizontally starting on line " + str(line) + " row " + str(row))
                        total += 1

                if(row - 3 >= 0):
                    if(currentChar == "X" and lines[line][row-1] == "M" and lines[line][row-2] == "A" and lines[line][row-3] == "S"):
                        print("Found XMAS horizontally starting on line " + str(line) + " row " + str(row))
                        total += 1

                # vertical
                if (line + 3 < len(lines)):
                    if (currentChar == "X" and lines[line + 1][row] == "M" and lines[line + 2][row] == "A" and lines[line + 3][row] == "S"):
                        print("Found XMAS vertically starting on line " + str(line) + " row " + str(row))
                        total += 1
                if(line - 3 >= 0):
                    if(currentChar == "X" and lines[line - 1][row] == "M" and lines[line - 2][row] == "A" and lines[line - 3][row] == "S"):
                        print("Found XMAS vertically starting on line " + str(line) + " row " + str(row))
                        total += 1
                
                # diagonal
                if (line + 3 < len(lines) and row + 3 < len(lines[line])):
                    if (currentChar == "X" and lines[line + 1][row + 1] == "M" and lines[line + 2][row + 2] == "A" and lines[line + 3][row + 3] == "S"):
                        print("Found XMAS diagonally starting on line " + str(line) + " row " + str(row))
                        total += 1

                if (line - 3 >= 0 and row - 3 >= 0):
                    if (currentChar == "X" and lines[line - 1][row - 1] == "M" and lines[line - 2][row - 2] == "A" and lines[line - 3][row - 3] == "S"):
                        print("Found XMAS diagonally starting on line " + str(line) + " row " + str(row))
                        total += 1

                if (line + 3 < len(lines) and row - 3 >= 0):
                    if (currentChar == "X" and lines[line + 1][row - 1] == "M" and lines[line + 2][row - 2] == "A" and lines[line + 3][row - 3] == "S"):
                        print("Found XMAS diagonally starting on line " + str(line) + " row " + str(row))
                        total += 1
                
                if (line - 3 >= 0 and row + 3 < len(lines[line])):
                    if (currentChar == "X" and lines[line - 1][row + 1] == "M" and lines[line - 2][row + 2] == "A" and lines[line - 3][row + 3] == "S"):
                        print("Found XMAS diagonally starting on line " + str(line) + " row " + str(row))
                        total += 1
  
    return total

# A()

def B():
    try:
        with open("./files/day4.txt", "r") as f:
            # find each apperance of regex mul\(\d+\,\d+\)
            total = 0

            data = f.read()

            total = findMasInX(data)

            print(total)

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except ValueError:
        print("File contains non-integer values.")
    except Exception as e:
        print(f"An error occurred: {e}")

def findMasInX(data):

    total = 0

    lines = data.split("\n")

    for line in range(len(lines)):
        for row in range(len(lines[line])):

            currentChar = lines[line][row]
            if(currentChar == "A"):

                if (line + 1 < len(lines) and row + 1 < len(lines[line]) and line - 1 >= 0 and row - 1 >= 0):
                    upperLeft = lines[line - 1][row - 1]
                    upperRight = lines[line - 1][row + 1]
                    lowerLeft = lines[line + 1][row - 1]
                    lowerRight = lines[line + 1][row + 1]
                    
                    if(upperLeft == "M" and upperRight == "M" and lowerLeft == "S" and lowerRight == "S"):
                        print("Found MAS in X starting on line " + str(line) + " row " + str(row))
                        total += 1
                    
                    if(upperLeft == "S" and upperRight == "S" and lowerLeft == "M" and lowerRight == "M"):
                        print("Found MAS in X starting on line " + str(line) + " row " + str(row))
                        total += 1

                    if(upperLeft == "M" and upperRight == "S" and lowerRight == "S" and lowerLeft == "M"):
                        print("Found MAS in X starting on line " + str(line) + " row " + str(row))
                        total += 1

                    if(upperLeft == "S" and upperRight == "M" and lowerRight == "M" and lowerLeft == "S"):
                        print("Found MAS in X starting on line " + str(line) + " row " + str(row))
                        total += 1
                    
    return total
                
B()