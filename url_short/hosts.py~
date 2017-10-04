from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'short-n', settings.ROOT_URLCONF, name = 'short-n'),
    host(r'(?!short-n).*', 'url_short.hostsconf.urls', name = 'wildcard'),
)
