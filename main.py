import socket
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from urllib.parse import urlparse
import sys


def validate_extract_host(host_input):
    if host_input.startswith(('http://', 'https://')):
        parsed_url = urlparse(host_input)
        host_input = parsed_url.hostname or parsed_url.path

    try:
        return socket.gethostbyname(host_input)
    except socket.gaierror:
        print(f"Error: Unable to resolve host {host_input}")
        sys.exit(1)


def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        result = sock.connect_ex((host, port))
        try:
            service = socket.getservbyport(port)
        except:
            service = 'Unknown'

        sock.close()
        print(f"Scanning - Port {port}: Result code {result}")
        if result == 0:
            return (port, 'Open', service)
        else:
            return (port, 'Closed', service)

    except Exception as e:
        print(f"Error on port {port}: {e}")
        return (port, 'Error', 'N/A')
    
def scan_host(host, ports=None):
    print(f"Scanning host: {host}")

    if ports is None:
        ports = range(1, 1001)
    
    results = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        scan_futures = {executor.submit(scan_port, host, port): port for port in ports}

        for future in as_completed(scan_futures):
            port, state, service = future.result()
            if state == 'Open':
                print(f"Port {port}: {state} (Service: {service})")
                results.append((port, state, service))
    return results


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <host> [ports]")
        sys.exit(1)

    host = validate_extract_host(sys.argv[1])

    if len(sys.argv) == 4:
        start_port = int(sys.argv[2])
        end_port = int(sys.argv[3])
        ports = range(start_port, end_port + 1)
    elif len(sys.argv) == 3:
        start_port = int(sys.argv[2])
        ports = range(start_port, start_port + 1)
    else:
        ports = [80, 3030, 3000, 4780, 5000, 8080, 9000]

    scan_host(host, ports)

if __name__ == "__main__":
    main()