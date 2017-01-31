def get_major_version(filename):
    return int(filename[14])


def get_elasticsearch_base_url(version):
    if version < 5:
        return 'https://download.elasticsearch.org/elasticsearch/elasticsearch'
    return 'https://artifacts.elastic.co/downloads/elasticsearch'


class FilterModule(object):
    def filters(self):
        return {
            'get_major_version': get_major_version,
            'get_elasticsearch_base_url': get_elasticsearch_base_url,
        }
