import time
from a2a import Peer


def test_peer_loopback_message():
    peer = Peer(name="TestPeer", role="tester", port=5070)
    received = []

    @peer.on("message_received")
    def _on_message(msg):
        received.append(msg)

    peer.start()
    try:
        ok = peer.send({"type": "ping", "n": 1}, target_port=peer.port)
        assert ok is True
        # allow some time for background thread to process
        for _ in range(10):
            if received:
                break
            time.sleep(0.05)
        assert received and received[0]["type"] == "ping"
    finally:
        peer.stop()
