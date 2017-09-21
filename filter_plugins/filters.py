def get_major_version(filename):
    return int(filename[14])


def get_elasticsearch_base_url(version):
    if version < 5:
        return 'https://download.elasticsearch.org/elasticsearch/elasticsearch'
    return 'https://artifacts.elastic.co/downloads/elasticsearch'


def get_elasticsearch_generic_command(version, command):
    if version == 1:
        return '/usr/share/elasticsearch/bin/plugin --{}'.format(command)
    elif version == 2:
        return '/usr/share/elasticsearch/bin/plugin {}'.format(command)
    else:
        return '/usr/share/elasticsearch/bin/elasticsearch-plugin {}'.format(command)


def get_elasticsearch_plugin_list_command(version):
    return get_elasticsearch_generic_command(version, 'list')


def get_elasticsearch_plugin_remove_command(version):
    return get_elasticsearch_generic_command(version, 'remove')


def get_elasticsearch_plugin_install_command(version):
    return get_elasticsearch_generic_command(version, 'install')


class FilterModule(object):
    def filters(self):
        return {
            'get_major_version': get_major_version,
            'get_elasticsearch_base_url': get_elasticsearch_base_url,
            'plugin_install_command': get_elasticsearch_plugin_install_command,
            'plugin_list_command': get_elasticsearch_plugin_list_command,
            'plugin_remove_command': get_elasticsearch_plugin_remove_command,
        }
