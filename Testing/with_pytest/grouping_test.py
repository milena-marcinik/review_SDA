class TestClass:
    def test_unicorn(self):
        x = "unicorn"
        assert "r" in x

    def test_pony(self):
        x = "pony"
        assert hasattr(x, "check")