user_string = input()

user_var = user_string[0]

actual_user_string = user_string[1:]

num = actual_user_string.count(user_var)

if num == 0 or num > 1:
    
    print(f"{num} {user_var}'s")
    
else:
    
    print(f"{num} {user_var}")