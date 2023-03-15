# Flood Warning System

This code sample forms the computational backend (library) to a new real-time flood warning system for England. The library fetches real-time river level data over the Internet from the Department for Environment Food and Rural Affairs data service, and supports specified data query types on river level monitoring stations (all the different TaskXX.py notebooks can be run to obtain the data). Last but not least, it analyses monitoring station data in order to assess flood risks, and issue flood warnings for areas of the country (Task2F.py, Task 2G.py).

Automated testing and continuous integration is also implemented using pytest (all of the test_xxx.py files), to ensure that our code is implemented correctly.

