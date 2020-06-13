import socket
import datetime

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as so:
    so.sendto(b"", ("127.0.0.1", 123))
    time, _ = so.recvfrom(254)
    l_time = time.decode("utf-8")
    r_time = datetime.datetime.now()
    print(f"Действительное время:   {r_time}")
    print(f"Время от сервера:   {l_time}")
    fake_time = datetime.datetime.strptime(l_time, "%Y-%m-%d %H:%M:%S.%f")
    if fake_time > datetime.datetime.now():
        delta = fake_time - r_time
    else:
        delta = r_time - fake_time

    print(f"Сервер врёт на:   {delta}")
