import boto3
import yaml


def get_hosts(cluster_id):
    client = boto3.client('emr')
    instances = client.list_instances(ClusterId=cluster_id)["Instances"]
    return [i['PrivateIpAddress'] for i in instances if i["Status"]["State"] == "RUNNING"]


def write_hosts(hosts):
    hosts = {f"vm{i}": {"ansible_host": h}  for i, h in enumerate(hosts)}
    yml = {
        "virtualmachines": {
            "hosts": hosts,
            "vars": {
                "ansible_user": "hadoop"
            }
        }
    }

    with open('inventory.yaml', 'w') as f:
        yaml.dump(yml, f)


if __name__ == '__main__':
    write_hosts(get_hosts("j-32OK46SJXLYM1"))