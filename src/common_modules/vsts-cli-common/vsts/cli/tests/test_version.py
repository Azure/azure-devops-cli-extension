import unittest
from ..common.version import _is_version_less_than


class TestVersionMethods(unittest.TestCase):

    def test__is_version_less_than(self):
        _test_version_compare('1.1.1', '1.1.1', False)
        _test_version_compare('2.1.1', '1.9.9', False)
        _test_version_compare('1.9.9', '2.0.0', True)
        _test_version_compare('1.2.1', '1.1.9', False)
        _test_version_compare('1.1.9', '1.2.0', True)
        _test_version_compare('1.1.2', '1.1.1', False)
        _test_version_compare('1.1.1', '1.1.2', True)
        _test_version_compare('1.1.1', '1.1.1a', False)
        _test_version_compare('1.1.1a', '1.1.1', True)
        _test_version_compare('1.1.1b', '1.1.1a', False)
        _test_version_compare('1.1.1a', '1.1.1b', True)
        _test_version_compare('1.1.1rc', '1.1.1b', False)
        _test_version_compare('1.1.1b', '1.1.1rc', True)
        _test_version_compare('1.1.1rc', '1.1.1rc', False)
        _test_version_compare('1.1.1rc0', '1.1.1b9', False)
        _test_version_compare('1.1.1b9', '1.1.1rc0', True)
        _test_version_compare('1.1.1rc0', '1.1.1b9', False)
        _test_version_compare('1.1.1b10', '1.1.1b2', False)
        _test_version_compare('1.1.1b2', '1.1.1b10', True)
        _test_version_compare('1.1.1b0', '1.1.1b0.dev', False)
        _test_version_compare('1.1.1b0.dev', '1.1.1b0', True)
        _test_version_compare('1.1.1b0.dev', '1.1.1b0.dev', False)
        _test_version_compare('1.1.1b0.post', '1.1.1b0.dev', False)
        _test_version_compare('1.1.1b0.dev', '1.1.1b0.post', True)
        _test_version_compare('1.1.1b0.post1', '1.1.1b0.dev9', False)
        _test_version_compare('1.1.1b0.dev9', '1.1.1b0.post1', True)
        _test_version_compare('1.1.1b0.dev123', '1.1.1b0.dev2', False)
        _test_version_compare('1.1.1b0.dev2', '1.1.1b0.dev123', True)
        _test_version_compare('1.1.1b0.dev123', '1.1.1b0.dev123', False)
        _test_version_compare('0.1.0b0', '0.1.0b0.dev4382347', False)


def _test_version_compare(current, latest, expected):
    if expected and not _is_version_less_than(current, latest):
        raise Exception("expected current < latest, {current} < {latest}".format(current=current, latest=latest))
    if not expected and _is_version_less_than(current, latest):
        raise Exception("expected current >= latest, {current} >= {latest}".format(current=current, latest=latest))


if __name__ == '__main__':
    unittest.main()
