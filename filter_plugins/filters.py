def get_major_version(filename):
    return int(filename[14])


class FilterModule(object):
    def filters(self):
        return {
            'get_major_version': get_major_version,
        }
