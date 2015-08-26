from django import template
from django.http import HttpResponse
from django.utils.encoding import force_text

import mimetypes


def publish(request, path):
    if path == '' or path.endswith('/'):
        path = path + "index.html"

    abspath = _path(path)
    mt, dmy = mimetypes.guess_type(abspath)
    res = File(open(abspath))

    if mt == 'text/html':
        t = template.Template(
            force_text(res.read(), encoding="cp932"))
        return HttpResponse(t.render(template.Context()))

    return HttpResponse(res, content_type=mt)
