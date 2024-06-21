# Prototyping Platform

Analog Devices, Inc. (ADI) provides software for many of the 100,000+ products across different application spaces. However, due to the nature of embedded development such solutions are often fragmented and not easily discoverable. The Prototyping Platform aims to provide a unified experience for users to quickly get started with ADI products and provide components that can be reused within an end product.

## Strategy

The Prototyping Platform is a collection of software components, HDL, tools, and documentation that can be used along side ADI products and solutions. These offering are built upon industry standards and best practices when possible to ensure that they are easily integrated into a larger system. This can create a bit of a learning curve for new users, but the goal is to provide a consistent experience across ADI products that require software support. Common software collateral would include: in-kernel drivers, HDL reference designs, MATLAB Toolbox, Python libraries, and more. All of which try to follow coding styles and architectures for a given language or platform. This generally reduces integration of ADI products if you are a experienced user of that ecosystem.

## Platform Collateral Structure

```{d2}
:width: 90%

direction: right
style: {
    fill: transparent
}

Hardware -> Linux Drivers
Hardware -> Bare-Metal Drivers
Hardware -> HDL
HDL -> Bare-Metal Drivers
HDL -> Linux Drivers

Linux Drivers -> Interface Tools
Bare-Metal Drivers -> Interface Tools

HDL -> Application Tools
Linux Drivers -> Application Tools
Bare-Metal Drivers -> Application Tools
Interface Tools -> Application Tools

```

The Prototyping Platform is broken down into a few key areas of interconnected solutions. Not all software offerings apply to all products, but the goal is to provide consistency across them when possible. The following are the key areas of the Prototyping Platform:
- [Hardware](hardware/README.md): Hardware reference designs and evaluation platforms.
- [Linux-Drivers](linux-drivers/README.md): In-kernel drivers for ADI products.
- [Bare-Metal-Drivers](bare-metal-drivers/README.md): Bare-metal drivers for ADI products.
- [Interface-Tools](interface-tools/README.md): Tools for interfacing with ADI products.
- [Application-Integrations](application-integrations/README.md): Software components for integrating ADI products into a larger system.
- [Configuration-Tools](configuration-tools/README.md): Tools for configuring ADI products which may or may not require hardware.

## Mapping Software Collateral To Different Platforms

Digging through the different component avoid in isolation can be a daunting task, and my provide limited contacts to how an overall system would function from end-to-end. To aid in this understanding, a number of system architecture articles have been created for different types of systems. These articles provide a high-level overview of how different software components can be used together to create a complete system. The following are the different system architecture articles that have been created:

```{toctree}
:hidden: true

fpga_system.md
micro_system.md

```
- [FPGA System Architecture](fpga_system.md): A high-level overview of how to use HDL, Linux drivers, bare-metal drivers, and application integrations to create a complete system.
- [Microcontroller System Architecture](micro_system.md): A high-level overview of how to use Linux, bare-metal drivers, interface tools, and application integrations to create a complete system.

Embedded systems are endlessly flexible and can be used in a wide variety of applications. Therefore, these examples should not be considered the extent of what can be done with ADI products or software. ADI software collateral is designed to be modular and flexible to allow for a wide variety of use cases. If you have a specific question or need help with a specific use case, please reach out to the [EngineerZone](https://ez.analog.com/) community for help.