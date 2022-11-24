import threading
import time
import sys
import multiprocessing
import concurrent.futures
import requests


img_urls = [
    'https://thumbs.dreamstime.com/b/sed-lumineux-du-soleil-avec-le-jpg-jaune-de-la-lumi%C3%A8re-169481284.jpg',
    'https://thumbs.dreamstime.com/b/sed-lumineux-du-soleil-avec-le-jpg-jaune-de-la-lumi%C3%A8re-169481284.jpg'

]

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[5]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded..')


def task_threading():
    t1 = threading.Thread(target=download_image, args=(img_urls[0],))
    t2 = threading.Thread(target=download_image, args=(img_urls[1],))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

def task_multiprocessing ():
    p1 = multiprocessing.Process(target=download_image, args=(img_urls[0],))
    p2 = multiprocessing.Process(target=download_image, args=(img_urls[1],))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


def task_pool():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(download_image, img_urls)

if __name__ == '__main__':
    start = time.perf_counter()
    task_threading()
    finish = time.perf_counter()
    print(f'THREADING in {round(finish-start, 3)} second(s)')

    start = time.perf_counter()
    task_multiprocessing()
    finish = time.perf_counter()
    print (f"MULTIPROCCESING dans {round(finish-start, 3)} second(s)")

    start = time.perf_counter()
    task_pool()
    finish = time.perf_counter()
    print(f'POOL in {round(finish-start, 3)} second(s)')