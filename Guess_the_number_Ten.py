import random
lower_lim = 1
upper_lim = 100
secret_num = random.randint(lower_lim, upper_lim)
print(f"Угадай число от {lower_lim} до {upper_lim}: ")
while True:
    tries = 0
    guess = None
    while guess != secret_num:
        tries += 1
        guess = int(input())
        if guess < secret_num:
            print(f"Мало")
            lower_lim = guess + 1
        elif secret_num < guess:
            print(f"много")
            upper_lim = guess - 1
        else:
            print('Молодец, угадал! Это число ', secret_num, 'Количество попыток: ', tries)
            lower_lim = 1
            upper_lim = 100
            secret_num = random.randint(lower_lim, upper_lim)
            print(f"Угадай число от {lower_lim} до {upper_lim}: ")