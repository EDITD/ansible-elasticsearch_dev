# ansible-elasticsearch_dev

By default, this will install elasticsearch and its head plugin. There are a number
of options to configure the ES installation.

It only installs elasticsearch on a single host and it doesn't try to form a cluster.

```
roles:
- EDITD.elasticsearch_dev
```

The default ES version to install is `2.3.0`. To override, use

```
elasticsearch_version: 2.3.0
```

By default, no ES config is written - it can be set by using

```
elasticsearch_config_file: path/to/es/config
```

The path should be relative to the playbook directory.

When running ES on a Vagrant machine, it needs to listen on all interface to be
accessible from outside the vagrant box. This is added to the config by default,
but can be stopped by setting

```
elasticsearch_listen_on_all_interfaces: false
```

Finally, the head plugin is installed by default - to override this, you can use

```
elasticsearch_plugins_to_install: ["mobz/elasticsearch-head", "some_other_ES_plugin"]
```
