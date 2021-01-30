while True:
    num1 = int(input('Type first number:'))
    num2 = int(input('Type second number:'))

    product = num1 * num2
    quotient = num1 / num2
    sum = num1 + num2
    difference = num1 - num2

    print('The PRODUCT of'+' '+str(num1)+' '+'and'+' '+str(num2)+' '+'is'+' '+str(product))
    print('The QUOTIENT of'+' '+str(num1)+' '+'and'+' '+str(num2)+' '+'is'+' '+str(quotient))
    print('The SUM of'+' '+str(num1)+' '+'and'+' '+str(num2)+' '+'is'+' '+str(sum))
    print('The DIFFERENCE of'+' '+str(num1)+' '+'and'+' '+str(num2)+' '+'is'+' '+str(difference))
    question = input('Do you want to input again?Y/N:')
    if question == 'Y' or question == 'y': pass
    else:
        break
