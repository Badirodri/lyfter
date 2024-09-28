# Cree las siguientes clases:
# Head
# Torso
# Arm
# Hand
# Leg
# Feet
# Ahora cree una clase de Human y conecte todas las clases de manera lógica por medio de atributos.

# class Torso:
# 	def __init__(self, head, right_arm, ...):
# 		self.head = head
# 		self.right_arm = right_arm
# 		...

# class Arm:
# 	def __init__(self, hand):
# 		self.hand = hand


# right_hand = Hand()
# right_arm = Arm(right_hand)
# torso = (head, right_arm)

class Head:
  def __init__(self):
    print('   ( . _ . )')

class Torso:
  def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
    self.head = head
    self.right_arm = right_arm
    self.left_arm = left_arm
    self.right_leg = right_leg
    self.left_leg = left_leg

class Arm:
  def __init__(self,hand):
    self.hand = hand


class Hand:
  def __init__(self):
    print ('--          --')

class Leg:
  def __init__(self,leg):
    self.leg= leg

class Feet:
  def __init__(self):
    print ('_/          |_')

head = Head()
right_hand= Hand()
left_hand= Hand()
right_feet= Feet()
left_feet= Feet()
right_arm= Arm(right_hand)
left_arm= Arm(left_hand)
right_leg = Leg(right_feet)
left_leg = Leg(left_feet)
torso=(head, right_arm, left_arm, right_leg, left_leg)

print (torso)