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
http://20.243.114.88:8000/ # or http://127.0.0.1:8000/
```

Make sure that port 8000 is (port) mapped onto your (either local or cloud) router (via login your router or cloud control panel); Otherwise, outside network traffic would not access the service at port 8000.

**Usage 2.** run the web server,
```shell
(fastapi) $ cd folder2
(fastapi) $ uvicorn main:app --host 0.0.0.0
```

access the broswer,
```
http://20.243.114.88:8000/items/foo
```

Again, make sure that port 8000 is mapped onto your router.


