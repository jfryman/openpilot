from selfdrive.car.interfaces import CarInterfaceBase
from selfdrive.car import gen_empty_fingerprint

class CarInterface(CarInterfaceBase):
  @staticmethod
  def get_params(candidate, fingerprint=gen_empty_fingerprint(), car_fw=None):
    ret = CarInterfaceBase.get_std_params(candidate, fingerprint)
    return ret

  # returns a car.CarState
  def update(self, c, can_strings):
    return self.CS.out

  def apply(self, c):
    can_sends = self.CC.update(c.enabled, self.CS, self.frame)
    self.frame += 1
    
    return can_sends

