"""
Agent management and peer functionality
"""
import socket
import threading
import json
from typing import Optional, List, Dict, Any, Callable
from dataclasses import dataclass, field

@dataclass
class Peer:
    """
    Represents a peer (agent) in the network
    """
    name: str
    role: str
    port: int = 5050
    zone: Optional[str] = None
    capabilities: List[str] = field(default_factory=list)
    _event_handlers: Dict[str, List[Callable]] = field(default_factory=dict)

    def __post_init__(self):
        self._server = None
        self._running = False

    def start(self) -> None:
        """Start the peer server"""
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.bind(("", self.port))
        self._server.listen()
        self._running = True
        
        # Start listener thread
        thread = threading.Thread(target=self._listen)
        thread.daemon = True
        thread.start()

    def stop(self) -> None:
        """Stop the peer server"""
        self._running = False
        if self._server:
            self._server.close()

    def _listen(self) -> None:
        """Listen for incoming connections"""
        while self._running:
            try:
                conn, addr = self._server.accept()
                thread = threading.Thread(target=self._handle_connection, args=(conn, addr))
                thread.daemon = True
                thread.start()
            except:
                if self._running:  # Only log if we're still supposed to be running
                    print(f"Error in peer {self.name} listener")

    def _handle_connection(self, conn: socket.socket, addr: tuple) -> None:
        """Handle an incoming connection"""
        try:
            data = conn.recv(1024)
            if data:
                message = json.loads(data.decode())
                self._trigger_event('message_received', message)
                conn.send(json.dumps({"status": "ok"}).encode())
        except Exception as e:
            print(f"Error handling connection: {e}")
        finally:
            conn.close()

    def send(self, message: Any, target_port: int = 5050) -> bool:
        """
        Send a message to another peer
        
        Args:
            message: The message to send
            target_port: Port of the target peer
            
        Returns:
            bool: True if message was sent successfully
        """
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(("localhost", target_port))
            client.send(json.dumps(message).encode())
            client.close()
            return True
        except:
            return False

    def on(self, event: str) -> Callable:
        """
        Decorator for registering event handlers
        
        Args:
            event: Name of the event to handle
            
        Returns:
            Callable: Decorator function
        """
        def decorator(func: Callable) -> Callable:
            if event not in self._event_handlers:
                self._event_handlers[event] = []
            self._event_handlers[event].append(func)
            return func
        return decorator

    def _trigger_event(self, event: str, data: Any = None) -> None:
        """
        Trigger an event and call all registered handlers
        
        Args:
            event: Name of the event to trigger
            data: Data to pass to the event handlers
        """
        for handler in self._event_handlers.get(event, []):
            try:
                handler(data)
            except Exception as e:
                print(f"Error in event handler: {e}")


class AgentBuilder:
    """
    Builder pattern for creating agents with specific configurations
    """
    def __init__(self):
        self._name = None
        self._role = None
        self._port = 5050
        self._capabilities = []

    def with_name(self, name: str) -> 'AgentBuilder':
        """Set the agent's name"""
        self._name = name
        return self

    def with_role(self, role: str) -> 'AgentBuilder':
        """Set the agent's role"""
        self._role = role
        return self

    def with_port(self, port: int) -> 'AgentBuilder':
        """Set the agent's port"""
        self._port = port
        return self

    def with_capabilities(self, capabilities: List[str]) -> 'AgentBuilder':
        """Set the agent's capabilities"""
        self._capabilities = capabilities
        return self

    def build(self) -> Peer:
        """Build and return the configured agent"""
        if not self._name or not self._role:
            raise ValueError("Agent requires at least a name and role")
            
        return Peer(
            name=self._name,
            role=self._role,
            port=self._port,
            capabilities=self._capabilities
        )