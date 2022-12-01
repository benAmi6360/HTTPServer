import socket
from CustomExceptions import *
from protocol import generate_header, known_requests
from functions import functions
from PostRequests import handle_post
from utilities import *


#TODO build function to receive more than GET, POST requests
def handle_client(client, addr):
    try:
        print("Connected to", addr)
        data = client.recv(1024)
        if data[:4] ==  b'POST':
            raise HandlePostRequest()
        data = data.decode('utf-8')
        if not known_requests[data.split(" ")[0]]:
            raise UnknownRequestError()
        filename = get_filename(data)
        file = open(filename, 'rb')
        outputdata = file.read()
        header = generate_header(filename)
        print(header)
        client.sendall(header)
        client.send(outputdata)
    except (UnknownRequestError, KeyError):
        client.sendall(generate_header(code=404))
        client.send("<h1>Not a known request :(</h1>".encode())
    except HandlePostRequest:
        handle_post(client, data)
    except OSError:
        try:
            method, params = get_func(data)
            lst = get_params(params)
            res = functions[method](lst)
        except KeyError:
            client.send('HTTP/1.1 404 Not Found'.encode())
            client.send('<h1>404 Does not exist</h1>'.encode())
        else:
            header = generate_header()
            if '.' in lst:
                header = generate_header(lst)
            client.sendall(header)
            client.send(res)
    except UnicodeDecodeError as e:
        print(str(e))
        print("Unicode error")
    finally:
        client.close()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 80))
    server.listen()
    while True:
        print('The HTTP server is ready to receive')
        client, addr = server.accept()
        try:
            handle_client(client, addr)
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    main()
