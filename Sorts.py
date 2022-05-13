import Tree
import time

class Sorts:


    __private_swaps = 0
    __private_compares = 0

    def round(self, f: float):
        """Округляем число в меньшую сторону"""
        x = int(f)
        if float(x) < f:
            x -= 1
        return x

    def compare(self, el1, el2, reverse = False, eq = False):
        """сравниваем значения для убывающиего и возрастающего порядка - если параметр reverse = False,
        а первый элемент больше второго, то их нужно поменять местами, то есть возвращаем True, если же
        reverse = True, то если первый элемент меньше второго, меняем их местами, возвращяя значение True"""
        self.__private_compares += 1
        if(el1 > el2 or ((eq^reverse) and el1 == el2)):
            reverse = not reverse
        return reverse

    def swap(self, clist: list, el, nel):
        self.__private_swaps += 1
        clist[el], clist[nel] = clist[nel], clist[el]


    def bubble_sort(self, clist: list, reverse: bool):
        """Сложность алгоритма O(x^2), так как в худшем случае сравниваем элементы n - 1 + n - 2 + ... =
        n * (1 + n - 1)/2 = (n^2)/2 = O(x^2) раз, в лучшем случае массив будет отсортирован pf n = O(n) раз,
        в среднем случае O(x^2), так как любое самоме малое число в конце вынуждает сортировать максимальное
        количество раз"""
        changed = True
        last = len(clist) - 1
        while (changed):
            """Если значения не были переставлены в текущей итерации, то массив отсортирован - завершаем сортировку,
            проходим по всем элементам списка, кроме последнего"""
            changed = False
            for el in range(0, last):
                if(self.compare(clist[el], clist[el + 1], reverse)):
                    self.swap(clist, el, el+1)
                    changed = True
            last -= 1

    def shaker_sort(self, clist: list, reverse: bool):
        """Модификация сортировки пузырьком - можно заметить, что при наличии самого малого элемента в конце
        списка количество сортировок достигает максимума, тогда для ускорения работы можно проходить от начала
        к концу списка и от конца к началу, тогда эта проблема уже не возникает, асимптотика та же, что и у пузырька,
        однако реальное время работы лучше"""
        changed = True
        last = len(clist) - 1
        first = -1;
        while (changed):
            """Если значения не были переставлены в текущей итерации, то массив отсортирован - завершаем сортировку,
            проходим по всем элементам списка, кроме последнего"""
            changed = False

            first += 1

            for el in range(first, last):
                if (self.compare(clist[el], clist[el + 1], reverse)):
                    self.swap(clist, el, el+1)
                    changed = True

            if(not changed):#если при итерации массив не сортировался, значит он отсортирован - завершаем сортировку
                break

            last -= 1

            for el in range(last, first, -1):
                if (self.compare(clist[el - 1], clist[el], reverse)):

                    self.swap(clist, el, el-1)
                    changed = True


    def comb_sort(self, clist: list, reverse: bool):
        """Модификация сортировки пузырьком - начала сортируем дальние друг от друга элемента на рсстоянии step,
         которое определяется коэффициентом k ,затем ближние, в конце обычная сортировка
        пузырьком, но с меньшим количеством итераций"""
        k = 1.2473309;

        step = len(clist) - 2;
        while (step > 1):
            i = 0
            while (i + step < len(clist)):
                if(self.compare(clist[i], clist[i + step], reverse)):
                    self.swap(clist, i, i + step)
                i += 1
            step /= k
            step = self.round(step)#Округляем число в меньшую сторону, чтобы не попасть в бесконечный цикл

        changed = True
        last = len(clist) - 1
        while (changed):
            """Обычная сортировка пузырьком"""
            changed = False
            for i in range(0, last):
                if (self.compare(clist[i], clist[i + 1], reverse)):
                    self.swap(clist, i, i + 1)
                    changed = True
            last -= 1

    def insertion_sort(self, clist: list, reverse: bool):
        """Сортировка вставками - вставляем каждый последующий элемент в подходящую для него позицию,
        сложность в лучшем случае - O(n) сравнений, в худшем и среднем O(n^2) сравнений и обменов"""

        for el in range(0, len(clist) - 1):
            i = el
            while(self.compare(clist[i], clist[i + 1], reverse) and i >= 0):
                self.swap(clist, i, i + 1)
                i -= 1

    def shell_sort(self, clist: list, reverse: bool):
        """Модификация сортировки вставками - предварительно разбиваем элементы на
         множества с шагом step, затем сравниваем между собой и меняем местами элементы
         этих множеств, их сортируем вставками пока step не станет равным 0"""
        step = len(clist) // 2


        while(step > 0):
            i = step
            while(i < len(clist)):
                j = i - step
                while(j >= 0 and self.compare(clist[j], clist[j + step], reverse)):
                    self.swap(clist, j, j + step)
                    j -= step
                i += 1
            step //= 2



    def tree_sort(self, clist: list, reverse: bool):
        tr = Tree.Tree(clist[0])
        i = 0
        for j in clist[1:]:
            ntr = Tree.Tree(j)
            i += tr.insert(ntr, reverse)
        del clist[:]
        tr.traverse(clist)
        self.__private_compares = int(i)
        self.__private_swaps = 'создано ' + str(len(clist)) + ' экземпляров объекта'
        pass

    def gnome_sort(self, clist: list, reverse: bool):
        i = 0
        it = 0
        while(i < len(clist)):

            it += 1
            if(i == 0 or self.compare(clist[i], clist[i - 1], reverse, eq=True)):
                i += 1
            else:
                self.swap(clist, i, i-1)
                i -= 1


    def selection_sort(self, clist: list, reverse: bool):
        for i in range(0, len(clist)):
            minz = clist[i]
            ind = i
            for j in range(i + 1, len(clist)):
                if(self.compare(minz, clist[j], reverse)):
                    minz = clist[j]
                    ind = j
            self.swap(clist, i, ind)



    def sort(self, clist: list, sort_type: str, reverse = False):
        self.__private_compares = self.__private_swaps = 0
        ts = time.time()
        if (len(clist) < 2):
            return
        match sort_type:
            case 'Сортировка пузырьком':
                self.bubble_sort(clist, reverse)
            case 'Коктейльная сортировка':
                self.shaker_sort(clist, reverse)
            case 'Сортировка расчёской':
                self.comb_sort(clist, reverse)
            case 'Сортировка вставками':
                self.insertion_sort(clist, reverse)
            case 'Сортировка Шелла':
                self.shell_sort(clist, reverse)
            case 'Сортировка деревом':
                self.tree_sort(clist, reverse)
            case 'Гномья сортировка':
                self.gnome_sort(clist, reverse)
            case 'Сортировка выбором':
                self.selection_sort(clist, reverse)
        return self.__private_compares, self.__private_swaps, time.time() - ts
