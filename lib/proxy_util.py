import httplib
import threading

host = "127.0.0.1"
port = "8118"
timeout = 10

def get_proxy():
    try:
        conn = httplib.HTTPConnection(host=host, port=port, timeout=timeout)
        path = "/get"
        conn.request("GET", path)
        response = conn.getresponse()
        proxy = response.read()
        conn.close()
    except:
        return None
    if not proxy:
        return None
    return proxy

def invalid(proxy):
    try:
        conn = httplib.HTTPConnection(host=host, port=port, timeout=timeout)
        path = "/invalid?p=%s" % proxy
        conn.request("GET", path)
        res = conn.getresponse()
        conn.close()
    except:
        pass

def invalid_noblock(proxy):
    t = threading.Thread(target=invalid, args=[proxy])
    t.start()
    return

if __name__ == "__main__":
    proxy = get_proxy()
    print proxy
    invalid_noblock(proxy)

