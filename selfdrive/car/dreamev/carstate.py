from cereal import car
from selfdrive.car.interfaces import CarStateBase

class CarState(CarStateBase):
  def update(self, cp):
    ret = car.CarState.new_message()
    return ret
