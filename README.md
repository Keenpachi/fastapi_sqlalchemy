## About

Fastapi app with usage of SQLAlchemy

## Installation
### mySQL

```bash
sudo apt install mysql-server
sudo mysql

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY {password};
FLUSH PRIVILEGES;
CREATE DATABASE ziptie;
```
### App
```bash
cd ziptie
pip install -r requirements.txt
```

## Setup
update password in .env file

```
password = {password}
```

## Run

```bash
uvicorn app.main:app --reload
```

## Usage

```
http://127.0.0.1:8000/docs#/
```

