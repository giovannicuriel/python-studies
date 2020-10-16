# Legacy server

This component represents the legacy service with an intermediary layer that
implements a HTTP REST API.

It is a simple server that receives a user registration request and, each time
it receives a GET request asking for status of such registration, the server
will check whether enough time has passed. If so, it will generate a rnadom
result (ok or error).

## How to run

If you followed the other README.md files (particularly the one at the root
of this repository), you should already have Flask installed. If not, just
execute `pipenv install` to install all necessary modules (Flask included).
Remember that you need to execute this command at this repositories' root folder
(check whether file `Pipfile` is present).

After installing everything, just start this application:

```bash
python3 ./app.py
```

If everything is fine, Flask initial log should appear:

```text
 * Serving Flask app "legacy-server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://localhost:3000/ (Press CTRL+C to quit)
```

Cool! Server is up, let's poke it with some sample requests:

```bash
$ curl 0:3000/registration -H 'content-type:application/json' -d '{"name": "John Doe", "age": 30}' -X POST
{"message":"ok","result":{"userid":"17b0030e-9fd8-406a-98ca-0cd5e21c4348"}}
$ curl 0:3000/registration/17b0030e-9fd8-406a-98ca-0cd5e21c4348
{"message":"ok","result":{"age":30,"name":"John Doe","process_status":"not-ready","user_id":"17b0030e-9fd8-406a-98ca-0cd5e21c4348"}}
$ curl 0:3000/registration/17b0030e-9fd8-406a-98ca-0cd5e21c4348
{"message":"ok","result":{"age":30,"name":"John Doe","process_status":"ok","user_id":"17b0030e-9fd8-406a-98ca-0cd5e21c4348"}}
```
