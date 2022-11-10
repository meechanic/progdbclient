import sys
from pathlib import Path
import yaml
import traceback
import progdbclient


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def eprint_exception(e, print_traceback=True, need_exit=True):
    eprint(e)
    if print_traceback:
        eprint(traceback.format_exc())
    if need_exit:
        exit(1)


class PDBCHelper:

    def __init__(self, args):
        self.args = args
        conf_file = "{}/.config/progdbclient/config.yaml".format(str(Path.home()))
        self.conf_file_object = {"profiles": {"main": {"print_traceback": True}}, "current": "main"}
        try:
            with open(conf_file, "r") as f:
                self.conf_file_object = yaml.safe_load(f)
        except Exception as e:
            pass
        if self.args.profile:
            self.conf_file_object["current"] = self.args.profile

    def get_all_confs(self):
        return self.conf_file_object

    def get_args(self):
        return self.args

    def get_current_profile(self):
        return self.conf_file_object.get("current", "main")

    def get_current_confs(self):
        return self.get_all_confs().get("profiles", {}).get(self.get_current_profile(), {})

    def get_current_conf_value(self, conf_param_name):
        return self.get_current_confs().get(conf_param_name, None)

    def get_current_conf_url(self):
        return "{}://{}:{}{}".format(self.get_current_conf_value("scheme"),
                                     self.get_current_conf_value("host"),
                                     self.get_current_conf_value("port"),
                                     self.get_current_conf_value("path"))

    def get_packages_api_instance(self):
        configuration = progdbclient.Configuration()
        configuration.host = self.get_current_conf_url()
        configuration.api_key["Authorization"] = self.get_current_conf_value("token")
        configuration.api_key_prefix["Authorization"] = "Token"
        return progdbclient.ApipackagesApi(progdbclient.ApiClient(configuration))

    def get_editions_api_instance(self):
        configuration = progdbclient.Configuration()
        configuration.host = self.get_current_conf_url()
        configuration.api_key["Authorization"] = self.get_current_conf_value("token")
        configuration.api_key_prefix["Authorization"] = "Token"
        return progdbclient.ApieditionsApi(progdbclient.ApiClient(configuration))

    def get_resources_api_instance(self):
        configuration = progdbclient.Configuration()
        configuration.host = self.get_current_conf_url()
        configuration.api_key["Authorization"] = self.get_current_conf_value("token")
        configuration.api_key_prefix["Authorization"] = "Token"
        return progdbclient.ApiresourcesApi(progdbclient.ApiClient(configuration))

