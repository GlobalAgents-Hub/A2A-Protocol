"""
Zone management functionality
"""
import json
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime

class ZoneManager:
    """
    Manages zones in the A2A network
    """
    def __init__(self, data_file: str = "data.json"):
        self.data_file = Path(data_file)
        self._load_data()

    def _load_data(self) -> None:
        """Load zone data from storage"""
        if self.data_file.exists():
            self.data = json.loads(self.data_file.read_text())
        else:
            self.data = {"zones": {}}
            self._save_data()

    def _save_data(self) -> None:
        """Save zone data to storage"""
        self.data_file.write_text(json.dumps(self.data, indent=2))

    def create_zone(self, name: str, metadata: Optional[Dict[str, Any]] = None) -> bool:
        """
        Create a new zone
        
        Args:
            name: Name of the zone to create
            metadata: Optional metadata for the zone
            
        Returns:
            bool: True if zone was created, False if it already existed
        """
        if name in self.data["zones"]:
            return False

        self.data["zones"][name] = {
            "name": name,
            "created_at": datetime.now().isoformat(),
            "entities": [],
            "metadata": metadata or {}
        }
        self._save_data()
        return True

    def delete_zone(self, name: str) -> bool:
        """
        Delete a zone
        
        Args:
            name: Name of the zone to delete
            
        Returns:
            bool: True if zone was deleted, False if it didn't exist
        """
        if name not in self.data["zones"]:
            return False

        del self.data["zones"][name]
        self._save_data()
        return True

    def list_zones(self) -> List[str]:
        """
        List all available zones
        
        Returns:
            List[str]: List of zone names
        """
        return list(self.data["zones"].keys())

    def get_zone(self, name: str) -> Optional[Dict[str, Any]]:
        """
        Get details about a specific zone
        
        Args:
            name: Name of the zone
            
        Returns:
            Optional[Dict[str, Any]]: Zone details if found, None otherwise
        """
        return self.data["zones"].get(name)

    def add_to_zone(self, zone_name: str, entity_name: str) -> bool:
        """
        Add an entity to a zone
        
        Args:
            zone_name: Name of the zone
            entity_name: Name of the entity to add
            
        Returns:
            bool: True if entity was added, False if zone doesn't exist
        """
        if zone_name not in self.data["zones"]:
            return False

        if entity_name not in self.data["zones"][zone_name]["entities"]:
            self.data["zones"][zone_name]["entities"].append(entity_name)
            self._save_data()

        return True

    def remove_from_zone(self, zone_name: str, entity_name: str) -> bool:
        """
        Remove an entity from a zone
        
        Args:
            zone_name: Name of the zone
            entity_name: Name of the entity to remove
            
        Returns:
            bool: True if entity was removed, False if zone doesn't exist
        """
        if zone_name not in self.data["zones"]:
            return False

        if entity_name in self.data["zones"][zone_name]["entities"]:
            self.data["zones"][zone_name]["entities"].remove(entity_name)
            self._save_data()

        return True

    def get_zone_entities(self, zone_name: str) -> List[str]:
        """
        Get all entities in a zone
        
        Args:
            zone_name: Name of the zone
            
        Returns:
            List[str]: List of entity names in the zone
        """
        return self.data["zones"].get(zone_name, {}).get("entities", [])