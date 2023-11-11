user_int = input("Please give your positive integer and I will find you all factors of it: ")
trans_user_int = int(user_int)

factor = 0

while factor <= trans_user_int:
    factor += 1
    if trans_user_int % factor == 0:
        print(f"{factor} is a factor of {trans_user_int}")
    
