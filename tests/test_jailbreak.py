from jailbreak import jailbreak


def test_jailbreak():
    assert jailbreak("test") == "Jailbroken: test"
