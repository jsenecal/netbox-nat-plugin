from extras.plugins import PluginConfig

class NATConfig(PluginConfig):
    name = 'netbox_nat_plugin'
    verbose_name = 'NetBox NAT Plugin'
    description = 'A NetBox plugin to document NAT related things.'
    version = '0.0.0'
    author='Jonathan Senecal',
    author_email='contact@jonathansenecal.com',
    base_url = 'nat'
    required_settings = []
    default_settings = {}
    min_version = "3.0"

config = NATConfig