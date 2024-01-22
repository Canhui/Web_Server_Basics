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

**Usage 1.a.** run the web server,
```shell
(fastapi) $ cd folder1_get_a
(fastapi) $ uvicorn main:app --host 0.0.0.0
```

access the browser, 
```
http://127.0.0.1:8000/ # or http://20.243.114.88:8000/
```

Make sure that port 8000 is (port) mapped onto your (either local or cloud) router (via login your router or cloud control panel); Otherwise, outside network traffic would not access the service at port 8000.

<br>

**Usage 2.a.** run the web server,
```shell
(fastapi) $ cd folder2_get_a
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


**Usage 2.b.** run the web server,
```shell
(fastapi) $ cd folder2_get_b
(fastapi) $ uvicorn main:app --host 0.0.0.0
```

access the broswer,
```
http://127.0.0.1:8000/users/me
http://127.0.0.1:8000/users/anotherme
```


<br>

**Usage 2.c.** run the web server,
```shell
(fastapi) $ cd folder2_get_c
(fastapi) $ uvicorn main:app --host 0.0.0.0
```

access the broswer,
```
http://127.0.0.1:8000/models/lenet
http://127.0.0.1:8000/models/anothermodel
```


<br>

**Usage 2.d.** run the web server,
```shell
(fastapi) $ cd folder2_get_d
(fastapi) $ uvicorn main:app --host 0.0.0.0 
```

access the broswer,
```
http://127.0.0.1:8000/files/fa
```


<br>

**Usage 3.a.** run the web server,
```shell
(fastapi) $ cd folder3_get_a
(fastapi) $ uvicorn main:app --host 0.0.0.0
```

access the broswer and read all items in a python dict,
```
http://127.0.0.1:8000/items
```


<br>

**Usage 3.b.** run the web server,
```shell
(fastapi) $ cd folder3_get_b
(fastapi) $ uvicorn main:app --host 0.0.0.0
```

access the browser, 
```
http://127.0.0.1:8000/items/foo-item?needy=sooooneedy
```



<br>

**Usage 4.a.** run the web server,
```shell
(fastapi) $ cd folder4_post_a
(fastapi) $ uvicorn main:app --host 0.0.0.0
```

access the browser to see the post method usage, 
```
http://127.0.0.1:8000/docs
```

for example, in an ubuntu shell, run the following command,
```shell
$ curl -X 'POST' \
  'http://127.0.0.1:8000/items/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "joe",
  "description": "hi world",
  "price": 0,
  "tax": 0
}'
```




<br>

**Usage 5.a.** run the web server,
```shell
(fastapi) $ cd folder5_a
(fastapi) $ uvicorn main:app --host 0.0.0.0
```

access the browser, 
```
http://127.0.0.1:8000/items/?q=foo&q=bar
```

<br>

**Usage 5.b.** run the web server,
```shell
(fastapi) $ cd folder5_b
(fastapi) $ uvicorn main:app --host 0.0.0.0
```

access the browser, 
```
http://127.0.0.1:8000/items/
```

<br>

**Usage 5.c.** run the web server,
```shell
(fastapi) $ cd folder5_c
(fastapi) $ uvicorn main:app --host 0.0.0.0
```

access the browser,
```
http://127.0.0.1:8000/items/?item-query=foobaritems
```

<br>

**Usage 6.a.** run the web server,
```shell
(fastapi) $ cd folder6_a
(fastapi) $ uvicorn main:app --host 0.0.0.0
```

access the browser,
```
http://127.0.0.1:8000/items/10
```

<br>

**Usage 7.a.** run the web server,
```shell
(fastapi) $ cd folder7_a
(fastapi) $ uvicorn main:app --host 0.0.0.0
```















<br>

## Acknowledgement

This repo was done when working with ASTRI Security Lab, Hong Kong Applied Science and Technology Research Institute.

<br>

## Long-Term Support (LTS) Log

[18 Jan 2024]: Repetable validation, succeed.

