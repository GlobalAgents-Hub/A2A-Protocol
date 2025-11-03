"""
Network discovery functionality
"""
from typing import List, Dict, Any, Optional
import socket
import json
import threading
from time import sleep

class NetworkDiscovery:
    """
    Handles peer and zone discovery in the network
    """
    def __init__(self, broadcast_port: int = 5060):
        self.broadcast_port = broadcast_port
        self._running = False
        self._known_peers: Dict[str, Dict[str, Any]] = {}
        self._known_zones: Dict[str, Dict[str, Any]] = {}

    def start(self) -> None:
        """Start the discovery service"""
        self._running = True
        self._start_listener()
        self._start_broadcaster()

    def stop(self) -> None:
        """Stop the discovery service"""
        self._running = False

    def _start_listener(self) -> None:
        """Start listening for discovery broadcasts"""
        thread = threading.Thread(target=self._listen)
        thread.daemon = True
        thread.start()

    def _start_broadcaster(self) -> None:
        """Start broadcasting presence"""
        thread = threading.Thread(target=self._broadcast)
        thread.daemon = True
        thread.start()

    def _listen(self) -> None:
        """Listen for discovery messages"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("", self.broadcast_port))
        sock.settimeout(1)

        while self._running:
            try:
                data, addr = sock.recvfrom(1024)
                message = json.loads(data.decode())
                self._handle_discovery_message(message, addr)
            except socket.timeout:
                continue
            except Exception as e:
                print(f"Error in discovery listener: {e}")

    def _broadcast(self) -> None:
        """Broadcast presence periodically"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        while self._running:
            try:
                message = {
                    "type": "discovery",
                    "peers": list(self._known_peers.keys()),
                    "zones": list(self._known_zones.keys())
                }
                sock.sendto(
                    json.dumps(message).encode(),
                    ("<broadcast>", self.broadcast_port)
                )
            except Exception as e:
                print(f"Error in discovery broadcaster: {e}")
            sleep(5)  # Broadcast every 5 seconds

    def _handle_discovery_message(self, message: Dict[str, Any], addr: tuple) -> None:
        """
        Handle incoming discovery message
        
        Args:
            message: The discovery message
            addr: Address of the sender
        """
        if message.get("type") == "discovery":
            # Update known peers and zones
            for peer in message.get("peers", []):
                if peer not in self._known_peers:
                    self._known_peers[peer] = {"last_seen": addr[0]}
            
            for zone in message.get("zones", []):
                if zone not in self._known_zones:
                    self._known_zones[zone] = {"last_seen": addr[0]}

    def find_peers(self, role: Optional[str] = None) -> List[str]:
        """
        Find peers in the network
        
        Args:
            role: Optional role to filter by
            
        Returns:
            List[str]: List of peer names
        """
        if role:
            return [
                name for name, info in self._known_peers.items()
                if info.get("role") == role
            ]
        return list(self._known_peers.keys())

    def find_zones(self, topic: Optional[str] = None) -> List[str]:
        """
        Find zones in the network
        
        Args:
            topic: Optional topic to filter by
            
        Returns:
            List[str]: List of zone names
        """
        if topic:
            return [
                name for name, info in self._known_zones.items()
                if topic.lower() in name.lower()
            ]
        return list(self._known_zones.keys())