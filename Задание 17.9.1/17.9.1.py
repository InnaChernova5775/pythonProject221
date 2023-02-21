
def merge_sort(L):

    if len(L) < 2: # если кусок массива меньше 2,
        return L[:]  # выходим из рекурсии
    else:
         middle = len(L) // 2  # ищем середину
         left = merge_sort(L[:middle])  # рекурсивно делим левую часть
         right = merge_sort(L[middle:]) # и правую
         return merge(left, right)  # выполняем слияние


def merge(left, right):# "властвуй"
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы
     # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
           result.append(left[i])
           i += 1
        else:
           result.append(right[j])
           j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result

# Бинарный поиск
def binary_search(L_1, N, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (right + left) // 2  # находимо середину
    if L_1[middle] == N:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif N< L_1[middle]:  # если элемент меньше элемента в середине
  # рекурсивно ищем в левой половине
        return binary_search(L_1,N, left, middle - 1)
    else:  # иначе в правой
         return binary_search(L_1, N, middle + 1, right)

try:
    A = input("Введите числа через пробел:")
    N = float(input("Введите число для его поиска в списке:"))
    L = [float(i) for i in A.split()]
    print('Введенный список до сортировки', L)
    L_1=merge_sort(L)
    print('Введенный список после сортировки', L_1)

    if N <min(L_1) or N> max(L_1):
        print ('Введенное число для поиска меньше  минимального или больше максимального в списке')
    elif N in L_1:
        print ('Введенное число присутствует в списке с индексом в отсортированном списке',binary_search(L_1,N, 0, len(L_1)))
    else:

        L_1.append(N)
        L_2 =merge_sort(L_1)
        index=binary_search(L_2,N, 0, len(L_2))
        print('Номер индекса ближайшего меньшего к числу, введенному для поиска:',(index-1))
        print('Индекс ближайшего большего к числу,введенному для поискa:',(index))
except ValueError:
    print(f'Ошибка ввода {ValueError}')
    print('Введено недопустимое значение.')
