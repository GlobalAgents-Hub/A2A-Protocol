"""
A2A Protocol - A decentralized protocol for agent communication
"""

from .core import A2A
from .agents import Peer, AgentBuilder
from .zones import ZoneManager
from .events import EventHandler
from .discovery import NetworkDiscovery

__version__ = "0.1.0"
__all__ = ['A2A', 'Peer', 'AgentBuilder', 'ZoneManager', 'EventHandler', 'NetworkDiscovery']