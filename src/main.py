"""
Главный модуль проекта
"""

def hello_world():
    """
    Функция для приветствия
    
    Returns:
        str: Приветственное сообщение
    """
    return "Hello, World!"

def add_numbers(a, b):
    """
    Складывает два числа
    
    Args:
        a (int): Первое число
        b (int): Второе число
        
    Returns:
        int: Сумма a и b
    """
    return a + b

if __name__ == "__main__":
    print(hello_world())
    print(f"2 + 3 = {add_numbers(2, 3)}")