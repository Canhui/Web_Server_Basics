## 1. Introduction

This repository motivates to run and debug a FastAPI-based web server.

<br>

## 2. Requirements

We suggest install the following dependencies on miniconda (or venv alternatively).

**R1.** setup a conda environment for python 3.9
```shell
$ conda create -n fastapi python=3.9
$ conda activate fastapi
(fastapi) $
```

**R2.** install fastapi and uvicorn
```shell
(fastapi) $ pip install fastapi
(fastapi) $ pip install "uvicorn[standard]"
```

<br>


## 3. Usage

**U1.** run the web server,
```shell
(fastapi) $ cd folder1
(fastapi) $ uvicorn main:app
```

access the browser,
```
http://127.0.0.1:8000/
```

**U2.** run the web server,
```shell
(fastapi) $ cd folder2
(fastapi) $ uvicorn main:app
```

access the broswer,
```
http://127.0.0.1:8000/items/foo
```



