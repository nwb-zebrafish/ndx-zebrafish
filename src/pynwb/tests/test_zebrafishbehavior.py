import numpy as np


from pynwb import NWBFile, NWBHDF5IO, NWBContainer

print("imported")


from pynwb.core import DynamicTableRegion
from pynwb.device import Device
from pynwb.ecephys import ElectrodeGroup
from pynwb.testing import TestCase, AcquisitionH5IOMixin

from ndx_zebrafish import ZebrafishBehavior


class TestZebrafishBehaviorRoundtripPyNWB(AcquisitionH5IOMixin, TestCase):
    """Complex, more complete roundtrip test for TetrodeSeries using pynwb.testing infrastructure."""

    def setUpContainer(self):
        """ Return the test TetrodeSeries to read/write """
        self.device = Device(
            name='device_name'
        )

        self.group = ElectrodeGroup(
            name='electrode_group',
            description='description',
            location='location',
            device=self.device
        )

        self.table = get_electrode_table()  # manually create a table of electrodes
        for i in np.arange(10.):
            self.table.add_row(
                x=i,
                y=i,
                z=i,
                imp=np.nan,
                location='location',
                filtering='filtering',
                group=self.group,
                group_name='electrode_group'
            )

        all_electrodes = DynamicTableRegion(
            data=list(range(0, 10)),
            description='all the electrodes',
            name='electrodes',
            table=self.table
        )

        data = np.random.rand(100, 3)
        tetrode_series = TetrodeSeries(
            name='name',
            description='description',
            data=data,
            rate=1000.,
            electrodes=all_electrodes,
            trode_id=1
        )
        return tetrode_series

    def addContainer(self, nwbfile):
        """Add the test TetrodeSeries and related objects to the given NWBFile."""
        nwbfile.add_device(self.device)
        nwbfile.add_electrode_group(self.group)
        nwbfile.set_electrode_table(self.table)
        nwbfile.add_acquisition(self.container)
