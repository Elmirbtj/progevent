import time
def task(i):
    print(f"Task {i} starts")
    time.sleep(1)
    print(f"Task {i} ends")
    start = time.perf_counter()
task(1)
task(2)
end = time.perf_counter()
print(f"Tasks ended in {round(end -start, 2)} second(s)")


-------------
import time
import concurrent.futures
import requests

img_urls = [
          "https://images3.alphacoders.com/695/695428.jpg"]

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[len(img_url.split('/'))-1]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")
start = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)
end = time.perf_counter()
print(f"Tasks ended in {round


---
import time
import concurrent.futures
import requests

img_urls = [
          "https://images3.alphacoders.com/695/695428.jpg"]

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[len(img_url.split('/'))-1]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")
start = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)
end = time.perf_counter()
print(f"Tasks ended in {round(end - start, 2)} second(s)")


--------------
import threading
import time



def task(i):
    print(f"Task {i} starts")
    time.sleep(1)
    print(f"Task {i} ends")

start = time.perf_counter() #demarer la thread
T = []
print(dir(T))

for i in range(100):
    T.append(threading.Thread(target=task, args=[i]))

for i in range(len(T)):
    T[i].start()
for i in range(len(T)):
    T[i].join() #attendre que les thread se termine
end = time.perf_counter()
print(f"Tasks ended in {round(end - start, 2)} second(s)")

-----------------

import threading
import time

def task(i):
    print(f"Task {i} starts for {i+1} second(s)")
    time.sleep(i+1)
    print(f"Task {i} ends")

start = time.perf_counter()
T = []
for i in range(100):
    T.append(threading.Thread(target=task, args=[i]))
for i in range(len(T)):
    T[i].start()
for i in range(len(T)):
    T[i].join()


end = time.perf_counter()
print(f"Tasks ended in {round(end - start, 2)} second(s)")

-------------------
import time
import multiprocessing
def task():
    print(f"Task starts for 1 second")
    time.sleep(1)
    print(f"Task ends")

if __name__ == '__main__':
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)
    p1.start()
    p2.start()
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")

