# GCD(n, k) = 1


def euler_phi(target_number: int):
    result = target_number
    check_number = 2

    while pow(check_number, 2) <= target_number:
        if not target_number % check_number:
            while not target_number % check_number:
                target_number //= check_number
            result -= result // check_number
        check_number += 1

    if target_number > 1:
        result -= result // target_number

    return result


target = int(input())
print(euler_phi(target))
