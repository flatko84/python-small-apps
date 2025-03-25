class ListComprehensions:
    def task_1(self):
        return {
            n: n**2
            for n in range(1,10)
            if n % 2 != 0
        }
    
    def task_2(self):
        return [(x, y) for x in range(3) for y in range(3)]
    
    def task_3(self):
        word = 'comprehension'
        vowels = {'a', 'e', 'i', 'o', 'u'}
        return {letter for letter in word.lower() if letter in vowels}
    
    def task_4(self):
        return [number for number in range(1, 21) if number % 2 == 0]


ch = ListComprehensions()
print(ch.task_4())

