class Product:
    """Класс для представления товара."""
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализирует товар с названием, описанием, ценой и количеством."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для представления категории товаров."""
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        """Инициализирует категорию с названием, описанием и списком товаров."""
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)


phone = Product("Samsung", "Телефон", 50000, 10)
iphone = Product("iPhone", "Телефон", 80000, 5)

cat1 = Category("Смартфоны", "Телефоны", [phone, iphone])
cat2 = Category("Пустая категория", "Нет товаров", [])

print(Category.category_count)
print(Category.product_count)
