from jnpr.jsnapy import SnapAdmin
from pprint import pprint
from jnpr.junos import Device


def snapshot():
    js = SnapAdmin()
    config_file = "C:/Users/MARIOPEREZBENAVIDES/jsnapy/testcase_python/venv/config.yml"
    snapvalue = js.snap(config_file, "snap")