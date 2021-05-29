
def dolla_dolla_bills(any_number) -> str:
    numbers = list(str(round(abs(any_number), 2)))
    numbers.reverse()
    
    stringed_dollars = []

    for index, number in enumerate(numbers, start=1):
        if index % 3 == 0:
            if number == ".":
                stringed_dollars.append(".")
            else:
                stringed_dollars.append(number)
                stringed_dollars.append(",")
        else:
            stringed_dollars.append(number)
    
    if stringed_dollars[-1] == ",":
        stringed_dollars.pop()
    
    stringed_dollars.reverse()
    
    dollars = "{prefix}{amount}{postfix}"

    prefix = "$"

    if any_number < 0:
        prefix = "-$"

    postfix = ""

    if type(any_number) != float:
        postfix = ".00"

    dollars = dollars.format(
        prefix=prefix,
        amount="".join(stringed_dollars),
        postfix=postfix
    )
    
    return dollars


if __name__ == "__main__":
    print(dolla_dolla_bills(-314159.2653))
