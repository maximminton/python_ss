import random 
def guess_the_number(): 
    number_to_guess = random.randint(1, 100) 
    attempts = 7 
    print("Вітаю у грі 'Вгадай число'!") 
    print(f"Я загадав число від 1 до 100. У тебе {attempts} спроб, щоб його відгадати.") 
    for attempt in range(1, attempts + 1): 
        user_input = input(f"Спроба {attempt}: Введіть ваше число: ") 
        if not user_input.isdigit(): 
            print("Ви помилково ввели букви, введіть ціле число.") 
            continue 
        guess = int(user_input) 
        if guess < number_to_guess: 
            print("Занадто маленьке!") 
        elif guess > number_to_guess: 
              print("Занадто велике!") 
        else: 
            print(f"Вітаю! Ви вгадали число {number_to_guess}!")
            return 
    print(f"Ви використали всі {attempts} спроб. Загадане число було {number_to_guess}. Гра закінчена.") 
if __name__ == "__main__": guess_the_number()
