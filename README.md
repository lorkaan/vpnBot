VPN BOT
=======

This is a demonstration on how to create an automated bot using the [pexpectparser](https://github.com/lorkaan/pexpectparser) library:

Using a Directed Graph, paths between symbols are represented.
A Grammar object is used to provide start and end symbols, providing some representation of context and direction for movement though the Graph.

A pexpect parser uses this Grammar and Directed Graph, to create a command line bot.

This Demo uses a VPN with command line login access as a proof of concept.

# Requirements

This code has the following requirements:
- Linux Operating System
- [PipEnv](https://pypi.org/project/pipenv/) 
- [Git](https://git-scm.com/)
- [OpenVPN](https://openvpn.net/)
- A subscription to a VPN service using [OpenVPN](https://openvpn.net/)
- A set of VPN server configurations represented by `.ovpn` files
	- Henceforth, referred to as `<ovpnSet>`

# Installation

```
$  git clone https://github.com/lorkaan/vpnBot.git <location>
```

where `<location>` is an optional path to the folder to download the source code to.

*Note*
- If you leave `<location>` blank, the source code with be in a new subdirectory called `vpnBot/` 

Navigate to `<location>` and run the following commands:
```
$  pipenv shell
$  pipenv install
```

# Usage

## Prerequistes

Due to the variety of OpenVPN clients and the security of sudo and login creditenials, there are some prerequistes needed before this demo can be run.

- The credentials file
	- This file is passed to the program as a command line argument: `runVPN.py <cred_file_path>`
	- Every line is of the format `<user>:<password>`
	- This file must have 2 lines in it
		- Line 1: Sudo Authentication
		- Line 2: VPN Client Authentication
- The `<location>/config/` folder used to hold the `<ovpnSet>`
	- If the `<location>` option in your installation step was blank, `<location> = vpnBot/` 
	- This folder must have at least one `.ovpn` file in it

## Running

*Note*
- This program can not be run with `sudo` within the PipEnv environment. This actually breaks the command out of the virtual environment and won't be able to find the dependencies as a result.

With all the prerequistes satisfied, the program can be run with the following command:
```
$  python runVPN.py <cred_file_path>
```

If the demo succeeds, the console will print out the following message:
```
  VPN Connected
  
```

Disconnecting the VPN can be done by pressing Ctrl+C. 
Due to the nature of a VPN, this program actually performs blocking on the terminal, until the user interrupts the program.

## Errors

Sometimes a user may encounter an error in running the program. 
Most of the time, these errors come from authentication problems, where the sudo auth is not correct or the ovpen username and password are incorrect. 

# Disclaimer

This is just a demo to show how the [pexpectparser](https://github.com/lorkaan/pexpectparser) library can be utilized to automate command line tasks. 
Future upgrades to remove some of the prerequistes can be expected.
