class Node:
    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power
        self.next = None

def add_polynomials(poly1, poly2):
    dummy = Node(0, 0)
    tail = dummy
    while poly1 and poly2:
        if poly1.power > poly2.power:
            tail.next = Node(poly1.coeff, poly1.power)
            poly1 = poly1.next
        elif poly1.power < poly2.power:
            tail.next = Node(poly2.coeff, poly2.power)
            poly2 = poly2.next
        else:
            tail.next = Node(poly1.coeff + poly2.coeff, poly1.power)
            poly1 = poly1.next
            poly2 = poly2.next
        tail = tail.next
    tail.next = poly1 or poly2
    return dummy.next

def print_polynomial(poly):
    while poly:
        print(f"{poly.coeff}x^{poly.power}", end=" + " if poly.next else "\n")
        poly = poly.next

# Example
poly1 = Node(3, 3)
poly1.next = Node(4, 2)

poly2 = Node(5, 3)
poly2.next = Node(6, 2)

print("Polynomial 1: ", end="")
print_polynomial(poly1)
print("Polynomial 2: ", end="")
print_polynomial(poly2)

result = add_polynomials(poly1, poly2)
print("Resultant Polynomial: ", end="")
print_polynomial(result)
