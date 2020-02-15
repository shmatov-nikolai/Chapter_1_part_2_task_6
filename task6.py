# Given an integer. Print its tens digit.

def tens_digit_int(num):
    print(f"Число {num} состоит из: {int(num/10)} десятков" )
    desyatki = num//10
    for i in range(1, desyatki+1):
        print (f"десятки: {i*10}")

tens_digit_int(155)