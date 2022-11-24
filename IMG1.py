import time
import threading
import concurrent.futures
import requests
import multiprocessing

img_urls = ['https://thumbs.dreamstime.com/b/sed-lumineux-du-soleil-avec-le-jpg-jaune-de-la-lumi%C3%A8re-169481284.jpg']
def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[len(img_url.split('/'))-1]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")

if __name__ == '__main__':
    start = time.perf_counter()
    T = []
    for i in img_urls:
        thread = multiprocessing.Process(target=download_image, kwargs={'img_url':i})
        T.append(thread)
    for thread in T:
        thread.start()
    for thread in T:
        thread.join()  # attendre la fin du thread
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")