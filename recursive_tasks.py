class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_print(s):
    if s == "":
        return
    reverse_print(s[1:])
    print(s[0], end='')

def swap_pairs(head):
    if head is None or head.next is None:
        return head
    new_head = head.next
    head.next = swap_pairs(new_head.next)
    new_head.next = head
    return new_head

def print_list(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    head.next = build_linked_list(values[1:])
    return head

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def climb_stairs(n):
    if n == 0 or n == 1:
        return 1
    return climb_stairs(n - 1) + climb_stairs(n - 2)

def my_pow(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / my_pow(x, -n)
    if n % 2 == 0:
        half = my_pow(x, n // 2)
        return half * half
    else:
        return x * my_pow(x, n - 1)

# ===========================
# Меню для тестування
# ===========================

def main():
    print("Вибери задачу:")
    print("1. Реверс строки")
    print("2. Поміняти місцями вузли у зв'язаному списку")
    print("3. Число Фібоначчі")
    print("4. Скільки способів піднятися по сходах")
    print("5. Піднесення в ступінь (pow)")
    choice = input("Введи номер задачі (1-5): ")

    if choice == "1":
        s = input("Введи строку: ")
        print("Результат: ", end="")
        reverse_print(s)
        print()

    elif choice == "2":
        raw = input("Введи елементи списку через пробіл: ")
        values = list(map(int, raw.strip().split()))
        head = build_linked_list(values)
        print("До:")
        print_list(head)
        head = swap_pairs(head)
        print("Після:")
        print_list(head)

    elif choice == "3":
        n = int(input("Введи n: "))
        print(f"F({n}) =", fibonacci(n))

    elif choice == "4":
        n = int(input("Введи кількість сходинок: "))
        print(f"Кількість способів: {climb_stairs(n)}")

    elif choice == "5":
        x = float(input("Введи x: "))
        n = int(input("Введи n: "))
        result = my_pow(x, n)
        print(f"{x}^{n} = {result}")

    else:
        print("Невірний вибір.")

if __name__ == "__main__":
    main()
