import socket
import time


class ClientError(Exception):
    """Общий класс исключений клиента"""
    pass


class ClientSocketError(ClientError):
    """Исключение, выбрасываемое клиентом при сетевой ошибке"""
    pass


class ClientProtocolError(ClientError):
    """Исключение, выбрасываемое клиентом при ошибке протокола"""
    pass


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.metrics_dict = {}
        try:
            self.connection = socket.create_connection((host, port), timeout)
        except socket.error as err:
            raise ClientSocketError("error create connection", err)

    def put(self, key, value, timestamp=None):
        if not timestamp:
            timestamp = int(time.time())
        try:
            self.connection.sendall(
                f"put {key} {value} {timestamp}\n".encode())
        except socket.error as err:
            raise ClientSocketError("error send data", err)
        response = self.connection.recv(4096)
        response = response.decode()
        if "error" in response:
            raise ClientError

    def get(self, key):
        self.connection.sendall(
            f"get {key}\n".encode())
        response = self.connection.recv(4096)
        response = response.decode().split(" ")
        if response == "ok\n\n":
            return {}
        else:
            temporary_list = []
            metric_exist_index = response[0].find('\n')
            metric_variable = response[0][metric_exist_index + 1:]
            self.metrics_dict[metric_variable] = []
            for i in range(1, len(response)):
                metric_exist_index = response[i].find('\n')
                if metric_exist_index != -1:
                    temporary_list.append(
                        int(response[i][0:metric_exist_index]))
                    temporary_list.append(temporary_list.pop(0))
                    self.metrics_dict[metric_variable].append(
                        tuple(temporary_list))
                    temporary_list = []
                    metric_variable = response[i][metric_exist_index + 1:]
                    try:
                        if metric_variable != '\n':
                            self.metrics_dict[metric_variable]
                    except KeyError:
                        self.metrics_dict[metric_variable] = []

                if metric_exist_index == -1:
                    temporary_list.append(float(response[i]))
            return self.metrics_dict


if __name__ == '__main__':
    client = Client("127.0.0.1", 8888, timeout=15)

    client.put("palm.cpu", 0.5, timestamp=1150864247)
    client.put("palm.cpu", 2.0, timestamp=1150864248)
    client.put("palm.cpu", 0.5, timestamp=1150864248)

    client.put("eardrum.cpu", 3, timestamp=1150864250)
    client.put("eardrum.cpu", 4, timestamp=1150864251)
    client.put("eardrum.memory", 4200000)
    print(client.get("*"))
