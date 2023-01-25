from random import randint

chars_num_simbol = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%^&*_+/"
pass_len = 16
password = [chars_num_simbol[randint(0, len(chars_num_simbol)-1)] for i in range(pass_len)]
print(f"Password: {''.join(password)}")