# Добавьте новую функцию в main.py
def multiply_numbers(a, b):
    """
    Умножает два числа
    
    Args:
        a (int): Первое число
        b (int): Второе число
        
    Returns:
        int: Произведение a и b
    """
    return a * b

# Добавьте вызов новой функции
if __name__ == "__main__":
    print(hello_world())
    print(f"2 + 3 = {add_numbers(2, 3)}")
    print(f"2 * 3 = {multiply_numbers(2, 3)}")  # Новая строка