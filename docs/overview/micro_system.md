# Microprocessor Based System Architecture

The Microprocessor System Architecture is a high-level overview of how to use Linux, bare-metal drivers, interface tools, and application integrations to create a complete system. This article is intended to provide a high-level overview of how the different software components can be used together to create a complete system. Microprocessors are typically used with ADI precision converters, sensors, and other low-speed peripherals. ADI provides a number of reference projects for microprocessor vendors like Maxim, Broadcom, and ADI.

## Linux Drivers

Linux drivers are usually implemented first for microprocessor based systems. Linux has a much richer development environment and is easier to debug than bare-metal systems in many cases. These drivers are implemented with a specific kernel subsystem depending on their application or purpose. Here is the typical breakdown of systems used:
- [IIO](https://wiki.analog.com/software/linux/docs/iio/iio): For data converters, sensors, and frequency generation devices
- [PMBUS](https://wiki.analog.com/software/linux/docs/pmbus): For power management devices
- [HWMON](https://wiki.analog.com/software/linux/docs/hwmon): For temperature and voltage monitoring devices
- [MISC](https://wiki.analog.com/software/linux/docs/misc): For devices that do not fit into the above categories
