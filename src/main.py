import src.maths as maths
import src.helpers as helpers

print("starting app")

x = input("Enter your name: ")
print("Hello " + x)

result = maths.Add(5, 3)
print("Result:", result)

data = helpers.getData()
print("Data:", data)
