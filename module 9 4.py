from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x[0] == y[0], first, second)))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='UTF-8') as file:
            for line in data_set:
                file.write(str(line))
                file.write('\n')
                print(line)

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        words = choice(self.words)
        return words


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
