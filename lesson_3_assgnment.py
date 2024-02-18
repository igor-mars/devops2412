# Write the following code: a = 1/0;
'''
try:
    a = 1/0
except BaseException as e:
    print(e.args)
'''

# 3. Is the following code legal?
'''
try:
    x = 1
finally:
    print("finally")
'''
# Answer: This code will, but won't catch exceptions

# 4 What exception types can be caught by the
# following handler?
# Except:

# Answer: When the type of Exception isn't specified, all types of errors will be treated.


# 5. What is wrong with using the above type of
# exception handler?
# Answer: With the such approach to handling errors will be hard to understand what
# the more specific reason for error. More specific in catching different types of errors -
# easier to debug/in runtime


# 6. What exceptions can be caught by the
# following handlers?
# ...
# except IOError - Answer: this error is related to issues with Input and Output operations,
# mostly, it is about reading/writing to/from files.(file not exists, file's permissions, file not found)
# …
# except ZeroDivisionError - Answer: handles case of division by zero


# 7. Create a text file named “words.txt”
# programmatically
filename = "words.txt"
my_file = open(filename, "w")

# 8 Write your name into the file
my_file.write("Igor")
my_file.close()

# 9 Read your file content and print it
my_file = open(filename, "r")
content = my_file.read()
print(content)
my_file.close()

# 10. Write Hebrew content into your text file and
# print its content programmatically.
encoding = "utf-8"
my_file = open(filename, "w+", encoding=encoding)
my_file.write("שלום, פייטון")
my_file.seek(0)
print(my_file.read())
my_file.close()

# Challenge:
# 11. Create an image from code (png file) Hint:
# use Pillow
# Answer - ChatGPT
from PIL import Image, ImageDraw

# Create a new blank image with a white background
width, height = 300, 200
image = Image.new("RGB", (width, height), "white")

# Create a drawing context
draw = ImageDraw.Draw(image)

# Draw a red rectangle on the image
left_top = (50, 50)
right_bottom = (250, 150)
draw.rectangle([left_top, right_bottom], outline="red", width=5)

# Save the image as a PNG file
image.save("example.png")

# Optionally, you can display the image using a viewer or a library like Matplotlib
image.show()
