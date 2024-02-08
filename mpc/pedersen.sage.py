

# This file was *autogenerated* from the file pedersen.sage
from sage.all_cmdline import *   # import sage library

_sage_const_0 = Integer(0)
load('curve.sage')

class PedersenCommitment(object):
      def __init__(self, value, blinder=None):
          self.value = value
          self.blinder = blinder if blinder is not None else random.randint(_sage_const_0 ,p)

      def commitment(self):
          return CurvePoint.generator() * self.value + CurvePoint.generator() * self.blinder

