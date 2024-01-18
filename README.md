## 1. Introduction

This repository motivates to run and debug a FastAPI-based web server.

<br>

## 2. Requirements

We suggest install the following dependencies on miniconda (or venv alternatively).

**Requirement 1.** setup a conda environment for python 3.9
```shell
$ conda create -n fastapi python=3.9
$ conda activate fastapi
(fastapi) $
```

**Requirement 2.** install fastapi and uvicorn
```shell
(fastapi) $ pip install fastapi
(fastapi) $ pip install "uvicorn[standard]"
```

<br>

## 3. Usages

**Usage 1.** run the web server,
```shell
(fastapi) $ cd folder1
(fastapi) $ uvicorn main:app --host 0.0.0.0
```

access the browser, 
```
http://127.0.0.1:8000/ # or http://20.243.114.88:8000/
```

Make sure that port 8000 is (port) mapped onto your (either local or cloud) router (via login your router or cloud control panel); Otherwise, outside network traffic would not access the service at port 8000.

<br>

**Usage 2.** run the web server,
```shell
(fastapi) $ cd folder2
(fastapi) $ uvicorn main:app --host 0.0.0.0
(fastapi) $ uvicorn main2:app --host 0.0.0.0
```

access the first item of the target folder via the broswer,
```
http://127.0.0.1:8000/items/foo
http://127.0.0.1:8000/items/3 # ok, though no file or folder named '3'.
```

Again, make sure that port 8000 is mapped onto your router.

<br>

**Usage 3.** run the web server,
```shell
(fastapi) $ cd folder3
(fastapi) $ uvicorn main:app --host 0.0.0.0
```

access the broswer,
```
http://127.0.0.1:8000/users/me
http://127.0.0.1:8000/users/anotherme
```

<br>

**Usage 4.** run the web server,
```shell
(fastapi) $ cd folder4
(fastapi) $ uvicorn main:app --host 0.0.0.0
```

access the broswer,
```
http://127.0.0.1:8000/models/lenet
http://127.0.0.1:8000/models/anothermodel
```

<br>

**Usage 5.** run the web server,
```shell
(fastapi) $ cd folder5
(fastapi) $ uvicorn main:app --host 0.0.0.0 
```

access the broswer,
```
http://127.0.0.1:8000/files/fa
```

<br>

**Usage 6.** run the web server,
```shell
(fastapi) $ cd folder6
(fastapi) $ uvicorn main:app --host 0.0.0.0
```

access the broswer and read all items in a python dict,
```
http://127.0.0.1:8000/items
```

<br>

**Usage 7.** run the web server,
```shell
(fastapi) $ cd folder7
(fastapi) $ uvicorn main:app --host 0.0.0.0
```

access the browser, 
```
http://127.0.0.1:8000/items/foo-item?needy=sooooneedy
```
