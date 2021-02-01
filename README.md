# TP-LinkR470T_Script
Python Script to get information of Firewall TP-Link R470T+



```bash
2021-01-31 18:29:39,616 - firewallUtil - INFO - Response  Status2 body: {
  "id": 1,
  "result": {
    "normal": [
      {
        "t_proto": "static",
        "macaddr": "FF-FF-FF-FF-FF-FF",
        "ipaddr": "192.168.199.1",
        "t_isup": true,
        "t_type": "physical",
        "t_name": "LAN",
        "netmask": "255.255.255.0",
        "t_linktype": "static"
      },
      {
        "t_proto": "dhcp",
        "ipaddr": "192.168.1.252",
        "netmask": "255.255.255.0",
        "t_linktype": "dhcp",
        "macaddr": "FF-FF-FF-FF-FF-FF",
        "dns1": "8.8.8.8",
        "gateway": "192.168.1.1",
        "t_isup": true,
        "t_type": "physical",
        "t_name": "WAN1"
      },
      {
        "t_proto": "dhcp",
        "ipaddr": "192.168.2.142",
        "netmask": "255.255.255.0",
        "t_linktype": "dhcp",
        "macaddr": "FF-FF-FF-FF-FF-FF",
        "dns1": "192.168.2.1",
        "gateway": "192.168.2.1",
        "t_isup": true,
        "t_type": "physical",
        "t_name": "WAN2"
      },
      {
        "t_proto": "dhcp",
        "macaddr": "FF-FF-FF-FF-FF-FF",
        "t_type": "physical",
        "t_isup": false,
        "t_name": "WAN3",
        "t_linktype": "dhcp"
      }
    ],
    "vpn": {}
  },
  "error_code": "0"
}

```

## TODO:
- [x] Connect with TP-R470T+
    - [x] Get status of WAN interfaces
    - [x] Enable/Disable specific WAN interface