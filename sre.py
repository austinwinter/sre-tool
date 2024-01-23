import click
from kubernetes import client, config
from kubernetes.client.rest import ApiException

config.load_kube_config()


@click.group()
def cli():
  pass


@cli.command()
@click.argument('namespace', default="")
def list(namespace):
  kube_client = client.AppsV1Api()
  try:
    if namespace != "":
        deployments = kube_client.list_namespaced_deployment(namespace=namespace)
        deploymentList = deployments.items
        for i in deploymentList:
            click.echo(i.metadata.name)
    else:
        deployments = kube_client.list_deployment_for_all_namespaces()
        deploymentList = deployments.items
        for i in deploymentList:
            click.echo(i.metadata.name)
        return
  except ApiException as e:
    click.echo("An error occurred: {}".format(e))
    return False

@cli.command()
@click.argument('name')
@click.argument('replicas', type=int)
@click.argument('namespace')
def scale(name, replicas: int, namespace="default"):
  kube_client = client.AppsV1Api()
  try:
    body = {"spec": {"replicas": replicas}}
    kube_client.patch_namespaced_deployment_scale(name=name, namespace=namespace, body=body, pretty=True)
    click.echo(
        'The Deployment {} in namespace {} has been modified to {} replicas'.
        format(name, namespace, replicas))
    return
  except ApiException as e:
    click.echo("An error occurred: {}".format(e))
    return False


@cli.command()
@click.argument('deployment')
@click.argument('namespace')
def info(deployment, namespace="default"):
  kube_client = client.AppsV1Api()
  try:
    deployment = kube_client.read_namespaced_deployment(deployment, namespace, pretty=True)
    click.echo(deployment.metadata)
  except ApiException as e:
    click.echo("An error occurred: {}".format(e))
    return False


if __name__ == "__main__":
  cli()
