import requests
import argparse
import os
from datetime import datetime
from colorama import Fore, Style
import threading
from queue import Queue

DEFAULT_WORDLIST = "wordlist/wordlist.txt"
DEFAULT_THREADS = 30


def print_banner():
    banner = """
   ____       ____  _                     
  / __ \_  __/ __ \(_)_____________ _____ 
 / / / / |/_/ / / / / ___/ ___/ __ `/ __ \\
/ /_/ />  </ /_/ / / /  (__  ) /_/ / / / /
\____/_/|_/_____/_/_/  /____/\__,_/_/ /_/ v1
        https://x-projetion.org/

    """
    print(banner)


def get_wordlist_info(wordlist):
    with open(wordlist, 'r') as f:
        lines = f.readlines()
        num_lines = len(lines)
        total_size = sum(len(line) for line in lines)
        print(f"{Fore.MAGENTA}Wordlist Info Number of Lines: {num_lines} Total Size: {total_size} threads: {DEFAULT_THREADS}{Style.RESET_ALL}")


def dir_search(url, wordlist, threads):
    get_wordlist_info(wordlist)
    print(f'Start : {url}\n')
    # Queue for thread-safe communication between threads
    queue = Queue()

    # Thread worker function
    def worker():
        while True:
            path = queue.get()
            full_url = url + '/' + path
            response = requests.get(full_url)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            status_msg = f"{response.status_code}"
            redirect_msg = f"- Redirected to: {response.url}" if response.history else ""
            file_size = len(response.content) if 'Content-Length' in response.headers else "Unknown"
            if response.status_code == 200:
                print(f"[{timestamp}] {Fore.GREEN}[INFO]{Style.RESET_ALL} [{status_msg}] [{file_size} bytes] {full_url} {redirect_msg}")
            elif response.status_code == 400:
                print(f"[{timestamp}] {Fore.RED}[INFO]{Style.RESET_ALL} [{status_msg}] [{file_size} bytes] {full_url} {redirect_msg}")
            elif response.status_code == 401:
                print(f"[{timestamp}] {Fore.RED}[INFO]{Style.RESET_ALL} [{status_msg}] [{file_size} bytes] {full_url} {redirect_msg}")
            elif response.status_code == 403:
                print(f"[{timestamp}] {Fore.RED}[INFO]{Style.RESET_ALL} [{status_msg}] [{file_size} bytes] {full_url} {redirect_msg}")
            elif response.status_code == 404:
                print(f"[{timestamp}] {Fore.RED}[INFO]{Style.RESET_ALL} [{status_msg}] [{file_size} bytes] {full_url} {redirect_msg}")
            elif response.status_code == 405:
                print(f"[{timestamp}] {Fore.RED}[INFO]{Style.RESET_ALL} [{status_msg}] [{file_size} bytes] {full_url} {redirect_msg}")
            elif response.status_code == 408:
                print(f"[{timestamp}] {Fore.RED}[INFO]{Style.RESET_ALL} [{status_msg}] [{file_size} bytes] {full_url} {redirect_msg}")
            elif response.status_code == 500:
                print(f"[{timestamp}] {Fore.RED}[INFO]{Style.RESET_ALL} [{status_msg}] [{file_size} bytes] {full_url} {redirect_msg}")
            elif response.status_code == 502:
                print(f"{Fore.RED}[-] Bad Gateway{Style.RESET_ALL}")
            elif response.status_code == 503:
                print(f"[{timestamp}] {Fore.RED}[INFO]{Style.RESET_ALL} [{status_msg}] [{file_size} bytes] {full_url} {redirect_msg}")
            elif response.status_code == 504:
                print(f"[{timestamp}] {Fore.RED}[INFO]{Style.RESET_ALL} [{status_msg}] [{file_size} bytes] {full_url} {redirect_msg}")

            queue.task_done()

    # Start the worker threads
    for _ in range(threads):
        t = threading.Thread(target=worker)
        t.daemon = True  # Threads are daemons so they will exit when the main thread exits
        t.start()

    # Populate the queue with paths from the wordlist
    with open(wordlist, 'r') as f:
        for line in f:
            queue.put(line.strip())

    # Wait for all threads to complete
    queue.join()

if __name__ == "__main__":
    print_banner()
    parser = argparse.ArgumentParser(description="0xdirsan is a simple program designed to search for directories in a file system")
    parser.add_argument("-w", "--wordlist", help="Path to wordlist file", default=DEFAULT_WORDLIST)
    parser.add_argument("-u", "--url", help="Target URL use http / https", required=True)
    parser.add_argument("-t", "--threads", help="Number of threads (default 30)", type=int, default=DEFAULT_THREADS)
    args = parser.parse_args()

    if not os.path.exists(args.wordlist):
        print("Wordlist file not found. Using default wordlist.")
        args.wordlist = DEFAULT_WORDLIST
    
    dir_search(args.url, args.wordlist, args.threads)
