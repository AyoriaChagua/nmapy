
# Port Scanner Script

This is a Python script designed to perform port scanning on a given host. It identifies whether specified ports are open, closed, or inaccessible and attempts to determine the service running on open ports.

### Features

    •	Resolves hostnames to IP addresses.
    •	Scans a range of ports or specific ports on a given host.
    •	Multithreaded scanning for faster execution.
    •	Identifies services running on open ports (when possible).
    •	Default port list included if no specific ports are provided.

### Requirements

	•	Python 3.6 or later.
	•	Internet connection (to resolve hostnames if needed).

### Installation

	1.	Clone the repository or copy the script file to your local machine.
	2.	Ensure Python 3.6+ is installed.
	3.	Install any required dependencies (none for this script).

### Usage

Run the script from the command line as follows:

```bash
$ python main.py <host> [start_port] [end_port]
```

### Parameters:

	1.	<host>: The target hostname or IP address.
	2.	[start_port]: (Optional) The starting port number for scanning.
	3.	[end_port]: (Optional) The ending port number for scanning.

### Examples:

    1.	Scan a specific host with default ports:

```bash
$ python main.py example.com
```
Scans ports 3001, 80, 8080, 443, and 3004.

    2.	Scan a host with a specific range of ports:

```bash
$ python main.py example.com 20 100
```

	3.	Scan a single port:
```bash
$ python main.py example.com 22
```
Scans port 22.


### Output

The script outputs the status of each port (open, closed, or error) and attempts to identify the service running on open ports.

Example output:

```bash
Scanning host: 192.168.1.1
Port 22: Open (Service: ssh)
Port 80: Open (Service: http)
Port 443: Closed (Service: Unknown)
```

### Notes

	•	The script uses multithreading (ThreadPoolExecutor) to speed up port scanning.
	•	If an invalid hostname is provided, the script will terminate with an error message.
	•	The default timeout for port connections is 3 seconds.
