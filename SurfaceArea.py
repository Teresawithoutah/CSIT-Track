l = float(input("Enter integer for LENGTH of rectangular prism: "))
w = float(input("Enter integer for WIDTH of rectangular prism: "))
h = float(input("Enter integer for HEIGHT of rectangular prism: "))

surface_area = (2 * l * w + 2 * (l + w) * h)

print("Surface Area:", round(surface_area, 2), "square feet")
