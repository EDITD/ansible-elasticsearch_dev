# ansible-elasticsearch_dev

This will install elasticsearch and its head plugin.

I wouldn't recommend using this for a production system! For one, it only
installs elasticsearch and it doesn't try to form a cluster.


```
roles:
- EDITD.elasticsearch_dev
```

Optionally a version can be specified.

```
roles:
- EDITD.elasticsearch_dev
  elasticsearch_version: 1.7.4
```


