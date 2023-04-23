import sh
import yaml

from utils import (
    microk8s_enable,
    wait_for_pod_state,
    microk8s_disable,
    kubectl_get
)


def addon_info(status, name):
    for addon in status['addons']:
        if addon['name'] == name:
            return addon
    return None


class TestAddons(object):
    def test_appsmith(self):
        NAME = 'appsmith-k8s'
        microk8s_enable(NAME)
        # wait_for_pod_state("appsmith-0", "default", "running")
        print(kubectl_get("all"))
        status = yaml.safe_load(sh.microk8s.status(format="yaml"))
        info = addon_info(status, NAME)
        assert info['status'] == 'enabled'
        microk8s_disable(NAME)

    def test_n8n(self):
        NAME = 'n8n-k8s'
        microk8s_enable(NAME)
        print(kubectl_get("all"))
        status = yaml.safe_load(sh.microk8s.status(format="yaml"))
        info = addon_info(status, NAME)
        assert info['status'] == 'enabled'
        microk8s_disable(NAME)
