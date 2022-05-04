# Написать программу, которая будет выводить приветствие с именем

name = 'Ivan'
print("v.1: Hello, Ivan")
print("v.2: Hello, " + name)
print("v.3: Hello, %s" % name)
print("v.4: Hello, {}".format(name))
print("v.5: Hello, {0}".format(name))
print("v.6: Hello, {name}".format(name=name))
print(f"v.7: Hello, {name}")
