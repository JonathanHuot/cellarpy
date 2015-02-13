from bottle import response


def guess_type(filename, resp=response):
    import mimetypes

    charset = 'UTF-8'
    mimetype, encoding = mimetypes.guess_type(filename)
    if not mimetype and filename.find(".woff2"):
        mimetype, encoding = mimetypes.guess_type(filename + ".woff")
        
    if encoding: headers['Content-Encoding'] = encoding

    if mimetype:
        if mimetype[:5] == 'text/' and charset and 'charset' not in mimetype:
            mimetype += '; charset=%s' % charset
        resp.headers['Content-Type'] = mimetype
