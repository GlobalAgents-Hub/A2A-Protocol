"""
Core A2A Protocol implementation
"""
import json
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict, Any

from .agents import Peer
from .zones import ZoneManager

class A2A:
    """
    Main class for the A2A Protocol implementation.
    Handles core protocol operations and coordinates between different components.
    """
    def __init__(self, data_file: str = "data.json"):
        self.data_file = Path(data_file)
        self.zone_manager = ZoneManager(self.data_file)
        self._load_data()

    def _load_data(self) -> None:
        """Load protocol data from storage"""
        if self.data_file.exists():
            self.data = json.loads(self.data_file.read_text())
        else:
            self.data = {
                "entities": {},
                "zones": {},
                "interactions": [],
                "logs": []
            }
            self._save_data()

    def _save_data(self) -> None:
        """Save protocol data to storage"""
        self.data_file.write_text(json.dumps(self.data, indent=2))

    def join_zone(self, peer: Peer, zone_name: str) -> bool:
        """
        Join an agent to a specific zone
        
        Args:
            peer: The peer (agent) trying to join the zone
            zone_name: Name of the zone to join
        
        Returns:
            bool: True if joined successfully, False otherwise
        """
        # Create zone if it doesn't exist
        if zone_name not in self.data["zones"]:
            self.zone_manager.create_zone(zone_name)
            self._load_data()  # Reload data after zone creation

        # Add peer to zone if not already present
        if peer.name not in self.data["zones"][zone_name]["entities"]:
            self.data["zones"][zone_name]["entities"].append(peer.name)
            self._save_data()
            return True
        
        return False

    def list_zones(self) -> List[str]:
        """List all available zones"""
        return list(self.data["zones"].keys())

    def get_zone_peers(self, zone_name: str) -> List[str]:
        """Get all peers in a specific zone"""
        return self.data["zones"].get(zone_name, {}).get("entities", [])

    def record_interaction(self, peer1: str, peer2: str, zone: str) -> None:
        """Record an interaction between two peers in a zone"""
        self.data["interactions"].append({
            "timestamp": datetime.now().isoformat(),
            "peers": [peer1, peer2],
            "zone": zone
        })
        self._save_data()

    def get_interactions(self, zone: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get interactions, optionally filtered by zone"""
        if zone is None:
            return self.data["interactions"]
        return [i for i in self.data["interactions"] if i["zone"] == zone]