"""
Exercise 4.2: Open/Closed Principle (OCP)

OPEN/CLOSED PRINCIPLE

Definition: Software entities should be OPEN for extension but CLOSED for modification.

In other words:
- You should be able to ADD new functionality (open for extension)
- WITHOUT changing existing code (closed for modification)

WHY IS THIS IMPORTANT?

BAD APPROACH (violates OCP):

    class PriceCalculator:
        def calculate_discount(self, price, discount_type):
            if discount_type == "percentage":
                return price * 0.10
            elif discount_type == "fixed":
                return 5.0
            elif discount_type == "bogo":
                return price * 0.50
            # Every time you add a new discount type, you MODIFY this method!
            # This violates OCP

Problems:
1. Every new discount requires CHANGING existing code
2. Risk of breaking existing functionality
3. Must retest entire method
4. Can't add discounts without access to source code

GOOD APPROACH (follows OCP):

    from abc import ABC, abstractmethod

    class DiscountStrategy(ABC):
        @abstractmethod
        def calculate(self, price: float) -> float:
            pass

    class PercentageDiscount(DiscountStrategy):
        def __init__(self, percentage: float):
            self.percentage = percentage

        def calculate(self, price: float) -> float:
            return price * (self.percentage / 100)

    class FixedDiscount(DiscountStrategy):
        def __init__(self, amount: float):
            self.amount = amount

        def calculate(self, price: float) -> float:
            return min(self.amount, price)

    # Adding a NEW discount? Just create a new class!
    class SeasonalDiscount(DiscountStrategy):
        def calculate(self, price: float) -> float:
            return price * 0.15

Benefits:
1. Add new discounts WITHOUT modifying existing code
2. Each discount is independent and testable
3. No risk of breaking existing discounts
4. Plugin architecture - anyone can add discounts

===================================
EXERCISE: E-commerce Discount System
===================================

PART 3: ShoppingCart

The shopping cart applies discount strategies.

Class: ShoppingCart

Attributes:
- items: list[tuple[str, float]] - List of (item_name, price) tuples
- discount_strategy: DiscountStrategy - Current discount strategy

Methods:
- __init__(): Initialize empty cart with NoDiscount strategy
- add_item(name: str, price: float): Add item to cart
- set_discount(strategy: DiscountStrategy): Change discount strategy
- get_subtotal() -> float: Sum of all item prices
- get_discount_amount() -> float: Total discount using current strategy
- get_total() -> float: Subtotal - discount amount
- checkout() -> dict: Return summary with subtotal, discount, and total

---

CHALLENGE PART 4: Stacked Discounts (OPTIONAL - for extra practice)

Some stores allow multiple discounts to stack (e.g., 10% off + $5 coupon).

Class: StackedDiscount (inherits from DiscountStrategy)

Attributes:
- strategies: list[DiscountStrategy] - List of discount strategies to apply

Methods:
- __init__(*strategies): Accept multiple discount strategies
- calculate(price): Apply each discount in sequence to the remaining price
  Example: $100 item with 10% off + $5 off:
    - After 10% off: $100 - $10 = $90
    - After $5 off: $90 - $5 = $85
    - Total discount: $15

This demonstrates OCP: You can combine existing strategies WITHOUT modifying them!

---

LEARNING OBJECTIVES:

1. Understand that new functionality shouldn't require changing existing code
2. See how abstraction enables extensibility
3. Practice the Strategy pattern (a design pattern based on OCP)
4. Learn to think about plugin architectures

ESTIMATED TIME: 45-60 minutes
"""

from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    
    @abstractmethod
    def calculate(price: float) -> float:
        pass


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage:float):
        if percentage > 100:
            raise ValueError("Percentage cannot be over 100")
        self.percentage = percentage

    def calculate(self, price:float):
        discount_amount = (price * self.percentage) / 100
        return discount_amount 


class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, discount_amount:float):
        self.discount_amount = discount_amount

    def calculate(self, price:float ):
        return min(price, self.discount_amount)

class BuyOneGetOneFree(DiscountStrategy):
    def calculate(self, price:float):
        return price/2

class NoDiscount(DiscountStrategy):
    def calculate(self, price:float):
        return 0.0

class ShoppingCart():
    def __init__(self):
        self.discount_strategy = NoDiscount()
        self.items = []

    def add_item(self, name: str, price: float):
        self.items.append(tuple([name, price]))

    def set_discount(self, strategy: DiscountStrategy):
        self.discount_strategy = strategy

    def get_discount_amount(self):
      return self.discount_strategy.calculate(self.get_subtotal())

    def get_subtotal(self) -> float: 
        total = 0
        for tup in self.items:
            price = tup[1]
            total += price
        return total

    def get_total(self):
        sub_total = self.get_subtotal()
        discount = self.get_discount_amount()
        return sub_total - discount

    def checkout(self):
        summery = {"subtotal": self.get_subtotal(), "discount": self.get_discount_amount(), "total": self.get_total() }
        return summery
    
    
class StackedDiscount(DiscountStrategy):
    def __init__(self, *strategies:DiscountStrategy):
        self.strategy_list = strategies


    def calculate(self, price:float):
        remaining_price = price
        total_discount = 0
        discount = 0
        for strategy in self.strategy_list:
            discount = strategy.calculate(remaining_price)
            remaining_price -= discount 
            total_discount += discount
            
        return total_discount
# # ==========================================
# TEST
# ==========================================

if __name__ == "__main__":
    print("\n=== Test 6: ShoppingCart - basic operations ===")
    cart = ShoppingCart()
    cart.add_item("Laptop", 1000.0)
    cart.add_item("Mouse", 25.0)
    cart.add_item("Keyboard", 75.0)

    subtotal = cart.get_subtotal()
    assert subtotal == 1100.0, f"Subtotal should be $1100, got ${subtotal}"
    print(f"✓ Subtotal correct: ${subtotal}")

    print("\n=== Test 7: ShoppingCart - applying discounts ===")

    # No discount (default)
    total = cart.get_total()
    assert total == 1100.0, "Total with no discount should be $1100"
    print(f"✓ No discount: ${total}")

    # 10% discount
    cart.set_discount(PercentageDiscount(10))
    discount_amount = cart.get_discount_amount()
    total = cart.get_total()
    assert discount_amount == 110.0, f"10% discount should be $110, got ${discount_amount}"
    assert total == 990.0, f"Total after 10% discount should be $990, got ${total}"
    print(f"✓ 10% discount: -${discount_amount}, total: ${total}")

    # Fixed $50 discount
    cart.set_discount(FixedAmountDiscount(50.0))
    discount_amount = cart.get_discount_amount()
    total = cart.get_total()
    assert discount_amount == 50.0, f"Fixed discount should be $50, got ${discount_amount}"
    assert total == 1050.0, f"Total after $50 discount should be $1050, got ${total}"
    print(f"✓ Fixed $50 discount: -${discount_amount}, total: ${total}")

    # BOGO
    cart.set_discount(BuyOneGetOneFree())
    discount_amount = cart.get_discount_amount()
    total = cart.get_total()
    assert discount_amount == 550.0, f"BOGO discount should be $550, got ${discount_amount}"
    assert total == 550.0, f"Total after BOGO should be $550, got ${total}"
    print(f"✓ BOGO discount: -${discount_amount}, total: ${total}")

    print("\n=== Test 8: ShoppingCart - checkout ===")
    cart.set_discount(PercentageDiscount(15))
    summary = cart.checkout()
    assert summary["subtotal"] == 1100.0
    assert summary["discount"] == 165.0  # 15% of 1100
    assert summary["total"] == 935.0
    print(f"✓ Checkout summary: {summary}")

    print("\n=== Test 9: OCP Demonstration - Add new discount without modifying existing code ===")

    # Imagine the business wants a VIP discount (25% off)
    # We can add it WITHOUT touching existing code!
    class VIPDiscount(DiscountStrategy):
        def calculate(self, price: float) -> float:
            return price * 0.25

    cart.set_discount(VIPDiscount())
    discount_amount = cart.get_discount_amount()
    assert discount_amount == 275.0, f"VIP 25% discount should be $275, got ${discount_amount}"
    print(f"✓ Added VIPDiscount without modifying existing code!")

    print("\n=== Test 10: Polymorphism - list of different discounts ===")
    discounts = [
        PercentageDiscount(10),
        FixedAmountDiscount(20),
        BuyOneGetOneFree(),
        NoDiscount()
    ]

    for discount in discounts:
        amount = discount.calculate(100.0)
        print(f"  {discount.__class__.__name__}: ${amount:.2f} off")

    print("✓ All discount types work polymorphically")

    print("\n=== OPTIONAL Test 11: Stacked Discounts ===")

    stacked = StackedDiscount(
        PercentageDiscount(10),  # 10% off
        FixedAmountDiscount(5)   # Then $5 off
    )
    # $100 - 10% = $90, then $90 - $5 = $85
    # Total discount: $15
    discount_amount = stacked.calculate(100.0)
    assert discount_amount == 15.0, f"Stacked discount should be $15, got ${discount_amount}"
    print(f"✓ Stacked discounts work: ${discount_amount} total discount")

    cart.set_discount(stacked)
    total = cart.get_total()
    # $1100 - 10% = $990, then $990 - $5 = $985
    assert total == 985.0, f"Cart with stacked discount should be $985, got ${total}"
    print(f"✓ Cart with stacked discount: ${total}")

    print("\n✓ All tests passed!")
    print("\n=== OCP Benefits Demonstrated ===")
    print("1. Added VIPDiscount without modifying existing classes")
    print("2. Each discount strategy is independent and testable")
    print("3. ShoppingCart works with ANY discount strategy")
    print("4. Easy to extend with new discount types")