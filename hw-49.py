class Ecommerce:
     def __init__(self, base_price, discount=0, tax=0):
        self.base_price=base_price
        self.discount=discount
        self.tax=tax
     def calculate_final_price(self):
        if self.base_price<0 or self.discount<0 or self.tax<0:
            raise ValueError("Should not be Negative values")
        else:
            discount_percent=self.base_price*(self.discount/100)
            tax_percent=self.base_price*(self.tax/100)            
            final=self.base_price+tax_percent-discount_percent
            return final
try:
    base_price=float(input("Enter the original price of product: "))
    discount=float(input("Enter the discount percentage: "))
    tax=float(input("Enter the tax percentage: "))
    product=Ecommerce(base_price,discount,tax)
    price=product.calculate_final_price()
    print(f"Total price: {price:.2f}")
except ValueError as e:
    print(e)


    
