# Log de Ações ao configurar API do Calibre

## Sobre o ambiente
- OS: ZorinOS 15
- Python: 3.9.6 (ambiente virtual limpo)

## Ambiente em nuvem
- OS: Ubuntu 21.04
- Python: 3.9.5 (limpo)


## Comandos e Pacotes Instalados
- **PKG-CONFIG**
-> sudo apt install pkg-config

- **Qt-Make**
-> sudo apt install qt5-default 
**or** 
sudo apt-get install qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools (on Ubuntu 21.04)

- **qtbase5-private-dev** (needed for _/usr/lib/x86_64-linux-gnu/libQt5FontDatabaseSupport.a_ found by apt-file)
-> sudo apt install -y qtbase5-private-dev
<!-- - **NPM** (não funcionou/não foi usado)
-> sudo apt install npm -->

- **libfreetype6-dev**
-> sudo apt install libfreetype6-dev

- **libfontconfig1-dev**
-> sudo apt install libfontconfig1-dev

- **libhunspell-dev**
-> sudo apt install -y libhunspell-dev

- **libpodofo-dev**
-> sudo apt install -y libpodofo-dev

- **pip** (repo manager for python)
-> sudo apt install -y python3-pip

- **msgpack** (python module for json)
-> python3 -m pip install msgpack

- **PyQt5**
-> python3 -m pip install PyQt5

- **sip**
-> python3 -m pip install sip

- **PyQt-builder**
-> python3 -m pip install PyQt-builder

- **pyqt5-dev**
-> sudo apt install pyqt5-dev

- **libicu67** (available on Ubuntu 21.04 and later)
-> sudo apt install -y libicu-dev libicu67

- **libhyphen-dev**
-> sudo apt install libhyphen-dev

- **libsqlite3-dev**
-> sudo apt install libsqlite3-dev

- **libstemmer-dev**
-> sudo apt-get install libstemmer-dev

- **libstemmer-dev**
-> sudo apt install libstemmer-dev

- **libusb-1.0-0-dev**
-> sudo apt install -y libusb-1.0-0-dev

- **libmtp-dev**
-> sudo apt install -y libmtp-dev

- **pyqt5.qtwebengine**
-> sudo apt install python3-pyqt5.qtwebengine

- **dateutil**
-> sudo apt install python3-dateutil

- **libexecs-dev**

- **qtcreator**
sudo apt install qtcreator (didn't fix)

- **apt-file** (searches for specific files inside repositories and tells the packages containing them)
-> sudo apt install -y apt-file
-> sudo apt-file update

## Build Calibre Headless Development Environment
- python3 calibre/setup.py bootstrap
- python3 calibre/setup.py develop

It's sunday, Aug 8, 18:15 and I'm already so fucking frustrated with Calibre I might as well delete it. I'm gonna try another way: full source install of calibre and then running a python script importing calibre and getting ready to run calibre code. Wish me luck!

Dear diary, I'm crying in fetal position.

libghc-xdg-basedir-dev
sudo apt install libghc-xdg-basedir-dev

sudo apt -y install xdg-utils xvfb imagemagick

giving up on calibre for now, moving to use [kan](https://pypi.org/project/kan/) to get books data.