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

def B():
    try:
        with open("./files/day3.txt", "r") as f:
            results = re.findall(r"(mul\(\d+\,\d+\))|(do\(\))|(don't\(\))", f.read())
            shouldDo = True
            total = 0

            # 2463154 too low

            for result in results:
                if(result[0].startswith("mul") and shouldDo):
                    split = result[0].split(',')
                    firstNum = int(split[0][4:])
                    secondNum = int(split[1][:-1])
                    total += firstNum * secondNum
                elif(result[1].startswith("do")):
                    shouldDo = True
                elif(result[2].startswith("don't")):
                    shouldDo = False

            print(total)

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except ValueError:
        print("File contains non-integer values.")
    except Exception as e:
        print(f"An error occurred: {e}")

B()