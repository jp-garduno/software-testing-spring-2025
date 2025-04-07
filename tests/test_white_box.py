# -*- coding: utf-8 -*-

"""
Complete white-box unit testing for white_box.py
"""
import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.white_box import (
    is_even,
    divide,
    get_grade,
    is_triangle,
    check_number_status,
    validate_password,
    calculate_total_discount,
    calculate_order_total,
    calculate_items_shipping_cost,
    validate_login,
    verify_age,
    categorize_product,
    validate_email,
    celsius_to_fahrenheit,
    validate_credit_card,
    validate_date,
    check_flight_eligibility,
    validate_url,
    calculate_quantity_discount,
    check_file_size,
    check_loan_eligibility,
    calculate_shipping_cost,
    grade_quiz,
    authenticate_user,
    get_weather_advisory,
    VendingMachine,
    TrafficLight,
    UserAuthentication,
    DocumentEditingSystem,
    ElevatorSystem,
    BankAccount,
    BankingSystem,
    Product,
    ShoppingCart
)


class TestWhiteBoxBasicFunctions(unittest.TestCase):
    """
    Unit tests for basic white-box functions.
    """

    def test_is_even(self):
        """Tests the is_even function."""
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(-4))
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(-3))

    def test_divide(self):
        """Tests the divide function."""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(7, 2), 3.5)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(10, -2), -5)
        self.assertEqual(divide(0, 5), 0)
        self.assertEqual(divide(10, 0), 0)  # Division by zero returns 0

    def test_get_grade(self):
        """Tests the get_grade function."""
        self.assertEqual(get_grade(95), "A")
        self.assertEqual(get_grade(90), "A")
        self.assertEqual(get_grade(85), "B")
        self.assertEqual(get_grade(80), "B")
        self.assertEqual(get_grade(75), "C")
        self.assertEqual(get_grade(70), "C")
        self.assertEqual(get_grade(65), "F")
        self.assertEqual(get_grade(0), "F")

    def test_is_triangle(self):
        """Tests the is_triangle function."""
        self.assertEqual(is_triangle(3, 4, 5), "Yes, it's a triangle!")
        self.assertEqual(is_triangle(5, 5, 5), "Yes, it's a triangle!")
        self.assertEqual(is_triangle(2, 2, 3), "Yes, it's a triangle!")
        self.assertEqual(is_triangle(1, 2, 3), "No, it's not a triangle.")
        self.assertEqual(is_triangle(3, 4, 8), "No, it's not a triangle.")
        self.assertEqual(is_triangle(5, 10, 3), "No, it's not a triangle.")


class TestWhiteBoxAdditionalFunctions(unittest.TestCase):
    """
    Unit tests for additional white-box functions.
    """

    def test_check_number_status(self):
        """Tests the check_number_status function."""
        self.assertEqual(check_number_status(5), "Positive")
        self.assertEqual(check_number_status(-3), "Negative")
        self.assertEqual(check_number_status(0), "Zero")

    def test_validate_password(self):
        """Tests the validate_password function."""
        self.assertTrue(validate_password("Passw0rd!"))
        self.assertTrue(validate_password("SecureP@ss123"))
        self.assertFalse(validate_password("password"))  # No uppercase
        self.assertFalse(validate_password("PASSWORD"))  # No lowercase
        self.assertFalse(validate_password("Password"))  # No digit
        self.assertFalse(validate_password("Passw0rd"))  # No special character
        self.assertFalse(validate_password("Pw0!"))  # Too short

    def test_calculate_total_discount(self):
        """Tests the calculate_total_discount function."""
        self.assertEqual(calculate_total_discount(50), 0)
        self.assertEqual(calculate_total_discount(100), 10)
        self.assertEqual(calculate_total_discount(300), 30)
        self.assertEqual(calculate_total_discount(500), 50)
        self.assertEqual(calculate_total_discount(1000), 200)

    def test_calculate_order_total(self):
        """Tests the calculate_order_total function."""
        items1 = [{"quantity": 3, "price": 10}]
        self.assertEqual(calculate_order_total(items1), 30)

        items2 = [{"quantity": 7, "price": 10}]
        self.assertEqual(calculate_order_total(items2), 66.5)  # 7 * 10 * 0.95

        items3 = [{"quantity": 15, "price": 10}]
        self.assertEqual(calculate_order_total(items3), 135)  # 15 * 10 * 0.9

        items4 = [
            {"quantity": 3, "price": 10},
            {"quantity": 7, "price": 20},
            {"quantity": 15, "price": 5}
        ]
        # 3*10 + 7*20*0.95 + 15*5*0.9
        self.assertEqual(calculate_order_total(items4), 30 + 133 + 67.5)

    def test_calculate_items_shipping_cost(self):
        """Tests the calculate_items_shipping_cost function."""
        items1 = [{"weight": 2}, {"weight": 2}]  # Total weight: 4
        self.assertEqual(calculate_items_shipping_cost(items1, "standard"), 10)
        self.assertEqual(calculate_items_shipping_cost(items1, "express"), 20)

        items2 = [{"weight": 3}, {"weight": 4}]  # Total weight: 7
        self.assertEqual(calculate_items_shipping_cost(items2, "standard"), 15)
        self.assertEqual(calculate_items_shipping_cost(items2, "express"), 30)

        items3 = [{"weight": 5}, {"weight": 6}]  # Total weight: 11
        self.assertEqual(calculate_items_shipping_cost(items3, "standard"), 20)
        self.assertEqual(calculate_items_shipping_cost(items3, "express"), 40)

        # Test invalid shipping method
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost(items1, "invalid")

    def test_validate_login(self):
        """Tests the validate_login function."""
        self.assertEqual(validate_login("user1", "password123"), "Login Successful")
        self.assertEqual(validate_login("user", "password123"), "Login Failed")  # Username too short
        self.assertEqual(validate_login("user1", "pass"), "Login Failed")  # Password too short
        self.assertEqual(validate_login("thisusernameistoolong", "password123"), "Login Failed")  # Username too long
        self.assertEqual(validate_login("user1", "thispasswordistoolong"), "Login Failed")  # Password too long

    def test_verify_age(self):
        """Tests the verify_age function."""
        self.assertEqual(verify_age(18), "Eligible")
        self.assertEqual(verify_age(30), "Eligible")
        self.assertEqual(verify_age(65), "Eligible")
        self.assertEqual(verify_age(17), "Not Eligible")
        self.assertEqual(verify_age(66), "Not Eligible")

    def test_categorize_product(self):
        """Tests the categorize_product function."""
        self.assertEqual(categorize_product(10), "Category A")
        self.assertEqual(categorize_product(30), "Category A")
        self.assertEqual(categorize_product(50), "Category A")
        self.assertEqual(categorize_product(51), "Category B")
        self.assertEqual(categorize_product(75), "Category B")
        self.assertEqual(categorize_product(100), "Category B")
        self.assertEqual(categorize_product(101), "Category C")
        self.assertEqual(categorize_product(150), "Category C")
        self.assertEqual(categorize_product(200), "Category C")
        self.assertEqual(categorize_product(5), "Category D")
        self.assertEqual(categorize_product(201), "Category D")

    def test_validate_email(self):
        """Tests the validate_email function."""
        self.assertEqual(validate_email("user@example.com"), "Valid Email")
        self.assertEqual(validate_email("a@b.c"), "Valid Email")  # Minimum length
        self.assertEqual(validate_email("verylong@example.com"), "Valid Email")
        self.assertEqual(validate_email("abc"), "Invalid Email")  # No @ or .
        self.assertEqual(validate_email("abc@def"), "Invalid Email")  # No .
        self.assertEqual(validate_email("abc.def"), "Invalid Email")  # No @
        self.assertEqual(validate_email("a@b"), "Invalid Email")  # Too short
        
    def test_celsius_to_fahrenheit(self):
        """Tests the celsius_to_fahrenheit function."""
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        self.assertEqual(celsius_to_fahrenheit(100), 212)
        self.assertEqual(celsius_to_fahrenheit(-40), -40)
        self.assertEqual(celsius_to_fahrenheit(37), 98.6)
        self.assertEqual(celsius_to_fahrenheit(-100), -148)
        self.assertEqual(celsius_to_fahrenheit(101), "Invalid Temperature")
        self.assertEqual(celsius_to_fahrenheit(-101), "Invalid Temperature")

    def test_validate_credit_card(self):
        """Tests the validate_credit_card function."""
        self.assertEqual(validate_credit_card("4111111111111111"), "Valid Card")  # 16 digits
        self.assertEqual(validate_credit_card("4111111111111"), "Valid Card")  # 13 digits
        self.assertEqual(validate_credit_card("411111111111"), "Invalid Card")  # Too short
        self.assertEqual(validate_credit_card("41111111111111111"), "Invalid Card")  # Too long
        self.assertEqual(validate_credit_card("4111-1111-1111-1111"), "Invalid Card")  # Non-digit characters

    def test_validate_date(self):
        """Tests the validate_date function."""
        self.assertEqual(validate_date(2023, 1, 1), "Valid Date")
        self.assertEqual(validate_date(1900, 1, 1), "Valid Date")
        self.assertEqual(validate_date(2100, 12, 31), "Valid Date")
        self.assertEqual(validate_date(1899, 1, 1), "Invalid Date")  # Year too early
        self.assertEqual(validate_date(2101, 1, 1), "Invalid Date")  # Year too late
        self.assertEqual(validate_date(2023, 0, 1), "Invalid Date")  # Month too early
        self.assertEqual(validate_date(2023, 13, 1), "Invalid Date")  # Month too late
        self.assertEqual(validate_date(2023, 1, 0), "Invalid Date")  # Day too early
        self.assertEqual(validate_date(2023, 1, 32), "Invalid Date")  # Day too late

    def test_check_flight_eligibility(self):
        """Tests the check_flight_eligibility function."""
        self.assertEqual(check_flight_eligibility(18, False), "Eligible to Book")
        self.assertEqual(check_flight_eligibility(65, False), "Eligible to Book")
        self.assertEqual(check_flight_eligibility(30, True), "Eligible to Book")
        self.assertEqual(check_flight_eligibility(17, False), "Not Eligible to Book")
        self.assertEqual(check_flight_eligibility(66, False), "Not Eligible to Book")
        self.assertEqual(check_flight_eligibility(17, True), "Eligible to Book")
        self.assertEqual(check_flight_eligibility(66, True), "Eligible to Book")

    def test_validate_url(self):
        """Tests the validate_url function."""
        self.assertEqual(validate_url("http://example.com"), "Valid URL")
        self.assertEqual(validate_url("https://example.com"), "Valid URL")
        self.assertEqual(validate_url("ftp://example.com"), "Invalid URL")  # Wrong protocol
        self.assertEqual(validate_url("example.com"), "Invalid URL")  # No protocol
        
        # Test URL that is too long (256 characters)
        long_url = "https://" + "a" * 249
        self.assertEqual(validate_url(long_url), "Invalid URL")

    def test_calculate_quantity_discount(self):
        """Tests the calculate_quantity_discount function."""
        self.assertEqual(calculate_quantity_discount(1), "No Discount")
        self.assertEqual(calculate_quantity_discount(5), "No Discount")
        self.assertEqual(calculate_quantity_discount(6), "5% Discount")
        self.assertEqual(calculate_quantity_discount(10), "5% Discount")
        self.assertEqual(calculate_quantity_discount(11), "10% Discount")
        self.assertEqual(calculate_quantity_discount(100), "10% Discount")

    def test_check_file_size(self):
        """Tests the check_file_size function."""
        self.assertEqual(check_file_size(0), "Valid File Size")
        self.assertEqual(check_file_size(1024), "Valid File Size")  # 1 KB
        self.assertEqual(check_file_size(1048576), "Valid File Size")  # 1 MB
        self.assertEqual(check_file_size(-1), "Invalid File Size")  # Negative size
        self.assertEqual(check_file_size(1048577), "Invalid File Size")  # Exceeds 1 MB

    def test_check_loan_eligibility(self):
        """Tests the check_loan_eligibility function."""
        self.assertEqual(check_loan_eligibility(20000, 700), "Not Eligible")
        self.assertEqual(check_loan_eligibility(30000, 650), "Secured Loan")
        self.assertEqual(check_loan_eligibility(30000, 750), "Standard Loan")
        self.assertEqual(check_loan_eligibility(50000, 650), "Secured Loan")
        self.assertEqual(check_loan_eligibility(50000, 750), "Standard Loan")
        self.assertEqual(check_loan_eligibility(70000, 700), "Standard Loan")
        self.assertEqual(check_loan_eligibility(70000, 800), "Premium Loan")

    def test_calculate_shipping_cost(self):
        """Tests the calculate_shipping_cost function."""
        self.assertEqual(calculate_shipping_cost(1, 10, 10, 10), 5)
        self.assertEqual(calculate_shipping_cost(2, 20, 20, 20), 10)
        self.assertEqual(calculate_shipping_cost(5, 30, 30, 30), 10)
        self.assertEqual(calculate_shipping_cost(6, 40, 40, 40), 20)
        self.assertEqual(calculate_shipping_cost(0.5, 15, 15, 15), 20)  # Mixed case

    def test_grade_quiz(self):
        """Tests the grade_quiz function."""
        self.assertEqual(grade_quiz(7, 2), "Pass")
        self.assertEqual(grade_quiz(8, 1), "Pass")
        self.assertEqual(grade_quiz(5, 3), "Conditional Pass")
        self.assertEqual(grade_quiz(6, 3), "Conditional Pass")
        self.assertEqual(grade_quiz(4, 5), "Fail")
        self.assertEqual(grade_quiz(5, 4), "Fail")
        self.assertEqual(grade_quiz(7, 3), "Fail")

    def test_authenticate_user(self):
        """Tests the authenticate_user function."""
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")
        self.assertEqual(authenticate_user("user12", "password123"), "User")
        self.assertEqual(authenticate_user("user", "password123"), "Invalid")  # Username too short
        self.assertEqual(authenticate_user("user12", "pass"), "Invalid")  # Password too short

    def test_get_weather_advisory(self):
        """Tests the get_weather_advisory function."""
        self.assertEqual(get_weather_advisory(35, 80), "High Temperature and Humidity. Stay Hydrated.")
        self.assertEqual(get_weather_advisory(35, 60), "No Specific Advisory")
        self.assertEqual(get_weather_advisory(25, 80), "No Specific Advisory")
        self.assertEqual(get_weather_advisory(-5, 30), "Low Temperature. Bundle Up!")
        self.assertEqual(get_weather_advisory(25, 30), "No Specific Advisory")


class TestWhiteBoxClassTests(unittest.TestCase):
    """
    Unit tests for classes in white_box.py
    """

    def test_vending_machine(self):
        """Tests the VendingMachine class."""
        vm = VendingMachine()
        self.assertEqual(vm.state, "Ready")
        
        # Test insert_coin when ready
        result = vm.insert_coin()
        self.assertEqual(result, "Coin Inserted. Select your drink.")
        self.assertEqual(vm.state, "Dispensing")
        
        # Test insert_coin when dispensing
        result = vm.insert_coin()
        self.assertEqual(result, "Invalid operation in current state.")
        self.assertEqual(vm.state, "Dispensing")
        
        # Test select_drink when dispensing
        result = vm.select_drink()
        self.assertEqual(result, "Drink Dispensed. Thank you!")
        self.assertEqual(vm.state, "Ready")
        
        # Test select_drink when ready
        result = vm.select_drink()
        self.assertEqual(result, "Invalid operation in current state.")
        self.assertEqual(vm.state, "Ready")

    def test_traffic_light(self):
        """Tests the TrafficLight class."""
        tl = TrafficLight()
        self.assertEqual(tl.state, "Red")
        self.assertEqual(tl.get_current_state(), "Red")
        
        tl.change_state()
        self.assertEqual(tl.state, "Green")
        self.assertEqual(tl.get_current_state(), "Green")
        
        tl.change_state()
        self.assertEqual(tl.state, "Yellow")
        self.assertEqual(tl.get_current_state(), "Yellow")
        
        tl.change_state()
        self.assertEqual(tl.state, "Red")
        self.assertEqual(tl.get_current_state(), "Red")

    def test_user_authentication(self):
        """Tests the UserAuthentication class."""
        ua = UserAuthentication()
        self.assertEqual(ua.state, "Logged Out")
        
        # Test login when logged out
        result = ua.login()
        self.assertEqual(result, "Login successful")
        self.assertEqual(ua.state, "Logged In")
        
        # Test login when already logged in
        result = ua.login()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(ua.state, "Logged In")
        
        # Test logout when logged in
        result = ua.logout()
        self.assertEqual(result, "Logout successful")
        self.assertEqual(ua.state, "Logged Out")
        
        # Test logout when already logged out
        result = ua.logout()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(ua.state, "Logged Out")

    def test_document_editing_system(self):
        """Tests the DocumentEditingSystem class."""
        des = DocumentEditingSystem()
        self.assertEqual(des.state, "Editing")
        
        # Test save_document when editing
        result = des.save_document()
        self.assertEqual(result, "Document saved successfully")
        self.assertEqual(des.state, "Saved")
        
        # Test save_document when already saved
        result = des.save_document()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(des.state, "Saved")
        
        # Test edit_document when saved
        result = des.edit_document()
        self.assertEqual(result, "Editing resumed")
        self.assertEqual(des.state, "Editing")
        
        # Test edit_document when already editing
        result = des.edit_document()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(des.state, "Editing")

    def test_elevator_system(self):
        """Tests the ElevatorSystem class."""
        es = ElevatorSystem()
        self.assertEqual(es.state, "Idle")
        
        # Test move_up when idle
        result = es.move_up()
        self.assertEqual(result, "Elevator moving up")
        self.assertEqual(es.state, "Moving Up")
        
        # Test move_up when moving
        result = es.move_up()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(es.state, "Moving Up")
        
        # Test stop when moving
        result = es.stop()
        self.assertEqual(result, "Elevator stopped")
        self.assertEqual(es.state, "Idle")
        
        # Test move_down when idle
        result = es.move_down()
        self.assertEqual(result, "Elevator moving down")
        self.assertEqual(es.state, "Moving Down")
        
        # Test stop when moving
        result = es.stop()
        self.assertEqual(result, "Elevator stopped")
        self.assertEqual(es.state, "Idle")
        
        # Test stop when idle
        result = es.stop()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(es.state, "Idle")

    def test_bank_account(self):
        """Tests the BankAccount class."""
        ba = BankAccount("12345", 1000)
        self.assertEqual(ba.account_number, "12345")
        self.assertEqual(ba.balance, 1000)
        
        # Test view_account (does not return anything)
        # Redirect stdout to capture print output
        import io
        from contextlib import redirect_stdout
        
        f = io.StringIO()
        with redirect_stdout(f):
            ba.view_account()
        
        self.assertEqual(f.getvalue(), "The account 12345 has a balance of 1000\n")

    def test_banking_system(self):
        """Tests the BankingSystem class."""
        bs = BankingSystem()
        self.assertEqual(bs.users, {"user123": "pass123"})
        self.assertEqual(bs.logged_in_users, set())
        
        # Test authentication
        # Redirect stdout to capture print output
        import io
        from contextlib import redirect_stdout
        
        # Test successful authentication
        f = io.StringIO()
        with redirect_stdout(f):
            result = bs.authenticate("user123", "pass123")
        
        self.assertTrue(result)
        self.assertEqual(f.getvalue(), "User user123 authenticated successfully.\n")
        self.assertEqual(bs.logged_in_users, {"user123"})
        
        # Test already logged in
        f = io.StringIO()
        with redirect_stdout(f):
            result = bs.authenticate("user123", "pass123")
        
        self.assertFalse(result)
        self.assertEqual(f.getvalue(), "User already logged in.\n")
        
        # Test failed authentication
        f = io.StringIO()
        with redirect_stdout(f):
            result = bs.authenticate("user456", "pass456")
        
        self.assertFalse(result)
        self.assertEqual(f.getvalue(), "Authentication failed.\n")
        
        # Test transfer_money
        # Test sender not authenticated
        f = io.StringIO()
        with redirect_stdout(f):
            result = bs.transfer_money("user456", "user123", 100, "regular")
        
        self.assertFalse(result)
        self.assertEqual(f.getvalue(), "Sender not authenticated.\n")
        
        # Test invalid transaction type
        f = io.StringIO()
        with redirect_stdout(f):
            result = bs.transfer_money("user123", "user456", 100, "invalid")
        
        self.assertFalse(result)
        self.assertEqual(f.getvalue(), "Invalid transaction type.\n")
        
        # Test successful transfer
        f = io.StringIO()
        with redirect_stdout(f):
            result = bs.transfer_money("user123", "user456", 100, "regular")
        
        self.assertTrue(result)
        self.assertEqual(f.getvalue(), "Money transfer of $100 (regular transfer) from user123 to user456 processed successfully.\n")

    def test_product_and_shopping_cart(self):
        """Tests the Product and ShoppingCart classes."""
        # Test Product
        p1 = Product("Item 1", 10)
        p2 = Product("Item 2", 20)
        
        self.assertEqual(p1.name, "Item 1")
        self.assertEqual(p1.price, 10)
        self.assertEqual(p2.name, "Item 2")
        self.assertEqual(p2.price, 20)
        
        # Test view_product
        import io
        from contextlib import redirect_stdout
        
        f = io.StringIO()
        with redirect_stdout(f):
            result = p1.view_product()
        
        self.assertEqual(result, "The product Item 1 has a price of 10")
        self.assertEqual(f.getvalue(), "The product Item 1 has a price of 10\n")
        
        # Test ShoppingCart
        sc = ShoppingCart()
        self.assertEqual(sc.items, [])
        
        # Test add_product
        sc.add_product(p1)
        self.assertEqual(len(sc.items), 1)
        self.assertEqual(sc.items[0]["product"], p1)
        self.assertEqual(sc.items[0]["quantity"], 1)
        
        # Test add more of the same product
        sc.add_product(p1, 2)
        self.assertEqual(len(sc.items), 1)
        self.assertEqual(sc.items[0]["product"], p1)
        self.assertEqual(sc.items[0]["quantity"], 3)
        
        # Test add a different product
        sc.add_product(p2, 2)
        self.assertEqual(len(sc.items), 2)
        self.assertEqual(sc.items[1]["product"], p2)
        self.assertEqual(sc.items[1]["quantity"], 2)
        
        # Test remove_product
        sc.remove_product(p1, 1)
        self.assertEqual(len(sc.items), 2)
        self.assertEqual(sc.items[0]["quantity"], 2)
        
        # Test remove all of a product
        sc.remove_product(p1, 2)
        self.assertEqual(len(sc.items), 1)
        self.assertEqual(sc.items[0]["product"], p2)
        
        # Test view_cart
        f = io.StringIO()
        with redirect_stdout(f):
            sc.view_cart()
        
        self.assertEqual(f.getvalue(), "2 x Item 2 - $40\n")
        
        # Test checkout
        f = io.StringIO()
        with redirect_stdout(f):
            sc.checkout()
        
        self.assertEqual(f.getvalue(), "Total: $40\nCheckout completed. Thank you for shopping!\n")


if __name__ == "__main__":
    unittest.main()