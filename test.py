"""
# combining positional and keyword arguments
print('Number one portal is {0}, {1}, and {other}.'.format('Geeks', 'For', other ='Geeks'))

# using format() method with number 
print("Geeks :{0:2d}, Portal :{1:8.2f}".format(12, 00.546))

# Changing positional argument
print("Second argument: {1:3d}, first one: {0:7.2f}".format(47.42, 11))

print("Geeks: {a:5d},  Portal: {p:8.2f}".format(a = 453, p = 59.058))/
"""
print("-"*50)
name = "Sirinthorn Cheyasak"
height = 173
weight = 65
bmi = weight/(height*0.01)**2
#print(f"{'Name':<10} {'Score':>5}")
print(f"{"Name":<12} {":":>2} {name:<25}")
print(f"{"Height":<12} {":":>2} {height:>7.1f} {"CM":>3}")
print(f"{"Weight":<12} {":":>2} {weight:>7.1f} {"KG":>3}")
print("-"*50)
print(f"{"Your BMI":<12} {":":>2} {bmi:>7.2f}")
print("-"*50)