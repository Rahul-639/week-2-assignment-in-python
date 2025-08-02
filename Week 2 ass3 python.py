class Node:
    def __init__(self, coeff, pow):
        self.coeff = coeff
        self.pow = pow
        self.next = None

def add_polynomials(poly1, poly2):
    dummy = Node(0, 0)
    tail = dummy

    while poly1 and poly2:
        if poly1.pow > poly2.pow:
            tail.next = Node(poly1.coeff, poly1.pow)
            poly1 = poly1.next
        elif poly1.pow < poly2.pow:
            tail.next = Node(poly2.coeff, poly2.pow)
            poly2 = poly2.next
        else:
            tail.next = Node(poly1.coeff + poly2.coeff, poly1.pow)
            poly1 = poly1.next
            poly2 = poly2.next
        tail = tail.next

    while poly1:
        tail.next = Node(poly1.coeff, poly1.pow)
        tail = tail.next
        poly1 = poly1.next
    while poly2:
        tail.next = Node(poly2.coeff, poly2.pow)
        tail = tail.next
        poly2 = poly2.next

    return dummy.next

def print_polynomial(head):
    while head:
        print(f"{head.coeff}x^{head.pow}", end=" -> " if head.next else "\n")
        head = head.next

# Example
# Poly1: x^3 + 2x^2
poly1 = Node(1, 3)
poly1.next = Node(2, 2)

# Poly2: 3x^3 + 4x^2
poly2 = Node(3, 3)
poly2.next = Node(4, 2)

result = add_polynomials(poly1, poly2)
print("Sum of Polynomials:")
print_polynomial(result)
