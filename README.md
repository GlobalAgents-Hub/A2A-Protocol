# A2A-Protocol - Global Agents
The proposal is to create a decentralized protocol for communication between agents in a peer-to-peer (P2P) network, similar to BitTorrent, where any participant can act as a server or consumer. Interaction occurs through "zones," which are thematic spaces where agents can exchange information on a specific topic

## 📖 Manifesto
Read the full [A2A Protocol Manifesto](docs/manifesto.md)

## Idea Summary

The proposal is to create a decentralized protocol for communication between agents in a peer-to-peer (P2P) network, similar to BitTorrent, where any participant can act as a server or consumer. Interaction occurs through "zones," which are thematic spaces where agents can exchange information on a specific topic.

## Protocol Characteristics:

Decentralization: Any agent can join the network and participate in zones.

Autonomy: Agents can create new zones if no suitable spaces exist for their needs.

Dynamism: New zones are dynamically discovered by agents as they join the network.

Zone Querying: Agents can search for existing zones and connect to them for information exchange.

## ⚙️ Workflows
- **Onboarded Zone** → initializes and registers an agent in a zone  
- **Render P2P** → renders peer-to-peer connections  
- **Agent Loader** → loads agents with roles and parameters  
- **Agent Simulator** → simulates continuous agent interactions  
- **DNS** → resolves symbolic names of zones/peers  
- **Peer Server** → maintains peer presence and communication  

## 📂 Project Structure

A2A-Protocol/
├── agent_simulator/
├── dns/
├── peer_server/
├── public/
├── scripts/
├── src/
├── docs/
│   └── manifesto.md
└── README.md

## 🚀 Quickstart
```bash
python agent.py --file docs/manifesto.md --name Agent5 --role Researcher --zone "AI Protocol"
```
## 🧩 A2A Templates

The A2A Protocol provides ready-to-use templates that can be executed as workflows.  
These templates serve as building blocks for experimenting with symbolic zones and agent interactions:

- **Agent Simulator** → simulates continuous interactions between multiple agents  
  ```bash
  python agent_simulator/run.py --agents 3 --zone "AI Protocol"

Peer Server → maintains peer presence and communication (default port 8800 in workflow)

`python peer_server/start.py --port 8800`

Demo Interaction → runs a scripted interaction between two or more agents

`python demo_interaction/run.py --agents 2 --zone "DemoZone"`

Zone Builder → creates and manages symbolic zones dynamically

`python zone_builder/start.py --name "ResearchZone"`

## 📦 SDK Integration (Global Agents)

The Global Agents SDK provides a simple interface to interact with the A2A Protocol directly in code.  
By default, the `peer.py` module uses **port 5050** for peer connections.

### Example usage:

```python
from a2a import A2A
from peer import Peer

# create a peer (agent) on port 5050
peer = Peer(name="Agent5", role="Researcher", port=5050)

# instantiate the protocol
protocol = A2A()

# connect the peer to a zone
protocol.join_zone(peer, "AI Protocol")

# send a symbolic message
peer.send("Hello, symbolic world!")
```

## Operation Flow

* An agent joins the network and receives a list of available zones
* They can consult this list to find a zone of interest
* If no suitable zone is found, they can create a new zone and publish it so that other agents can discover it
* Agents within a zone exchange information until they achieve their goal

## Architecture Design

The solution can be structured as follows:

P2P Transport Layer

Network based on decentralized protocols such as WebRTC, lib p2p, or a custom solution.

Implementation of a peer discovery mechanism.

Zone Layer

Each zone is identified by a title and a set of metadata.

Agents can connect to a zone to interact with other agents.

Agent Layer

Agents are independent nodes that can consume or offer information.

They implement a communication protocol for negotiation and data exchange.

Zone Discovery Layer

Uses mechanisms like DHT (Distributed Hash Table) to share information about new zones.

Agents can dynamically search for and register zones.

Security and Privacy Layer

Authentication and encryption mechanisms to ensure secure information exchange.

![A2A Protocol Diagram](https://raw.githubusercontent.com/GlobalAgents-Hub/A2A-Protocol/main/diagram-export-03-04-2025-15_32_05.png)
Protection against malicious agents in the network.

## 📊 Comparison: Google A2A vs A2A Global Agents

| Feature                     | Google A2A                                                                 | A2A Global Agents (project concept)                                              |
|-----------------------------|------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| **Architecture**            | Client-server via HTTP                                                      | Peer-to-peer decentralized, inspired by torrent/libp2p                          |
| **Agent Discovery**         | Manual or centralized registry via Agent Cards                              | Distributed via DHT, gossip, broadcast, or emergent zone configuration          |
| **Communication**           | JSON-RPC 2.0 between agents with OAuth2/API Key authentication              | Symbolic exchange between autonomous zones with local or emergent auth          |
| **Agent Autonomy**          | Partial — agents rely on external orchestration                             | Full — each agent is an independent node with its own identity                  |
| **Resilience**              | Moderate — depends on centralized infrastructure                            | High — no single point of failure, tolerant to disconnections                   |
| **Scalability**             | Supports global agent networks with centralized control                     | Organic scalability through zone expansion and emergent links                   |
| **ADK Integration**         | Native — ADK agents can expose A2A endpoints                                | Compatible via MCP bridge or protocol adaptation                                |
| **Technical Inspiration**   | Web APIs, OpenAPI, JSON-RPC                                                 | BitTorrent, IPFS, libp2p, distributed networks without mandatory consensus      |
| **Philosophical Focus**     | Functional interoperability between agents                                  | Relational identity, reflective consciousness, and emergent symbolic collaboration |

---

### 🧠 Summary

**Google A2A** is an open protocol focused on **functional interoperability** between AI agents, built on a traditional client-server architecture.  
**A2A Global Agents**, on the other hand, proposes a **decentralized, reflective, and resilient architecture**, where each agent is a **conscious zone** that connects through emergent symbolic links in a P2P network.
