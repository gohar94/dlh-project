Accelergy-Timeloop for Albireo
------------------------------

This directory contains an implementation of [Albireo](https://ieeexplore.ieee.org/document/9499746) for Accelergy and Timeloop.

### Energy Estimates

The energy estimates for most of the components are based on the Albireo paper or its cited references.

Run the following script to get an energy breakdown derived from the results in the paper:
```
python3 energy_calculation.py
```

### Accelergy modification

We require the following primitive components file to be packaged with Accelergy: `albireo_primitive_component.lib.yaml`

For example, if running with the provided Docker container, please copy it inside the Accelergy installation as follows:

Note: This needs to be run *inside* the container:
```
cp albireo_primitive_component.lib.yaml /usr/local/share/accelergy/primitive_component_libs/
```
