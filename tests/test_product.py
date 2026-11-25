from src.product import Product, Category


def test_product_init():
    prod_1 = Product('samsung', 'смартфоны', 50000, 10)
    assert prod_1.name == 'samsung'
    assert prod_1.description == 'смартфоны'
    assert prod_1.price == 50000
    assert prod_1.quantity == 10


def test_category_init():
    phone = Product("Samsung", "Смартфон", 50000, 10)
    iphone = Product("iPhone", "Смартфон", 80000, 5)
    category_product = Category('Смартфоны', 'Мобильные телефоны', [phone, iphone])
    assert category_product.name == 'Смартфоны'
    assert category_product.description == 'Мобильные телефоны'
    assert len(category_product.products) == 2
    assert category_product.products[0] is phone


def test_category_count():
    before = Category.category_count

    Category("Телевизоры", "Бытовая техника", [])
    assert Category.category_count == before + 1


def test_product_count():
    before = Category.product_count

    phone = Product("Samsung", "Смартфон", 50000, 10)
    iphone = Product("iPhone", "Смартфон", 80000, 5)

    Category("Смартфоны", "Телефоны", [phone, iphone])
    assert Category.product_count == before + 2
