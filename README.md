# SRE Tool

This tool is used to automate some of the functions required to manage a kubernetes cluster. It currently uses the python kuberentes client and click for parsing arguments.

## Available commands:
    - sre list - Lists all deployments by default, but can accept the argument `namespace` to list deployments from specific namespace
      Optional Argument:
        - namespace : Limits list to specific namespace
    - sre scale - Scales the specified deployment to selected replicas
      Required Arguments:
        - name : deployment name
        - replicas: Int replicas to scale deployment to.
        - namespace: Specify namespace - defaults to 'default' namespace
    - sre info - lists deployment information
      Required Arguments:
        - deployment : Deployment to get info from
        - namespace : Namespace deployment is in - defaults to 'default' namespace

## Installation instructions
  1. Clone the repo
  1. cd into the repository
  2. run `pip install .`
