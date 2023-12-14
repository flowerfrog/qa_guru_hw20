import allure
from tests.utils import api_post
from selene import browser, have
from data.items import Item


class AddItemsToCart:
    def open_to_cart(self):
        with allure.step("Открываем корзину"):
            browser.open('/cart')
            return self

    @staticmethod
    def open_browser_with_added_item(url=None, data=None):
        with allure.step('Открываем браузер с добавленным товаром в корзину'):
            result = api_post(url=url,
                              data=data)
            cookies = result.cookies.get('Nop.customer')
            browser.open('/')
            browser.driver.add_cookie({'name': 'Nop.customer', 'value': cookies})

    @staticmethod
    def item_has_been_added_to_cart(item):
        with allure.step('Проверяем, что товар добавлен в корзину'):
            browser.element('a.product-name').should(have.text(item.name))
            browser.element('input.qty-input').should(have.value(f'{item.qty}'))
            browser.element('.product-unit-price').should(have.text(item.price))
            browser.element('.product-subtotal').should(have.text(item.total_price))


def test_adding_virtual_gift_card_to_cart():
    item = Item(
        name="$25 Virtual Gift Card",
        qty=1,
        price="25.00",
        total_price="25.00"
    )

    add_items_to_cart = AddItemsToCart()

    # GIVEN
    add_items_to_cart.open_browser_with_added_item(url="/2/1", data={
        "giftcard_2.RecipientName": "test",
        "giftcard_2.RecipientEmail": "test_recipient@mail.com",
        "giftcard_2.SenderName": "test",
        "giftcard_2.SenderEmail": "test_sender@mail.com",
        "giftcard_2.Message": "test)",
        "addtocart_2.EnteredQuantity": 1
    })

    # WHEN
    add_items_to_cart.open_to_cart()

    # THEN
    add_items_to_cart.item_has_been_added_to_cart(item)


def test_adding_simple_computer_to_cart():
    item = Item(
        name="Simple Computer",
        qty=2,
        price="800.00",
        total_price="1600.00"
    )

    add_items_to_cart = AddItemsToCart()

    # GIVEN
    add_items_to_cart.open_browser_with_added_item(url="/75/1", data={
        "product_attribute_75_5_31": 96,
        "product_attribute_75_6_32": 100,
        "product_attribute_75_3_33": 102,
        "product_attribute_75_8_35": 108,
        "addtocart_75.EnteredQuantity": 2
    })

    # WHEN
    add_items_to_cart.open_to_cart()

    # THEN
    add_items_to_cart.item_has_been_added_to_cart(item)


def test_adding_own_computer_to_cart():
    item = Item(
        name="Build your own computer",
        qty=1,
        price="1265.00",
        total_price="1265.00"
    )

    add_items_to_cart = AddItemsToCart()

    # GIVEN
    add_items_to_cart.open_browser_with_added_item(url="/16/1", data={
        "product_attribute_16_5_4": 14,
        "product_attribute_16_6_5": 15,
        "product_attribute_16_3_6": 18,
        "product_attribute_16_4_7": 44,
        "product_attribute_16_8_8": 22,
        "addtocart_16.EnteredQuantity": 1
    })

    # WHEN
    add_items_to_cart.open_to_cart()

    # THEN
    add_items_to_cart.item_has_been_added_to_cart(item)
