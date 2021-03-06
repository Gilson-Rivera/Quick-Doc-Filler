
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '9ECF222301EBAA28F6B2331CF8CD8182'
    
_lr_action_items = {'EMAIL':([3,4,],[6,-7,]),'ID':([3,4,8,],[5,-7,10,]),'$end':([1,2,3,4,5,7,8,9,11,15,],[-1,0,-6,-7,-9,-5,-8,-4,-3,-2,]),'DATE':([13,],[14,]),'NAME':([0,3,4,6,10,12,14,],[4,8,-7,9,11,13,15,]),'SAL':([10,],[12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'program':([0,],[2,]),'param':([3,],[7,]),'command':([0,],[3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement','program',1,'p_program','Parser Draft.py',15),
  ('statement -> command NAME ID SAL NAME DATE NAME','statement',7,'p_statement','Parser Draft.py',21),
  ('statement -> command NAME ID NAME','statement',4,'p_statement','Parser Draft.py',22),
  ('statement -> command EMAIL NAME','statement',3,'p_statement','Parser Draft.py',23),
  ('statement -> command param','statement',2,'p_statement','Parser Draft.py',24),
  ('statement -> command','statement',1,'p_statement','Parser Draft.py',25),
  ('command -> NAME','command',1,'p_command_add','Parser Draft.py',46),
  ('param -> NAME','param',1,'p_param','Parser Draft.py',53),
  ('param -> ID','param',1,'p_param','Parser Draft.py',54),
]
