# gRPC HBase

This repository contains a gRPC server which emulates the HBase Java API and clients for this server.
The intent is to make this a kubernetes-first application which will run as a sidecar container in the pod of an application.
The gRPC service is then exposed over localhost to your app.

## Server
The server is written in Scala. It supports Kerberos authentication. Because this server will run alongside each container, each instance can manage its own keytab.
Fetched results are streamed to the client cell-by-cell.

## Clients
At this point only a python client is available. It has integration with pandas to load results into a DataFrame.

## TODO
* Add support for more operations to server (Put, Delete)
* Test
* Add documentation
* Create Dockerfile for server
* Create clients in more languages (Rust (with Tonic), ...)
* Structure Python client as proper library
* Create example k8s deployments with server and client in one pod (targeting Minikube)

## Run example

Create a resource file named `secrets.conf` in `server/src/main/resources` and populate it with HBase (and Kerberos if wanted) config.

Then start the server and wait for it to be ready:
```shell script
cd server
sbt run
```

Create a virtual python environment in your preferred way and activate it.

Now install dependencies:

```shell script
pip install -r python-client/dev-requirements.txt
```

Then run the client:

```shell script
python python-client/src/main.py
```
