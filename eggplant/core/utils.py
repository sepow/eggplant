import os
import uuid

from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site


def absolute_url_reverse(url_name=None, **kwargs):
    domain = Site.objects.get_current().domain
    path = '/'
    if url_name:
        path = reverse(url_name, **kwargs)
    full_url = "{}://{}{}".format(settings.DEFAULT_HTTP_PROTOCOL,
                                  domain, path)
    return full_url


def generate_upload_path(instance, filename, dirname=None):
    """
        Generate path with random file name for FileField.
    """
    ext = os.path.splitext(filename)[1].lstrip('.')
    rand_name = "{}.{}".format(uuid.uuid4().hex, ext)
    if dirname:
        rand_name = "{}/{}".format(dirname, rand_name)
    return rand_name
