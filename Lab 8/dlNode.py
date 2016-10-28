"""
Nodes
file: dlNode.py
author: michael j o'connor
"""

from rit_lib import *


class dlNode(struct):
    """
    this class describes the nodes used in the circular, doubly-linked list
    """
    _slots = ((object,'data'),
              (bool, 'turn'),
              (('dlNode',NoneType),'prev'),
              (('dlNode',NoneType),'next'))

