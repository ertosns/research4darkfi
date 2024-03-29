

# This file was *autogenerated* from the file curve.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3618502788666131213697322783095070105623107215331596699973092056135872020481 = Integer(3618502788666131213697322783095070105623107215331596699973092056135872020481); _sage_const_1 = Integer(1); _sage_const_3141592653589793238462643383279502884197169399375105820974944592307816406665 = Integer(3141592653589793238462643383279502884197169399375105820974944592307816406665); _sage_const_874739451078007766457464989774322083649278607533249481151382481072868806602 = Integer(874739451078007766457464989774322083649278607533249481151382481072868806602); _sage_const_152666792071518830868575557812948353041420400780739481342941381225525861407 = Integer(152666792071518830868575557812948353041420400780739481342941381225525861407); _sage_const_3618502788666131213697322783095070105526743751716087489154079457884512865583 = Integer(3618502788666131213697322783095070105526743751716087489154079457884512865583); _sage_const_0 = Integer(0)# stark curve https://docs.starkware.co/starkex/crypto/stark-curve.html

import random


p = _sage_const_3618502788666131213697322783095070105623107215331596699973092056135872020481 
alpha = _sage_const_1 
# $$y^2 = x^3 + \alpha \dot x + \beta$$  (mod p)
beta = _sage_const_3141592653589793238462643383279502884197169399375105820974944592307816406665 
F = GF(p)
E = EllipticCurve(F, [alpha,beta])
ec_order = E.order()
# ECDSA scheme generator
G_generator = E(_sage_const_874739451078007766457464989774322083649278607533249481151382481072868806602 , _sage_const_152666792071518830868575557812948353041420400780739481342941381225525861407 )
p_scalar = _sage_const_3618502788666131213697322783095070105526743751716087489154079457884512865583 
K = GF(p_scalar)


class CurvePoint():
      def __init__(self, x=None, y=None):
          if x==None or y==None:
             self.point = CurvePoint.random()
          else:
                self.point = E(x,y)
          self.x = self.point[_sage_const_0 ]
          self.y = self.point[_sage_const_1 ]

      def zero():
            return G_generator * _sage_const_0 

      def __repr__(self):
          return bytes("[ x: {}, y: {}, z: 1]".format(self.x, self.y), encoding='utf-8')

      def __str__(self):
          return self.__repr__()

      def random(max=p):
          return G_generator * random.randint(_sage_const_0 , max)

      def __add__(self, rhs):
          return self.point + rhs.point

      def __sub__(self, rhs):
          return self.point - rhs.point

      def __neg__(self):
          return -_sage_const_1  * self.point

      def generator():
          return G_generator

      def __mul__(self, factor):
          return factor * self.point

      def msm(points, scalars):
          assert len(points) == len(scalars), 'len(p): {}, len(s): {}'.format(len(points), len(scalars))
          return sum([s*p for (s, p) in zip(points, scalars)])

