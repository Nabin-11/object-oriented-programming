# Understanding Object Creation in Python

# ============================================
# 1. EXPLICIT CLASS INSTANTIATION
# ============================================
class Dog:
    def __init__(self, name):
        self.name = name

# Explicit syntax to create an object
dog1 = Dog("Buddy")  # Calls Dog.__init__()
print(type(dog1))  # <class '__main__.Dog'>
print(dog1.name)   # Buddy

# ============================================
# 2. BUILT-IN TYPES (int, str, list, etc.)
# ============================================
# These ALSO use the same syntax! Python just hides it.

# Both of these are EQUIVALENT:
x = 5              # Implicit/shorthand syntax
x = int(5)         # Explicit syntax (same thing!)

print(type(x))     # <class 'int'>
print(x)           # 5

# ============================================
# 3. THEY FOLLOW THE SAME PATTERN
# ============================================

# Custom class
class MyClass:
    def __init__(self, value):
        self.value = value

obj1 = MyClass(10)   # Explicit constructor call
print(f"obj1 type: {type(obj1)}")
print(f"obj1.value: {obj1.value}")

# Built-in int class
num1 = int(10)       # Same pattern - calling the class as a constructor
print(f"num1 type: {type(num1)}")
print(f"num1 value: {num1}")

# ============================================
# 4. PYTHON'S SYNTACTIC SUGAR
# ============================================
# Python provides shortcuts for literals:

# These are all equivalent:
s1 = "hello"           # Literal (syntactic sugar)
s2 = str("hello")      # Explicit constructor

l1 = [1, 2, 3]         # Literal (syntactic sugar)
l2 = list([1, 2, 3])   # Explicit constructor

d1 = {"a": 1}          # Literal (syntactic sugar)
d2 = dict({"a": 1})    # Explicit constructor

print("\n--- All equivalent ---")
print(f"s1 == s2: {s1 == s2}")
print(f"l1 == l2: {l1 == l2}")
print(f"d1 == d2: {d1 == d2}")

# ============================================
# 5. BEHIND THE SCENES
# ============================================
# When you write: x = 5
# Python actually does: x = int.__new__(int), then int.__init__(x, 5)
# It's the same as calling: x = int(5)

# When you write: dog = Dog("Buddy")
# Python does: dog = Dog.__new__(Dog), then Dog.__init__(dog, "Buddy")

print("\n--- Proof they're the same ---")
print(f"int(5) creates: {type(int(5))}")
print(f"5 creates: {type(5)}")
print(f"Are they equal? {int(5) == 5}")

print(f"\nstr('hello') creates: {type(str('hello'))}")
print(f"'hello' creates: {type('hello')}")
print(f"Are they equal? {str('hello') == 'hello'}")
