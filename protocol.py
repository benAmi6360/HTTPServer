known_requests = {
    "GET": True,
    "POST": True,
}

file_type = {
    'html': 'text/html; charset=utf-8',
    'jpg': 'image/jpeg',
    'css': 'text/css',
    'gif': 'image/webp',
    'ico': 'image/vnd.microsoft.icon',
    'js': 'text/javascript; charset=utf-8',
    'txt': 'text/plain',
    'png': 'image/png'
}

def generate_header(filename='txt', code=200):
    return (f"""HTTP/1.1 {code} OK
Content-Type: """ + file_type[filename.split(".")[-1]] + '\n\n').encode()
