import random
english_words={
    "hello": "привет",
    "dog": "собака",
    'cat': 'кошка',
     'what': "что"}
print('добро пожаловать')
score = 0
while True:
    word = random.choice(list(english_words.keys()))
    answer = input(f"как переводится слово {word} на русский ")
    if answer.lower() == 'стоп':
        break
    if answer.lower() == english_words[word]:
        print("правильно")
        score += 1
    else:
        print(f'неправильно. правильное слово {english_words[word]}')
print(f"конец игры ты набрал {score} очков(а)")