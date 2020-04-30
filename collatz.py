
def collatz(number):
    if number%2 == 0:
        value = number//2
        return value
    else:
        value = 3 * number + 1
        return value

print('Enter a number of your choice')
inputNum = int(input())
outputNum = collatz(inputNum)
print(outputNum)

while True:
    if outputNum == 1:
        break
    else:
        outputNum = collatz(outputNum)
        print(outputNum)
        continue
 
