# class Solution(object):
#     def twosum(self, nums, target):
#         d = {}
#
#         for i in range(len(nums)):
#             d[nums[i]] = i
#
#         for i in range(len(nums)):
#             x = target - nums[i]
#             if x in d and i != d[x]:
#                 return [nums[i], x]
#         return None
#
#
# solution = Solution()
# nums = [85, 9, 90, 96, 47, 5, 78, 42, 6, 13, 91, 62, 99, 75, 33, 89, 38, 1, 55, 77, 46, 16, 57, 95, 71, 51, 4, 29, 26]
# target = 57
# result = solution.twosum(nums, target)
# print(result)


# class Solution(object):
#     def fibonacci(self, n):
#         nums = [0, 1]
#
#         array = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
#         length = len(array) + 1
#
#         while len(nums) < length:
#             next_sum = nums[-1] + nums[-2]
#             nums.append(next_sum)
#         return next_sum
#
#
# solution = Solution()
# print(solution.fibonacci(1))


# def sort_impar_par(lista):
#     lista_par = []
#     lista_impar = []
#
#     for i in lista:
#         if i % 2 == 0:
#             lista_par.append(i)
#             # print(f"par = {lista_par}")
#         else:
#             lista_impar.append(i)
#             # print(f"impar = {lista_impar}")
#
#     lista_par.sort()
#     lista_impar.sort()
#
#     return lista_par, lista_impar
#
#
# # Example usage
# lista = [-24, 70, 98, 80, 95, 12, 28, -37, -63, 9, -22, -93, 91]
# par_sorteado, impar_sorteado = sort_impar_par(lista)
#
# print("Lista:", lista)
# print("Ordenado par:", par_sorteado)
# print("Ordenado impar:", impar_sorteado)
# print("Lista ordenada junta: ", par_sorteado + impar_sorteado)



def sort_even_odd(input_list):
    even_list = []
    odd_list = []

    for num in input_list:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)

    even_list.sort()
    odd_list.sort()

    return even_list, odd_list


# Example usage
input_numbers = [9, 2, 7, 4, 5, 8, 3, 6, 1]
sorted_even, sorted_odd = sort_even_odd(input_numbers)

print("Original list:", input_numbers)
print("Sorted even numbers:", sorted_even)
print("Sorted odd numbers:", sorted_odd)
print("Sorted list: ", sorted_even + sorted_odd)


# import hashlib
#
# # Frase e método fornecidos
# sentence = "liquors_massed_machines_play"
# method = "md5"
#
# # Gerando a hash MD5 da frase
# hash_md5 = hashlib.md5(sentence.encode()).hexdigest()
#
# print(hash_md5)
