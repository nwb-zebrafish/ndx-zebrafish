# -*- coding: utf-8 -*-
import os.path

from pynwb.spec import NWBNamespaceBuilder, export_spec, NWBGroupSpec, NWBAttributeSpec

# TODO: import other spec classes as needed
# from pynwb.spec import NWBDatasetSpec, NWBLinkSpec, NWBDtypeSpec, NWBRefSpec


def main():
    # these arguments were auto-generated from your cookiecutter inputs
    ns_builder = NWBNamespaceBuilder(
        doc="""NWB extensions for storing (larval) zebrafish expreiment related data""",
        name="""ndx-zebrafish""",
        version="""0.1.0""",
        author=list(
            map(
                str.strip,
                """Ruben Portugues, Martin Haesemeyer, Luigi Petrucco, Vilim Stih""".split(
                    ","
                ),
            )
        ),
        contact=list(map(str.strip, """ruben.portugues@tum.de""".split(","))),
    )

    ns_builder.include_type("ZebrafishBehaviorSeries", namespace="core")

    # TODO: define your new data types
    # see https://pynwb.readthedocs.io/en/latest/extensions.html#extending-nwb
    # for more information
    FishGroup = NWBGroupSpec(
        neurodata_type_def="ZebrafishBehaviorSeries",
        neurodata_type_inc="NWBContainer",
        doc="An extension of the NWB group to include all behavioral data from a zebrafish traking experiemnt",
        attributes=[
            NWBAttributeSpec(name="fish_id", doc="The fish ID.", dtype="int32")
        ],
    )
    FishGroup.add_dataset(
        default_name="orientation",
        neurodata_type_def="Orientation",
        neurodata_type_inc="SpatialSeries",
        quantity="?",
        doc="The direction the fish head points in a left coordinate system"
        " (angle increases clockwise, zero points right",
    )
    FishGroup.add_dataset(
        default_name="tail_shape",
        neurodata_type_def="TailShape",
        neurodata_type_inc="SpatialSeries",
        quantity="?",
        doc="The shape of the tail recorded as relative angles to first tail segment",
    )
    FishGroup.add_dataset(
        default_name="position",
        neurodata_type_def="Coordinates",
        neurodata_type_inc="SpatialSeries",
        quantity="?",
        doc="The x,y position of the swim bladder in camera coordinates",
    )

    new_data_types = [FishGroup]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "spec")
    )
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == "__main__":
    # usage: python create_extension_spec.py
    main()
