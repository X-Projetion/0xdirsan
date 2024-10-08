<p align="center">
    <img src="https://raw.githubusercontent.com/X-Projetion/0xdirsan/main/0xdirsan.png" alt="0xdirsan" width="60%">
</p>
<h4 align="center">0xdirsan is a simple program designed to search for directories in the file system</h4>
<p align="center">
  <a href="https://goreportcard.com/report/github.com/X-Projetion/split-files/"><img src="https://goreportcard.com/badge/github.com/X-Projetion/split-files"></a>
  <a href="https://github.com/X-Projetion/split-files/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
  <a href="https://github.com/X-Projetion/split-files/releases"><img src="https://img.shields.io/github/release/X-Projetion/split-files"></a>
  <br>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/made%20with-Python-pink.svg"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-pink.svg"></a>
  <a href="https://github.com/X-Projetion/split-files/issues"><img src="https://img.shields.io/github/issues/X-Projetion/split-files?color=pink"></a>
</p>
<p align="center">
  • <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#pypi-installation">Installation via PyPI</a> •
  <a href="#usage">Usage</a> •
  <a href="#help">Help</a> •
  <a href="#disclaimer">Disclaimer</a> •
  <a href="#license">License</a>
</p>

## 0xdirsan
0xdirsan is a simple program designed to perform directory searches in a file system using a brute-force method with a given list of words. This program is intended for security testing and can be used by security researchers to discover hidden directories and files on web servers.

## Feature
- Brute-Force Based Search: 0xdirsan uses brute-force techniques to try different combinations of paths based on the provided word list, helping to uncover directories that might otherwise be invisible.
- Use of Multi-Threading: This program supports the use of multiple threads to speed up the search process, thereby increasing efficiency and reducing the time required to find a directory.
- HTTP Status Information: Each request will display the HTTP status code and other related information, so that users can know whether the directory they are looking for exists or not.
- Custom Word List Support: Users can provide their own word lists, allowing flexibility in searches.
- Simple User Interface: With the use of command line arguments, 0xdirsan is easy to use by anyone, even those new to the tool.


## Installation
### Install and run the 0xdirsan script via pip
```sh
root@Lutfifakee:~$ pip install 0xdirsan
root@Lutfifakee:~$ xdirsan
```

Follow these steps to install 0xdirsan :

1. **Clone repositori**:
   ```sh
    root@Lutfifakee:~$ git clone https://github.com/X-Projetion/0xdirsan.git
    root@Lutfifakee:~$ cd 0xdirsan
    ```
2. **Clone repositori**:
   ```sh
   root@Lutfifakee:~$ pip install -r requirements.txt
    ```

## Usage
- root@Lutfifakee:~$ python 0xdirsan.py -u <TARGET_URL>

## Help
```bash
root@Lutfifakee:~$ xdirsan -h

   ____       ____  _
  / __ \_  __/ __ \(_)_____________ _____
 / / / / |/_/ / / / / ___/ ___/ __ `/ __ \
/ /_/ />  </ /_/ / / /  (__  ) /_/ / / / /
\____/_/|_/_____/_/_/  /____/\__,_/_/ /_/ v0.1.0
        https://x-projetion.org/

usage: xdirsan [-h] [-w WORDLIST] [-u URLS] [-f FILE] [-t THREADS] [-v]

0xdirsan is a simple program designed to search for directories in a file system

options:
  -h, --help            show this help message and exit
  -w WORDLIST, --wordlist WORDLIST
                        Path to wordlist file
  -u URLS, --urls URLS  Target URLs separated by comma (e.g. x-projetion.org)
  -f FILE, --file FILE  File containing target URLs, one per line
  -t THREADS, --threads THREADS
                        Number of threads (default 30)
  -v, --version         Show version
```
### Connect with me:

- **Website:** [X-Projetion.org](https://x-projetion.org/)
- **Pypi:** [0xdirsan](https://pypi.org/project/0xdirsan/)
- **Instagram:** [@lutfifakee](https://www.instagram.com/lutfifakee/)
  
## Disclaimer
0xdirsan is provided for educational purposes only. Use of this program for illegal or unethical activities is not recommended. The developer is not responsible for any actions taken by users.

<br>
<p>0xdirsan was developed by X-Projetion, a software developer with a focus on security and penetration testing. You can visit the website <a href="https://x-projetion.org/">X-Projetion.org</a> for more information or follow <a href="https://www.instagram. com/lutfifakee/">Instagram</a> X-Projetion for the latest updates.</p>


