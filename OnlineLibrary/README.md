# Books

**Dependencies:** Python 3.8.0, Pip, Virtualenv, Npm

#### Create virtual environment 

```sh
git clone https://github.com/mertbilgic/Books.git
cd books
virtualenv --python=/usr/local/bin/python3.8  venv
```

#### Install depedencies

```sh
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### Install Styles and Scripts

```sh
cd static
$ npm install
```
### Start

```sh
$ python main.py 
```