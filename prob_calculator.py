import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **balls):
    self.contents = []
    for key, value in balls.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, number):
    result = []
    if number > len(self.contents):
      return self.contents
    else:
      while number > 0:
        result.append(self.contents.pop(random.randrange(0,len(self.contents))))
        number -= 1
      return result

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
  N = 0
  M = 0
  get_ball = False
   
  for n in range(num_experiments):
    new_hat = copy.deepcopy(hat)
    balls_drawn = new_hat.draw(num_balls_drawn)

    expected_balls_list = []
    for key, value in expected_balls.items():
      for i in range(value):
        expected_balls_list.append(key)

    for ball in expected_balls_list:
      if ball in balls_drawn:
        balls_drawn.remove(ball)
        get_ball = True
      else:
        get_ball = False
        break

    if get_ball:
      M += 1

    N += 1
  
  return M/N