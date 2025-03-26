class ListComprehensions:

    def task_1(self) -> dict[int, int]:
        """Returns a dictionary of {n: n**2} for all odd numbers from 1 to 10."""
        return {
            n: n**2
            for n in range(1,11)
            if n % 2 != 0
        }
    
    def task_2(self) -> list[tuple[int, int]]:
        """Returns a list of tuples for all possible coordinates where x and y are between 0 and 2."""
        return [(x, y) for x in range(3) for y in range(3)]
    
    def task_3(self) -> set[str]:
        """Returns a set with all unique vowels in 'comprehension.'"""
        word: str = 'comprehension'
        vowels: set[str] = {'a', 'e', 'i', 'o', 'u'}
        return {letter for letter in word.lower() if letter in vowels}
    
    def task_4(self) -> list[int]:
        """Returns a list of all even numbers from 1 to 20."""
        return [number for number in range(1, 21) if number % 2 == 0]


ch = ListComprehensions()
print(ch.task_1())
print(ch.task_2())
print(ch.task_3())
print(ch.task_4())

