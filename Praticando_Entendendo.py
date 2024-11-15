# def soma(x, y):
#     print(x + y)
#
#
# soma(2, 3)

# args = 5,5,4


# def multi(*numeros):
#     total = 1
#     for numero in numeros:
#
#         total *= numero
#     # print(total)
#     return total
#
#
# print(multi(5, 5, 4))
# # multi(5, 5, 4)
#
#
# def par_impar(numero):
#
#     if numero % 2 == 0:
#         return 'Par'
#     return 'Impar'
#
#
# print(par_impar(6))
# print(par_impar(5))
# print(par_impar(26))


# class Solution(object):
#     def twosum(self, nums, target):
#         d = []
#
#         for i in range(0, len(nums)):
#             d[nums[i]] = i
#
#         for i in range(0, len(nums)):
#             x = target - nums[i]
#             if x in d and i != d[x]:
#                 return [i, d[x]]
#         return None

# a, b = 0, 1
#
# while a <= 13:
#     if a % 2 == 1:
#         print(a)
#     a, b = b, a + b


# def foo(a, b):
#     while a != b:
#         if a > b:
#             a = a - b
#         elif b > a:
#             b -= a
#     return a
#
#
# print(foo(48, 36))

# def multiplicador(multiplicador):
#     def multiplicar(num):
#         return num * multiplicador
#     return multiplicar
#
#
# duplicar = multiplicador(2)
# triplicar = multiplicador(3)
# quadruplicar = multiplicador(4)
#
# print(duplicar(2))
# print(triplicar(2))
# print(quadruplicar(2))

pessoa = {
    'nome': 'Lucas',
    'sobrenome': 'Rocha',
    'idade': 20,
    'altura': 1.83,
    'endereços': [
        {'rua': 'Rua 1', 'numero': 255},
        {'rua': 'Rua 2', 'numero': 258},
    ]
}

# print(pessoa)

for chave in pessoa:
    print(chave + ':', pessoa[chave])
