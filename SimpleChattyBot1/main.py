def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    remainder3 = int(input())
    remainder5 = int(input())
    remainder7 = int(input())
    age = (remainder3 % 3 * 70 + remainder5 % 5 * 21 + remainder7 % 7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print("Now I will prove to you that I can count to any number you want.")
    number_user = int(input())
    count = 0
    while count <= number_user:
        print(count, "!")
        count += 1


def test():
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    while True:
        answer = int(input())
        if answer == 4:
            print("Completed, have a nice day!")
            break
        else:
            print("Please, try again.")


def end():
    print('Congratulations, have a nice day!')    


greet("Alexey", "2021")
remind_name()
guess_age()
count()
test()
end()
