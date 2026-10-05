#!/usr/bin/env python3
"""
DNS resolver: takes a string with hostnames separated by commas and/or spaces,
resolves each one to an IP address (or multiple).
"""

import socket
import re
import sys


def parse_input(raw: str) -> list[str]:
    """Split the input string by commas and whitespace, drop empties."""
    # Split by comma or whitespace (one or more)
    parts = re.split(r"[,\s]+", raw.strip())
    return [p for p in parts if p]


def resolve(host: str) -> list[str]:
    """Resolve a hostname to a list of IP addresses (IPv4 + IPv6)."""
    try:
        # getaddrinfo returns tuples: (family, type, proto, canonname, sockaddr)
        infos = socket.getaddrinfo(host, None)
    except socket.gaierror as e:
        return [f"ERROR: {e}"]

    ips = []
    for info in infos:
        ip = info[4][0]
        if ip not in ips:  # dedupe
            ips.append(ip)
    return ips


def main():
    # Get the input: from CLI argument, or prompt if nothing was given
    if len(sys.argv) > 1:
        raw = " ".join(sys.argv[1:])
    else:
        raw = input("Enter hosts (separated by comma/space): ")

    hosts = parse_input(raw)

    if not hosts:
        print("No hosts to resolve.")
        return

    print(f"Resolving {len(hosts)} host(s)...\n")

    for host in hosts:
        ips = resolve(host)
        if len(ips) == 1 and ips[0].startswith("ERROR"):
            print(f"{host:<30} -> {ips[0]}")
        else:
            print(f"{host:<30} -> {', '.join(ips)}")


if __name__ == "__main__":
    main()