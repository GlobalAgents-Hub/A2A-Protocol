"""
Event handling system
"""
from typing import Dict, List, Callable, Any
from dataclasses import dataclass, field

@dataclass
class EventHandler:
    """
    Handles event registration and dispatching
    """
    _handlers: Dict[str, List[Callable]] = field(default_factory=dict)

    def on(self, event: str) -> Callable:
        """
        Register an event handler
        
        Args:
            event: Event name to handle
            
        Returns:
            Callable: Decorator function
        """
        def decorator(func: Callable) -> Callable:
            if event not in self._handlers:
                self._handlers[event] = []
            self._handlers[event].append(func)
            return func
        return decorator

    def emit(self, event: str, data: Any = None) -> None:
        """
        Emit an event
        
        Args:
            event: Name of the event to emit
            data: Data to pass to event handlers
        """
        for handler in self._handlers.get(event, []):
            try:
                handler(data)
            except Exception as e:
                print(f"Error in event handler: {e}")

    def remove_handler(self, event: str, handler: Callable) -> bool:
        """
        Remove an event handler
        
        Args:
            event: Event name
            handler: Handler function to remove
            
        Returns:
            bool: True if handler was removed, False otherwise
        """
        if event in self._handlers and handler in self._handlers[event]:
            self._handlers[event].remove(handler)
            return True
        return False

    def clear_handlers(self, event: str = None) -> None:
        """
        Clear all handlers for an event or all events
        
        Args:
            event: Optional event name. If None, clears all handlers
        """
        if event:
            self._handlers[event] = []
        else:
            self._handlers.clear()