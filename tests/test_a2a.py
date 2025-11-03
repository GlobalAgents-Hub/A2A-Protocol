import pytest
from a2a import spawn, create_zone, load_data

def test_spawn():
    """Test agent spawning functionality"""
    data = load_data()
    initial_count = len(data["entities"])
    
    # Test creating a new agent
    result = spawn("test_agent")
    assert result == True
    
    # Verify agent was created
    data = load_data()
    assert len(data["entities"]) == initial_count + 1
    assert "test_agent" in data["entities"]

def test_create_zone():
    """Test zone creation functionality"""
    data = load_data()
    initial_count = len(data["zones"])
    
    # Test creating a new zone
    result = create_zone("test_zone")
    assert result == True
    
    # Verify zone was created
    data = load_data()
    assert len(data["zones"]) == initial_count + 1
    assert "test_zone" in data["zones"]

def test_duplicate_spawn():
    """Test spawning duplicate agent names"""
    # First spawn should succeed
    result1 = spawn("duplicate_agent")
    assert result1 == True
    
    # Second spawn with same name should fail
    result2 = spawn("duplicate_agent")
    assert result2 == False