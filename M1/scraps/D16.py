class Creature:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __str__(self):
        return f"{self.name} has power {self.power}"

    def __repr__(self):
        return f"Creature('{self.name}', {self.power})"


a = Creature("Dragon", 999)
b = Creature("Wolf", 250)


print("1:", a)
print("2:", str(b))
print("3:", repr(a))
print("4:", [a, b])
print("5:", f"Fight: {a} vs {b}")
print("6:", f"Debug: {a!r} vs {b!r}")

# Reconstruct test
creature_text = repr(a)
new_a = eval(creature_text)
print("7:", new_a)

print("8:", type(new_a), new_a.name == a.name and new_a.power == a.power)
