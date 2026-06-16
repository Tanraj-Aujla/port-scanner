# Port Scanner

A Python port scanner that checks which TCP ports are open on a target host, with two implementations: a simple sequential version and a faster multithreaded version.

## Files

| File | Description |
|------|-------------|
| `port_scanner.py` | Basic sequential scanner |
| `port_scanner_threading.py` | Multithreaded scanner using a worker queue |

## How It Works

Both scripts use Python's `socket` library to attempt a TCP connection on each port. If the connection succeeds, the port is open. They also attempt to identify the service running on each open port via `socket.getservbyport()`.

### `port_scanner.py`
Scans ports 1–1023 one at a time and prints whether each port is open or closed.

### `port_scanner_threading.py`
Fills a `Queue` with ports 1–1023, then spins up 1000 worker threads that each pull from the queue and scan concurrently. Only open ports are printed, and a final summary lists all open ports.

## Usage

1. Set the `target` variable in either script to the IP address or hostname you want to scan:
   ```python
   target = "127.0.0.1"  # default: localhost
   ```

2. Run the desired script:
   ```bash
   python port_scanner.py
   # or
   python port_scanner_threading.py
   ```

## Requirements

- Python 3.x (no third-party dependencies)

## Notes

- Scanning ports on systems you do not own or have explicit permission to test may be illegal. Only use this tool on your own machines or in authorized environments.
- The threaded version is significantly faster but may trigger rate-limiting or firewall alerts on remote hosts.
- The 1-second socket timeout in the threaded version can be adjusted to tune speed vs. accuracy.
