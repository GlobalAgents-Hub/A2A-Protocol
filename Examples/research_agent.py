"""
Example of creating and using agents with the A2A Protocol
"""
from a2a import A2A, AgentBuilder, NetworkDiscovery
import time

def main():
    # Initialize the protocol
    protocol = A2A()
    discovery = NetworkDiscovery()
    discovery.start()

    # Create a researcher agent
    researcher = (
        AgentBuilder()
        .with_name("ResearchAgent")
        .with_role("Researcher")
        .with_capabilities(["text_analysis", "data_collection"])
        .build()
    )

    # Start the agent's server
    researcher.start()

    # Handle incoming messages
    @researcher.on("message_received")
    def handle_message(message):
        print(f"Received message: {message}")
        # Process the message and potentially respond
        if "query" in message:
            researcher.send({
                "type": "response",
                "data": f"Analysis result for: {message['query']}"
            })

    # Join the AI Research zone
    protocol.join_zone(researcher, "AI Research")
    print(f"Joined zone: AI Research")

    try:
        while True:
            # Periodically check for new peers and zones
            peers = discovery.find_peers(role="Researcher")
            zones = discovery.find_zones(topic="AI")
            
            print(f"\nActive researchers: {peers}")
            print(f"Available AI zones: {zones}")
            
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nShutting down...")
        researcher.stop()
        discovery.stop()

if __name__ == "__main__":
    main()