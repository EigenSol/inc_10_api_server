def printer_decorator(func):
  def wrapper():
    print("--------------")
    func()
    print("--------------")
    print(":CUT")

  return wrapper


# Task

@printer_decorator
def print_name():
  print("Shabbeer")

@printer_decorator
def print_age():
  print("Age: is 33")

print_name()
print_age()


# new_print_name = printer_decorator(print_name)
# new_print_name()

# new_print_age = printer_decorator(print_age)
# new_print_age()

# # Execute

# print("--------------")
# print_name()
# print("--------------")
# print(":CUT")

# print("--------------")
# print_age()
# print("--------------")
# print(":CUT")