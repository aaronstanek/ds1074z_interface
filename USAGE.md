# USAGE

The program has two interfaces.

The Python interface in through the class: ds1074z_controlPanel.
Found in the file ds1074z_controlPanel.py

For a guide on how to use this, see program.py

The config file interface is found in osc_control.txt
- co-channels indicates which channels to use
- co-count is how many events to collect
- co-delay is how many seconds should be between events
  - keep this in the range 0.3 to 2.0
  - if the oscilloscope is running but not collecting any data, increase this value
- co-format is the format in which to save the data
  - many formats are supported, only json_clump has been thoroughly tested
- co-path is where to save the data
  - should be an existing folder
  - should end with a slash character

To use this interface, put osc_control.txt in the same folder as script_control_master.py;
then call script_control_master.py from the command line
