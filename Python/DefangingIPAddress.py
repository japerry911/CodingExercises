"""
---Defanging an IP Address---
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
"""

# always given valid IPv4 address


def defang_ip_addr(address: str) -> str:
    return address.replace(".", "[.]")
