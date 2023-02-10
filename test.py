from main import Shop, Cart, Item
import unittest

class CartTest(unittest.TestCase):
    
    def test_add_item(self):
        test_cart = Cart()
        test_cart.add("eggs", 12, 6.5)
        self.assertEqual(len(test_cart.items), 1)
        self.assertEqual(test_cart.items["eggs"].quantity, 12)
        self.assertEqual(test_cart.items["eggs"].price, 6.5)
        
        test_cart.add("apple", 2, 0.99)
        self.assertEqual(len(test_cart.items), 2)
        self.assertEqual(test_cart.items["apple"].quantity, 2)
        self.assertEqual(test_cart.items["apple"].price, 0.99)

    def test_item_instantiation(self):
        test_item = Item("bread", 2, 1.99)
        self.assertEqual(test_item.name, "bread")
        self.assertEqual(test_item.quantity, 2)
        self.assertEqual(test_item.price, 1.99)


    def test_delete_item(self):
        test_cart = Cart()
        test_cart.add("milk", 1, 3.5)
        test_cart.delete("milk")
        self.assertEqual(len(test_cart.items), 0)

    def test_delete_two_items(self):
        test_cart = Cart()
        test_cart.add("banana", 4, 0.25)
        test_cart.add("lemon", 2, 0.10)
        
        test_cart.delete("banana")
        self.assertEqual(len(test_cart.items), 1)
        self.assertNotIn("banana", test_cart.items)
        
        test_cart.delete("onion")
        self.assertEqual(len(test_cart.items), 1)
        


        

unittest.main()
