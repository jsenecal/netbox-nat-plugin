# netbox-nat-plugin

A [NetBox](https://github.com/netbox-community/netbox) plugin to document NAT related things. Netbox >= v3.0 is required.

# Installation

General installation steps and considerations follow the [official guidelines](https://netbox.readthedocs.io/en/stable/plugins/).

### Package Installation from PyPi

Assuming you use a Virtual Environment for NetBox in `/opt/netbox/venv`:
```
$ source /opt/netbox/venv/bin/activate
(venv) $ pip3 install netbox-nat-plugin
```

### Package Installation from Source Code
The source code is available on [GitHub](https://github.com/jsenecal/netbox-nat-plugin).  
Download and install the package. Assuming you use a Virtual Environment for NetBox in `/opt/netbox/venv`:
```
$ git clone https://github.com/jsenecal/netbox-nat-plugin
$ cd netbox-nat-plugin
$ source /opt/netbox/venv/bin/activate
(venv) $ pip3 install .
```

To ensure NextBox UI plugin is automatically re-installed during future upgrades, create a file named `local_requirements.txt` (if not already existing) in the NetBox root directory (alongside `requirements.txt`) and list the `netbox-nat-plugin` package:

```no-highlight
# echo netbox-nat-plugin >> local_requirements.txt
```

### Enable the Plugin
In a global Netbox **configuration.py** configuration file, update or add PLUGINS parameter:
```python
PLUGINS = [
    'netbox_nat_plugin',
]
```

Optionally, update a PLUGINS_CONFIG parameter in **configuration.py** to rewrite default plugin behavior