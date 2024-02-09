class LimitedQueue:

    def __init__(self, max_n):
        self.max_n = max_n
        self.queue = [None] * self.max_n
        self.head = 0  # Голова указывает на индекс 0
        self.tail = 0  # Хвост указывает на индекс 0
        self.size = 0  # При создании очередь пуста, её длина - 0

    def is_empty(self):
        return self.size == 0
  
    def push(self, value):
        if self.queue[self.tail] is not None:
            self.head = (self.head + 1) % self.max_n
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.max_n
        if self.size < self.max_n:
            self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        value = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return value

# Начинаем проверку! Создаём очередь с ограничением 8 элементов:
q = LimitedQueue(8) 
# q.push(1)  # Добавляем один элемент.
# print('Очередь с одним элементом:', q.queue)
# print('Длина очереди с одним элементом:', q.size)
# Добавляем ещё три элемента:
for i in range(15):
    q.push(i)
    print(f'q.queue = {q.queue} / q.tail = {q.tail} / q.head = {q.head} / q.size = {q.size}')

print(f'\n\n')

for i in range(15):
    q.pop()
    print(f'q.queue = {q.queue} / q.tail = {q.tail} / q.head = {q.head} / q.size = {q.size}')

# q.push(-1)
# print(f'q.tail = {q.tail} / q.head = {q.head}')
# q.push(0)
# print(f'q.tail = {q.tail} / q.head = {q.head}')
# q.push(11)
# print(f'q.tail = {q.tail} / q.head = {q.head}')
# print('Очередь с четырьмя элементами:', q.queue)
# print('Длина очереди с четырьмя элементами:',q.size)
# print(f'q.tail = {q.tail} / q.head = {q.head}')