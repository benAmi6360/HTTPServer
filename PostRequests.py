from protocol import generate_header
from utilities import log

def handle_post(client, temp):
    try: 
        data = str(temp)
        size = int(data.split("Content-Length: ")[1].split('\\r\\n')[0])
        filename = 'uploads/' + data.split()[1].split('?')[1].split('=')[-1]
        log(size)
        req = client.recv(size * 2)
        log(len(req))
        imp = size - len(req)
        log(imp)
        content = temp[1024 - imp:] + req
        with open(filename, 'wb') as file:
            file.write(content)
    except Exception as e:
        log(str(e))
        client.send(generate_header(code=404))
    else:
        client.send(generate_header(code=200))
