from pynwb.testing import TestCase, AcquisitionH5IOMixin

from ndx_zebrafish import ZebrafishBehavior


class TestZebrafishBehaviorRoundtripPyNWB(AcquisitionH5IOMixin, TestCase):
    def setUpContainer(self):
        """Return the test ZebrafishBehavior to read/write"""
        zbh = ZebrafishBehavior(fish_id=1, name="fish_behavior")
        return zbh
