#!/usr/bin/env python3
"""
Sends the three sample NAC accounting events to the local listener for testing.
Run the listener first, then: python test_webhook.py
"""

import json
import urllib.request

URL = "http://localhost:8001/"

PAYLOADS = [
    {
        "topic": "nac-accounting",
        "events": [{
            "ap": "709041040e34", "bssid": "709041388c43",
            "client_type": "wireless", "mac": "5e6601115b49",
            "multi_session_id": "0x41363031454238383837304231423839",
            "nas_ip": "172.16.0.10", "nas_vendor": "juniper-mist",
            "org_id": "0e134843-ba6c-403a-badb-fe97452f0ca4",
            "session_id": "46A689BBEA655716",
            "session_unique_id": "43e76c65ab0e828f5e2ad14c4fe4d01d",
            "site_id": "2bf5a231-6d95-4c62-aa16-2c6bc6b5f83a",
            "ssid": "PK_NAC", "timestamp": 1782127701568,
            "type": "NAC_ACCOUNTING_START",
            "username": "user1@keeley.org.uk",
            "device_cert_expiry": "0001-01-01T00:00:00Z",
        }],
    },
    {
        "topic": "nac-accounting",
        "events": [{
            "ap": "709041040e34", "bssid": "709041388c43",
            "client_ip": "172.16.10.71", "client_type": "wireless",
            "mac": "5e6601115b49",
            "multi_session_id": "0x41363031454238383837304231423839",
            "nas_ip": "172.16.0.10", "nas_vendor": "juniper-mist",
            "org_id": "0e134843-ba6c-403a-badb-fe97452f0ca4",
            "session_id": "46A689BBEA655716",
            "session_unique_id": "43e76c65ab0e828f5e2ad14c4fe4d01d",
            "site_id": "2bf5a231-6d95-4c62-aa16-2c6bc6b5f83a",
            "ssid": "PK_NAC", "timestamp": 1782127701595,
            "type": "NAC_ACCOUNTING_UPDATE",
            "username": "user1@keeley.org.uk",
            "device_cert_expiry": "0001-01-01T00:00:00Z",
        }],
    },
    {
        "topic": "nac-accounting",
        "events": [{
            "ap": "709041040e34", "bssid": "709041388c43",
            "client_ip": "172.16.10.71", "client_type": "wireless",
            "mac": "5e6601115b49",
            "multi_session_id": "0x41363031454238383837304231423839",
            "nas_ip": "172.16.0.10", "nas_vendor": "juniper-mist",
            "org_id": "0e134843-ba6c-403a-badb-fe97452f0ca4",
            "rx_bytes": 158242, "rx_pkts": 588,
            "session_duration_in_mins": 0,
            "session_id": "46A689BBEA655716",
            "session_unique_id": "43e76c65ab0e828f5e2ad14c4fe4d01d",
            "site_id": "2bf5a231-6d95-4c62-aa16-2c6bc6b5f83a",
            "ssid": "PK_NAC", "terminate_cause": "User-Request",
            "timestamp": 1782127749529,
            "tx_bytes": 130997, "tx_pkts": 208,
            "type": "NAC_ACCOUNTING_STOP",
            "username": "user1@keeley.org.uk",
            "device_cert_expiry": "0001-01-01T00:00:00Z",
        }],
    },
]

for payload in PAYLOADS:
    data = json.dumps(payload).encode()
    req = urllib.request.Request(URL, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as resp:
        print(f"Sent {payload['events'][0]['type']} → {resp.status} {resp.read().decode()}")
