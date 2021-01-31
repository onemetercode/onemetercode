print('<<'+'='*57+'>>')
print('<<'+'='*25+'CHOICES'+'='*25+'>>')
print('<<'+'='*57+'>>')

print("""1 - While Loop - Controlled
2 - While Loop - Event Controlled
3 - For Loop - Specific Output
4 - For Loop - Even and Odd
5 - String formatting  
        """)
choice = int(input('Enter your choice: '))
while True:
    if choice == 1:
        print('Welcome to "While Loop - Controlled"')
        start = int(input('Enter where to start: '))
        end = int(input('Enter where to end: '))
        increment = int(input('Enter the increment: '))
        for fchoice in range(start,end,increment):
            if fchoice%2:
                print(fchoice,' : ODD number')
            else:
                print(fchoice,' : EVEN number')
        askuser = input('Do you want to continue your session?:Y/N ')
        if askuser == 'Y' or askuser == 'y' or askuser == 'Yes' or askuser == 'yEs' or askuser == 'yeS' or askuser == 'YeS' or askuser == 'yes' or askuser == 'YES':
            pass
        elif askuser == 'N' or askuser == 'n' or askuser == 'No' or askuser == 'nO':
            break
        elif askuser != 'Y' or askuser != 'y' or askuser != 'Yes' or askuser != 'yEs' or askuser != 'yeS' or askuser != 'YeS' or askuser != 'yes' or askuser != 'YES':
            print('"Invalid input"')
            break
        elif askuser != 'N' or askuser != 'n' or askuser != 'No' or askuser != 'nO':
            print('"Invalid input"')
            break
    elif choice == 2:
        print('Welcome to "While Loop - Event Controlled!!"')
        start = int(input('Enter where to start: '))
        end = int(input('Enter where to end: '))
        product = start*end
        divide = start/end
        sum = start+end
        subtract = start-end
        exponent = start**end
        modulo = start%end
        print('The PRODUCT of {} and {} is {}'.format(str(start), str(end), str(product)))
        print('The QUOTIENT of {} and {} is {}'.format(str(start), str(end), str(divide)))
        print('The SUM of {} and {} is {}'.format(str(start), str(end), str(sum)))
        print('The DIFFERENCE of {} and {} is {}'.format(str(start), str(end), str(subtract)))
        print('The EXPONENTIAL of {} and {} is {}'.format(str(start), str(end), str(exponent)))
        print('The MODULO of {} and {} is {}'.format(str(start), str(end), str(modulo)))
        askuser = input('Do you want to continue your session?:Y/N ')
        if askuser == 'Y' or askuser == 'y' or askuser == 'Yes' or askuser == 'yEs' or askuser == 'yeS' or askuser == 'YeS' or askuser == 'yes' or askuser == 'YES':
            pass
        elif askuser != 'Y' or askuser != 'y' or askuser != 'Yes' or askuser != 'yEs' or askuser != 'yeS' or askuser != 'YeS' or askuser != 'yes' or askuser != 'YES':
            print('"Invalid input"')
            break
        elif askuser != 'N' or askuser != 'n' or askuser != 'No' or askuser != 'nO':
            print('"Invalid input"')
            break
    elif choice == 3:
        print('Welcome to "For Loop - Specific Output"')
        for number in range(1,11):
            print('This is line number {}'.format(number))
        break
    elif choice == 4:
        print('Welcome to "For Loop - Even and Odd"')
        for oddevennumber in range(1,31):
            if oddevennumber%2:
                print(oddevennumber,' : ODD number')
            else:
                print(oddevennumber,' : EVEN number')
        break
    elif choice == 5:
        print('Welcome to "String formatting"')
        fname = input('Enter your first name: ')
        lname = input('Enter your last name: ')
        age = int(input('Enter your age: '))
        address = input('Enter your address: ')

        print('<<'+'='*50+'|'+'='*17+'|'+'='*50+'>>')
        print('<<'+'='*50+'Welcome to my Story'+'='*50+'>>')
        print('<' + '=' * 121 + '>')
        string_to_center = 'Hi {} {} you are already {} years already and currently living in {}.'.format(fname,lname,str(age),(address))
        centered_string = string_to_center.center(119)
        print('||'+centered_string+'||')
        print('<<'+'='*119+'>>')
        askuser = input('Do you want to continue your session?:Y/N ')
        if askuser == 'Y' or askuser == 'y' or askuser == 'Yes' or askuser == 'yEs' or askuser == 'yeS' or askuser == 'YeS' or askuser == 'yes' or askuser == 'YES':
            pass
        elif askuser != 'Y' or askuser != 'y' or askuser != 'Yes' or askuser != 'yEs' or askuser != 'yeS' or askuser != 'YeS' or askuser != 'yes' or askuser != 'YES':
            print('"Invalid input"')
            break
        elif askuser != 'N' or askuser != 'n' or askuser != 'No' or askuser != 'nO':
            print('"Invalid input"')
            break



