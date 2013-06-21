class Player:
  name = None

  def greet(self):
    if self.name is None:
      return "welcome guest!"
    else:
      return self.name + ", Welcome"



james = Player()

noah = Player()

james.name = "Sharmech"

print(james.greet())
print(noah.greet())
