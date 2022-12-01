def get_filename(req):
    filename = req.split()[1][1:]
    if filename == '':
        filename = './index.html'
    return filename


def get_func(req):
    inp = req.split(" ")[1].split('?')
    method = inp[0][1:]
    params = inp[1]
    return method, params


def get_params(params):
    lst = []
    if ('&' in params):
        params = params.split('&')
        for param in params:
            lst.append(param.split('=')[-1])
    else:
        lst = params.split('=')[-1]
    return lst


def log(msg):
    print("RECEIVED:", msg)