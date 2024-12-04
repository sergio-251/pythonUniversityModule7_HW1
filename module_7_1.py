# Режимы открытия файлов

class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def __is_product_exist(self, product):
        return product.name in self.get_products()

    def get_products(self):
        file = open(self.__file_name, 'r')
        s = file.read()
        file.close()
        return s

    def add(self, *products):
        if self.get_products() == '':
            file = open(self.__file_name, 'a')
            for p in products:
                file.write(f'{str(p)}\n')
            file.close()
        else:
            file = open(self.__file_name, 'a')
            for p in products:
                if self.__is_product_exist(p):
                    print(f'Продукт {p.name} уже есть в магазине')
                    continue
                else:
                    file.write(f'{str(p)}\n')
            file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())

