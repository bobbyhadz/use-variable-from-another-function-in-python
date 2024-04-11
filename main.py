# How to use a Variable from another Function in Python

def func_a():
    odd_numbers = [1, 3, 5, 7, 9]

    return odd_numbers


def func_b():
    a_list = func_a()
    print(a_list)


func_b()  # 👉️ [1, 3, 5, 7, 9]