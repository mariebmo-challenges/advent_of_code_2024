import re

def A():
    try:
        with open("./files/day3.txt", "r") as f:
            # find each apperance of regex mul\(\d+\,\d+\)
            results = re.findall(r"mul\(\d+\,\d+\)", f.read())
            total = 0

            for result in results:
                split = result.split(',')
                firstNum = int(split[0][4:])
                secondNum = int(split[1][:-1])
                total += firstNum * secondNum
            

            print(total)

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except ValueError:
        print("File contains non-integer values.")
    except Exception as e:
        print(f"An error occurred: {e}")

A()