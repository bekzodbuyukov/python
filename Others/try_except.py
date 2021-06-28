# Exercising from: https://www.w3schools.com/python/python_try_except.asp

# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code, if no errors were raised.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.


def main() -> None:
    some_text = 'Seems, today we will have rain.'

    try:
        print(some_text)
    except NameError:
        print('Seems, you have not declared \'some_text\' variable.')
    else:
        print('No errors were raised.')
    finally:
        print('All Done!')
    

if __name__ == '__main__':
    main()
