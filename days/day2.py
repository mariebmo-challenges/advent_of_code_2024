def A() : 
    try : 
        with open("./files/day2.txt", "r") as f : 
            total = 0
            for line in f : 
                if isAcceptableReport(line) : 
                    total += 1
            print(total)
            
    except FileNotFoundError : 
        print("File not found. Please check the file path.")
    except ValueError : 
        print("File contains non-integer values.")
    except Exception as e : 
        print(f"An error occurred: {e}")

def isAcceptableReport(report) :
    split = report.split()
    
    previousNum = 0
    inc = False
    for i in range(len(split)) : 
        currNum = int(split[i])
        if i == 0 : 
            previousNum = currNum
            continue
        
        if(i == 1) : 
            if currNum > previousNum : 
                inc = True

        if inc :
            if currNum < previousNum : 
                return False
            else :
                if(currNum - previousNum > 3 or currNum - previousNum < 1) : 
                    return False

        else : 
            if currNum > previousNum : 
                return False
            else : 
                if(previousNum - currNum > 3 or previousNum - currNum < 1) : 
                    return False
        
        previousNum = currNum

    return True

A()
    

def B(): 
    try : 
        with open("./files/day2.txt", "r") as f : 

            # wrong: 617, 625, 628, 631, 638, 738

            testData = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
1 1 2 3 4
1 5 6 7 8
8 8 6 4 2
8 8 8 8 8"""
            total = 0
            for line in f: 
                if isAcceptableReportWithDampener(line) : 
                    total += 1
            print(total)
            
    except FileNotFoundError : 
        print("File not found. Please check the file path.")
    except ValueError : 
        print("File contains non-integer values.")
    except Exception as e : 
        print(f"An error occurred: {e}")

def isAcceptableReportWithDampener(line):
    numbers = list((int(x) for x in line.split(" ")))

    if(isAscDesc(numbers)) : 
        errors = 0
        if(abs(numbers[0] - numbers[1]) > 3 or abs(numbers[0] - numbers[1]) < 1) : 
            errors += 1

        if(abs(numbers[len(numbers) - 1] - numbers[len(numbers) - 2]) > 3 or abs(numbers[len(numbers) - 1] - numbers[len(numbers) - 2]) < 1) : 
            errors += 1

        if errors > 1 :
            return False
        
        for i in range(len(numbers) - 1) : 
            diff = abs(numbers[i] - numbers[i + 1])
            if diff > 3 or diff < 1 : 
                return False
        return True
    
    else : 
        newArr = getFormattedArray(numbers)

        if(newArr == False) :
            return False

        for i in range(len(newArr) - 1) : 
            diff = abs(newArr[i] - newArr[i + 1])
            if diff > 3 or diff < 1 : 
                return False
        return True
    
def isAscDesc(numbers) : 
    isAsc = True
    isDesc = True
    twoOfSame = False

    for i in range(len(numbers) - 1) : 
        if numbers[i] > numbers[i + 1] : 
            isAsc = False
        if numbers[i] == numbers[i + 1] :
            twoOfSame = True
    
    for i in range(len(numbers) - 1) : 
        if numbers[i] < numbers[i + 1] : 
            isDesc = False
        if numbers[i] == numbers[i + 1] :
            twoOfSame = True
    
    return (isAsc != isDesc) and twoOfSame == False

def getFormattedArray(numbers):

    for i in range(len(numbers)) : 
        newArr = numbers.copy()
        newArr.remove(newArr[i])
        if(isAscDesc(newArr)) : 
            return newArr

    return False

B()