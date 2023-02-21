# G = {"Адмиралтейская" :
#          ["Садовая"],
#      "Садовая" :
#          ["Сенная площадь",
#           "Спасская",
#           "Адмиралтейская",
#           "Звенигородская"],
#      "Сенная площадь" :
#          ["Садовая",
#           "Спасская"],
#      "Спасская" :
#          ["Садовая",
#           "Сенная площадь",
#           "Достоевская"],
#      "Звенигородская" :
#          ["Пушкинская",
#           "Садовая"],
#      "Пушкинская" :
#          ["Звенигородская",
#           "Владимирская"],
#      "Владимирская" :
#          ["Достоевская",
#           "Пушкинская"],
#      "Достоевская" :
#          ["Владимирская",
#           "Спасская"]}
#
# G = {"Адмиралтейская" :
#          {"Садовая" : 4},
#      "Садовая" :
#          {"Сенная площадь" : 3,
#           "Спасская" : 3,
#           "Адмиралтейская" : 4,
#           "Звенигородская" : 5},
#      "Сенная площадь" :
#          {"Садовая" : 3,
#           "Спасская" : 3},
#      "Спасская" :
#          {"Садовая" : 3,
#           "Сенная площадь" : 3,
#           "Достоевская" : 4},
#      "Звенигородская" :
#          {"Пушкинская" : 3,
#           "Садовая" : 5},
#      "Пушкинская" :
#          {"Звенигородская" : 3,
#           "Владимирская" : 4},
#      "Владимирская" :
#          {"Достоевская" : 3,
#           "Пушкинская" : 4},
#      "Достоевская" :
#          {"Владимирская" : 3,
#           "Спасская" : 4}}
#
# D = {k : 100 for k in G.keys()} # расстояния
# start_k = 'Адмиралтейская' # стартовая вершина
# D[start_k] = 0 # расстояние от неё до самой себя равно нулю
# U = {k : False for k in G.keys()} # флаги просмотра вершин
#
# for _ in range(len(D)):
#     # выбираем среди непросмотренных наименьшее по расстоянию
#     min_k = min([k for k in U.keys() if not U[k]], key = lambda x: D[x])
#
#     for v in G[min_k].keys(): # проходимся по всем смежным вершинам
#         D[v] = min(D[v], D[min_k] + G[min_k][v]) # минимум
#     U[min_k] = True # просмотренную вершину помечаем
# print(D)
#
# P = {k : None for k in G.keys()}
#
# D = {k : 100 for k in G.keys()} # расстояния
# start_k = 'Адмиралтейская' # стартовая вершина
# D[start_k] = 0 # расстояние от нее до самой себя равно нулю
# U = {k : False for k in G.keys()} # флаги просмотра вершин
# P = {k : None for k in G.keys()} # предки
#
# for _ in range(len(D)):
#     # выбираем среди непросмотренных наименьшее по расстоянию
#     min_k = min([k for k in U.keys() if not U[k]], key = lambda x: D[x])
#
#     for v in G[min_k].keys(): # проходимся по всем смежным вершинам
#          if D[v] > D[min_k] + G[min_k][v]: # если расстояние от текущей вершины меньше
#             D[v] = D[min_k] + G[min_k][v] # то фиксируем его
#             P[v] = min_k # и записываем как предок
#     U[min_k] = True # просмотренную вершину помечаем
#
# # pointer = some_station # куда должны прийти
# pointer = "Владимирская"
# while pointer is not None: # перемещаемся, пока не придём в стартовую точку
#     print(pointer)
#     pointer = P[pointer]

# Древовидные структуры мы видим повсеместно: фамильное древо, структура организаций, которая тоже чаще всего иерархическая. Или же, например, объектная модель документов (DOM) в языке HTML, с которой мы познакомимся в следующих модулях.
#
# В зависимости от максимального количества потомков в одной вершине различают:
#
# бинарные;
# тернарные деревья;
# n-арные деревья (с максимальным количеством потомков n);
# 2-3 деревья, 2-3-4, в которых помимо увеличенного количества потомков в самом узле может храниться больше данных.
# О таких деревьях в курсе мы говорить не будем, но после знакомства с основной информацией о бинарных деревьях, можно обратиться к статье.
#
# Итак, рассмотрим бинарное дерево. Основное его свойство заключается в том, что у каждого узла может быть не более 2 потомков — соответственно, левый и/или правый.
#
# img
# Источник: habr.com
# Линейные структуры данных (массивы, списки, очереди, стеки) более понятны интуитивно. Но как же хранить в памяти деревья? Здесь нам поможет знание объектно-ориентированного программирования, а воспользуемся мы принципом, по которому хранятся списки в памяти. Напомним, что каждый элемент списка хранит собственное значение и указатель на следующий элемент.
#
# В нашей структуре данных, в каждом узле бинарного дерева мы будем хранить указатель на левого и правого потомка.
#
# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left_child = None
#         self.right_child = None
# class Node:
#    def __init__(self, data):
#       self.left = None
#       self.right = None
#       self.data = data
#
# class BinaryTree:
#     def __init__(self, datd):
#         self.data = data
#         self.left_child = None
#         self.right_child = None
#
#
# def insert_left(self,new_data):
#     if self.left is None:
#         self.left = BinaryTree(data)
#     else:
#         self.left = BinaryTree(new_data)
#     return self.left
#
# def insert_right(self,new_data):
#     if self.right is None:
#         self.right = BinaryTree(data)
#     else:
#
#         self.right= BinaryTree(new_data)
#     return self.right
# # создаём корень и его потомков /7|2|5\
#
# node_root = BinaryTree(2).insert_left (7),insert_right(5)
# # левое поддерево корня /2|7|6\
# node_7 = BinaryTree(7).insert_left(2).insert_right(6)
# # правое поддерево предыдущего узла /5|6|11\
# node_6 = BinaryTree(6).insert_left(5).insert_right(11)
# # правое поддерево корня /|5|9\
# node_5 = BinaryTree(6).insert_right(9)
# # левое поддерево предыдущего узла корня /4|9|\
# node_9 = BinaryTree(9.insert_left(4)
#
# def post_order(self):
#     if self.left_child is not None: # если левый потомок существует
#         self.left_child.post_order() # рекурсивно вызываем функцию
#
#     if self.right_child is not None: # если правый потомок существует
#         self.right_child.post_order() # рекурсивно вызываем функцию
#
#     print(self.value) # процедура обработки
# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left_child = None
#         self.right_child = None
#
#     def insert_left(self, next_value):
#         if self.left_child is None:
#             self.left_child = BinaryTree(next_value)
#         else:
#             new_child = BinaryTree(next_value)
#             new_child.left_child = self.left_child
#             self.left_child = new_child
#         return self
#
#     def insert_right(self, next_value):
#         if self.right_child is None:
#             self.right_child = BinaryTree(next_value)
#         else:
#             new_child = BinaryTree(next_value)
#             new_child.right_child = self.right_child
#             self.right_child = new_child
#         return self
#
#     def pre_order(self):
#
#         # global node_root
#         # global BinaryTree
#
#         print(self.value)  # процедура обработки
#
#         if self.left_child is not None:  # если левый потомок существует
#             self.left_child.pre_order()  # рекурсивно вызываем функцию
#
#         if self.right_child is not None:  # если правый потомок существует
#             self.right_child.pre_order()  # рекурсивно вызываем функцию
#
#     def post_order(self):
#         if self.left_child is not None:  # если левый потомок существует
#             self.left_child.post_order()  # рекурсивно вызываем функцию
#
#         if self.right_child is not None:  # если правый потомок существует
#             self.right_child.post_order()  # рекурсивно вызываем функцию
#
#         print(self.value)  # процедура обработки
#
# node_root = BinaryTree(2).insert_left(7).insert_right(5)
# # левое поддерево корня /2|7|6\
# node_7 = node_root.left_child.insert_left(2).insert_right(6)
# # правое поддерево предыдущего узла /5|6|11\
# node_6 = node_7.right_child.insert_left(5).insert_right(11)
# # правое поддерево корня /|5|9\
# node_5 = node_root.right_child.insert_right(9)
# # левое поддерево предыдущего узла корня /4|9|\
# node_9 = node_5.right_child.insert_left(4)
#
# # def pre_order(self):
# #
# #     # global node_root
# #     # global BinaryTree
# #
# #     print(self.value) # процедура обработки
# #
# #     if self.left_child is not None: # если левый потомок существует
# #         self.left_child.pre_order() # рекурсивно вызываем функцию
# #
# #     if self.right_child is not None: # если правый потомок существует
# #         self.right_child.pre_order() # рекурсивно вызываем функцию
# node_root.post_order()
class Node:  # класс элемента
    def __init__(self, value=None, next_=None):  # инициализируем
        self.value = value  # значением
        self.next = next_  # и ссылкой на следующий элемент

    def __str__(self):
        return "Node value = " + str(self.value)


class LinkedList:  # класс списка
    def __init__(self):  # инициализируем пустым
        self.first = None
        self.last = None

    def clear(self):  # очищаем список
        self.__init__()

    def __str__(self):  # функция печати
        R = ''

        pointer = self.first  # берем первый указатель
        while pointer is not None:  # пока указатель не станет None
            R += str(pointer.value)  # добавляем значение в строку
            pointer = pointer.next  # идем дальше по указателю
            if pointer is not None:  # если он существует добавляем пробел
                R += ' '
        return R

    def pushleft(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value, self.first)
            self.first = new_node

    def pushright(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value)
            self.last.next = new_node
            self.last = new_node

    def popleft(self):
        if self.first is None:
            # если список пустой, возвращаем None
            return None
        elif self.first == self.last:  # если список содержит только один элемент
            node = self.first  # сохраняем его
            self.__init__()  # очищаем
            return node  # и возвращаем сохраненный элемент
        else:
            node = self.first  # сохраняем первый элемент
            self.first = self.first.next  # меняем указатель на первый элемент
            return node  # возвращаем сохраненный

    def popright(self):
        if self.first is None:  # если список пустой, возвращаем None
            return None
        elif self.first == self.last:  # если список содержит только один элемент
            node = self.first  # сохраняем его
            self.__init__()  # очищаем
            return node  # и возвращаем сохраненный элемент
        else:
            node = self.last  # сохраняем последний
            pointer = self.first  # создаем указатель
            while pointer.next is not node:  # пока не найдем предпоследний
                pointer = pointer.next
                pointer.next = None  # обнуляем указатели, чтобы
                self.last = pointer  # предпоследний стал последним
                return node  # возвращаем сохраненный

    def __iter__(self):  # объявляем класс как итератор
        self.current = self.first  # в текущий элемент помещаем первый
        return self  # возвращаем итератор

    def __next__(self):  # метод перехода
        if self.current is None:  # если текущий стал последним
            raise StopIteration  # вызываем исклчение
        else:
            node = self.current  # сохраняем текущий элемент
            self.current = self.current.next  # совершаем переход
            return node  # и возвращаем сохраненный

    def __len__(self):
        count = 0
        pointer = self.first
        while pointer is not None:
            count += 1
            pointer = pointer.next
        return count

LL = LinkedList()

LL.pushright(1)
LL.pushleft(2)
LL.pushright(3)
LL.popright()
LL.pushleft(4)
LL.pushright(5)
LL.popleft()

print(LL.__len__())