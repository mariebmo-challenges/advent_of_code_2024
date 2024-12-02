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
    