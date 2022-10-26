#3141592653589793238462643383279502884197169399375105820974944592
#2718281828459045235360287471352662497757247093699959574966967627

def splittingFunction(firstNum, secondNum):
    if(len(str(firstNum)) < 2 or len(str(secondNum)) < 2):
        return firstNum*secondNum
    else:
        numberOfDigits = max(len(str(firstNum)), len(str(secondNum)))
        firstHalf1 = str(firstNum)[:(numberOfDigits//2)]
        secondHalf1 = str(firstNum)[(numberOfDigits//2):]
        firstHalf2 = str(secondNum)[:(numberOfDigits//2)]
        secondHalf2 = str(secondNum)[(numberOfDigits//2):]
        product1 = int(splittingFunction(int(firstHalf1), int(firstHalf2)))
        product2 = int(splittingFunction(int(secondHalf1), int(secondHalf2)))
        product3 = int(splittingFunction((int(firstHalf1)+int(secondHalf1)), (int(firstHalf2)+int(secondHalf2))))
        product4 = product3 - product2 - product1
        return product1*(10**numberOfDigits) + product2 + product4*(10**(numberOfDigits//2))


number1, number2 = (int(input()), int(input()))
print(splittingFunction(number1, number2))
