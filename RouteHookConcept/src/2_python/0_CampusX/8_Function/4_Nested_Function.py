

# Nested Function
#===================


def f():
    def g():
        print("Print g!")
    g()
    print("Print f!")

f()

# Print g!
# Print f!