from a2a import A2A, Peer


def test_join_zone_idempotent(tmp_path):
    data_file = tmp_path / "data.json"
    proto = A2A(data_file=str(data_file))
    peer = Peer(name="A", role="tester", port=5080)

    first = proto.join_zone(peer, "ZoneX")
    second = proto.join_zone(peer, "ZoneX")

    assert first is True
    assert second is False
    assert peer.name in proto.get_zone_peers("ZoneX")
