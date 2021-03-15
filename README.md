# darkbox

This is a work-in-progress, all-in-one, portable, cross-platform, command-line toolkit. It's similar in nature to BusyBox, but is able to run on Windows, Linux, macOS, etc. darkbox is built for hackers, penetration testers, incident responders, and security researchers. It not only comes with many of the standard utilities that you use on a daily basis, but also tools that computer security practitioners know and love.

darkbox is written by your friendly neighborhood AbnormalSec <3

## How to get darkbox

Pre-built, portable binaries can be downloaded for Linux, Windows, and macOS in the [releases section](https://github.com/AbnormalSec/darkbox/releases).

If you'd like to compile your own binary, darkbox is compiled using [Nuitka](http://nuitka.net/). See the [Nuitka documentation](http://nuitka.net/pages/documentation.html) to learn how to get up and running, and then darkbox can be built like so: `nuitka3 --recurse-all darkbox/darkbox.py`

darkbox is also available on [PyPI](https://pypi.org/project/darkbox/) and can be installed using pip:
```
pip install darkbox
```

If you'd like to run darkbox from the git repo source code you can:
```bash
$ git clone https://github.com/abnormalsec/darkbox
$ # use it directly as a module like so
$ python -m darkbox.darkbox -v
darkbox 0.1.0
$ # or manually install it
$ python setup.py install
$ darkbox -v
darkbox 0.1.0
```

## Usage

Once you have darkbox it can be used like so:
```
$ darkbox --help
Usage: darkbox <tool> [OPTIONS]
Tools: base64, cat, cp, curl, exip, head, hostname, ls, md5sum, mv, nmap, pwd, rm, sha224sum, sha256sum, sha384sum, sha512sum, unzip, xxd, zip

$ darkbox cat hello.txt
Hello, world!

$ darkbox nmap -p22 localhost
Starting darkbox Nmap v0.0.1 at 2018-14-22 16:14 EST
Nmap scan report for localhost (127.0.0.1)
PORT      STATE
22/tcp    open
Nmap done: 1 IP addresses scanned in 0.02 seconds

$ darkbox md5sum /bin/ls
d77c1dd5bb8e39c2dd27c96c3fd2263e /bin/ls
```