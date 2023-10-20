class python:
    def findPerSqr(self, x):
        return 4*x

print("Enter Length: ", end="")
s = float(input())

ob = python()
p = ob.findPerSqr(s)

print("\nPerimeter = {:.2f}".format(p))