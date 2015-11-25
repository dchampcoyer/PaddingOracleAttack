# PaddingOracleAttack
Summary:
Demonstrates a padding oracle attack to decrypt and encrypted message

Language: python

Description:
  poattack.attack() is the code that I wrote to execute the padding oracle attack and decrypt the message.
  The necessary steps to execute the code are:
  >>> import po1 as po
  >>> import poattack
  >>> import os
  >>> po.key = os.urandom(16)
  >>> c = po.enc('hello')
  >>> poattack.attack(c)
