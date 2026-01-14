

```
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

**Test Cases:**
```
Test 1 (normal): input → expected output
Test 2 (edge):   input → expected output
Test 3 (error):  input → expected output
```

---

## I - IMPLEMENT
[Write your actual Python code with type hints and docstring]

```python
def function_name(param: type) -> return_type:
    """[Description]

    Args:
        param: [description]

    Returns:
        [description]
    """
    pass
```

---

## R - REVIEW
[Test your code, find bugs, verify edge cases]

**Test Results:** [which tests passed/failed?]
**Bugs Fixed:** [what bugs did you find and fix?]
**Quality Check:** [type hints? docstring? clear names? no magic numbers?]

---

## E - EVALUATE
[Analyze time/space complexity and possible improvements]

**Time Complexity:** O(___) because [explanation]
**Space Complexity:** O(___) because [explanation]
**Improvements:** [could you optimize further?]
**Learned:** [what did you learn from this problem?]
