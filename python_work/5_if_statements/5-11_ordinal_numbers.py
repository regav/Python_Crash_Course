numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    st_string = "st"
    nd_string = "nd"
    rd_string = "rd"
    th_string = "th"
    if number == 1:
        print(str(number) + st_string)
    elif number == 2:
        print(str(number) + nd_string)
    elif number == 3:
        print(str(number) + rd_string)
    elif number > 3:
        print(str(number) + th_string)