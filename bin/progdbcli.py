#!/usr/bin/env python3

import os
import sys
import argparse
import yaml
from progdbclient.helpers import (PDBCHelper, eprint_exception, eprint)
from progdbclient.rest import ApiException
import progdbclient

yaml.Dumper.ignore_aliases = lambda *args : True
print_traceback = True
print_result = True


def parse_args(argv):
    self_name = os.path.basename(argv[0])
    parent_parser = argparse.ArgumentParser(prog=self_name,
                                            description="Client for software database")
    subparsers = parent_parser.add_subparsers(help="Endpoint groups")
    subparsers.required = True
    subparsers.dest = "group"
    subparser_packages = subparsers.add_parser("packages", help="Utilities for work with Packages")
    subparser_packages.add_argument("--action", type=str, help="Possible actions: list | create | get | update | delete")
    subparser_packages.add_argument("--profile", type=str, help="Config profile")
    subparser_packages.add_argument("--id", type=str, help="Entity ID")
    subparser_packages.add_argument("--input-file", type=str, help="Input file")
    subparser_replicas = subparsers.add_parser("replicas", help="Utilities for work with Replicas")
    subparser_replicas.add_argument("--action", type=str, help="Possible actions: list | get | create")
    subparser_replicas.add_argument("--profile", type=str, help="Config profile")
    subparser_replicas.add_argument("--id", type=str, help="Entity ID")
    subparser_replicas.add_argument("--input-file", type=str, help="Input file")
    subparser_modules = subparsers.add_parser("modules", help="Utilities for work with Modules")
    subparser_modules.add_argument("--action", type=str, help="Possible actions: list | get | create")
    subparser_modules.add_argument("--profile", type=str, help="Config profile")
    subparser_modules.add_argument("--id", type=str, help="Entity ID")
    subparser_modules.add_argument("--input-file", type=str, help="Input file")
    subparser_sourcereplicas = subparsers.add_parser("source-replicas", help="Utilities for work with SourceReplicas")
    subparser_sourcereplicas.add_argument("--action", type=str, help="Possible actions: list | get | create")
    subparser_sourcereplicas.add_argument("--profile", type=str, help="Config profile")
    subparser_sourcereplicas.add_argument("--id", type=str, help="Entity ID")
    subparser_sourcereplicas.add_argument("--input-file", type=str, help="Input file")
    subparser_fsobjects = subparsers.add_parser("fs-objects", help="Utilities for work with FSObjects")
    subparser_fsobjects.add_argument("--action", type=str, help="Possible actions: list | get | create")
    subparser_fsobjects.add_argument("--profile", type=str, help="Config profile")
    subparser_fsobjects.add_argument("--id", type=str, help="Entity ID")
    subparser_fsobjects.add_argument("--input-file", type=str, help="Input file")
    return parent_parser.parse_args(sys.argv[1:])


def main():
    args = parse_args(sys.argv)
    pdbch = PDBCHelper(args)
    obj = None
    if args.group == "packages":
        if args.action == "list" or args.action == None:
            try:
                api_instance = pdbch.get_package_api_instance()
                res = api_instance.apipackage_list()
                if res:
                    obj = [i.to_dict() for i in res]
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "get":
            try:
                id = int(args.id)
            except TypeError as e:
                eprint("Incorrect or missing ID")
                exit(1)
            try:
                api_instance = pdbch.get_package_api_instance()
                obj = api_instance.apipackage_read(id).to_dict()
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "create":
            if not args.input_file:
                eprint("Missing input file")
                exit(1)
            try:
                with open(args.input_file, "r") as f:
                    res_pre = yaml.safe_load(f)
            except (OSError, yaml.YAMLError) as e:
                eprint_exception(e, print_traceback=print_traceback)
                exit(1)
            package_keys = ["name", "human_description", "machine_description", "main_prog_language", "package_collection"]
            res = {correct_key: res_pre[correct_key] for correct_key in package_keys}
            data = progdbclient.Package(**res)
            try:
                api_instance = pdbch.get_package_api_instance()
                obj = api_instance.apipackage_create(data).to_dict()
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "update":
            if not args.input_file:
                eprint("Missing input file")
                exit(1)
            try:
                id = int(args.id)
            except TypeError as e:
                eprint("Incorrect or missing ID")
                exit(1)
            try:
                with open(args.input_file, "r") as f:
                    res_pre = yaml.safe_load(f)
            except (OSError, yaml.YAMLError) as e:
                eprint_exception(e, print_traceback=print_traceback)
                exit(1)
            package_keys = ["name", "human_description", "machine_description", "main_prog_language", "package_collection"]
            res = {correct_key: res_pre[correct_key] for correct_key in package_keys}
            data = progdbclient.Package(**res)
            try:
                api_instance = pdbch.get_package_api_instance()
                obj = api_instance.apipackage_update(id, data).to_dict()
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "delete":
            try:
                id = int(args.id)
            except TypeError as e:
                eprint("Incorrect or missing ID")
                exit(1)
            try:
                api_instance = pdbch.get_package_api_instance()
                api_instance.apipackage_delete(id)
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        else:
            eprint("Not implemented for action: {}".format(args.action))
            exit(1)
    elif args.group == "replicas":
        if args.action == "list" or args.action == None:
            try:
                api_instance = pdbch.get_replica_api_instance()
                res = api_instance.apireplica_list()
                if res:
                    obj = [i.to_dict() for i in res]
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "get":
            try:
                id = int(args.id)
            except TypeError as e:
                eprint("Incorrect or missing ID")
                exit(1)
            try:
                api_instance = pdbch.get_replica_api_instance()
                obj = api_instance.apireplica_read(id).to_dict()
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "create":
            if not args.input_file:
                eprint("Missing input file")
                exit(1)
            try:
                with open(args.input_file, "r") as f:
                    res_pre = yaml.safe_load(f)
            except (OSError, yaml.YAMLError) as e:
                eprint_exception(e, print_traceback=print_traceback)
                exit(1)
            replica_keys = ["name", "human_description", "machine_description", "is_main", "is_installation", "location", "replica_collection", "module"]
            res = {correct_key: res_pre[correct_key] for correct_key in replica_keys}
            data = progdbclient.Replica(**res)
            try:
                api_instance = pdbch.get_replica_api_instance()
                obj = api_instance.apireplica_create(data).to_dict()
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "update":
            if not args.input_file:
                eprint("Missing input file")
                exit(1)
            try:
                id = int(args.id)
            except TypeError as e:
                eprint("Incorrect or missing ID")
                exit(1)
            try:
                with open(args.input_file, "r") as f:
                    res_pre = yaml.safe_load(f)
            except (OSError, yaml.YAMLError) as e:
                eprint_exception(e, print_traceback=print_traceback)
                exit(1)
            replica_keys = ["name", "human_description", "machine_description", "is_main", "is_installation", "location", "replica_collection", "module"]
            res = {correct_key: res_pre[correct_key] for correct_key in replica_keys}
            data = progdbclient.Replica(**res)
            try:
                api_instance = pdbch.get_replica_api_instance()
                obj = api_instance.apireplica_update(id, data).to_dict()
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "delete":
            try:
                id = int(args.id)
            except TypeError as e:
                eprint("Incorrect or missing ID")
                exit(1)
            try:
                api_instance = pdbch.get_replica_api_instance()
                api_instance.apireplica_delete(id)
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        else:
            eprint("Not implemented for action: {}".format(args.action))
            exit(1)
    elif args.group == "modules":
        if args.action == "list" or args.action == None:
            try:
                api_instance = pdbch.get_module_api_instance()
                res = api_instance.apimodule_list()
                if res:
                    obj = [i.to_dict() for i in res]
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "get":
            try:
                id = int(args.id)
            except TypeError as e:
                eprint("Incorrect or missing ID")
                exit(1)
            try:
                api_instance = pdbch.get_module_api_instance()
                obj = api_instance.apimodule_read(id).to_dict()
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "create":
            if not args.input_file:
                eprint("Missing input file")
                exit(1)
            try:
                with open(args.input_file, "r") as f:
                    res_pre = yaml.safe_load(f)
            except (OSError, yaml.YAMLError) as e:
                eprint_exception(e, print_traceback=print_traceback)
                exit(1)
            module_keys = ["name", "human_description", "machine_description", "prog_language", "location", "sourcereplica_collection", "module"]
            res = {correct_key: res_pre[correct_key] for correct_key in module_keys}
            data = progdbclient.Module(**res)
            try:
                api_instance = pdbch.get_module_api_instance()
                obj = api_instance.apimodule_create(data).to_dict()
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "update":
            if not args.input_file:
                eprint("Missing input file")
                exit(1)
            try:
                id = int(args.id)
            except TypeError as e:
                eprint("Incorrect or missing ID")
                exit(1)
            try:
                with open(args.input_file, "r") as f:
                    res_pre = yaml.safe_load(f)
            except (OSError, yaml.YAMLError) as e:
                eprint_exception(e, print_traceback=print_traceback)
                exit(1)
            module_keys = ["name", "human_description", "machine_description", "prog_language", "location", "sourcereplica_collection", "module"]
            res = {correct_key: res_pre[correct_key] for correct_key in module_keys}
            data = progdbclient.Module(**res)
            try:
                api_instance = pdbch.get_module_api_instance()
                obj = api_instance.apimodule_update(id, data).to_dict()
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "delete":
            try:
                id = int(args.id)
            except TypeError as e:
                eprint("Incorrect or missing ID")
                exit(1)
            try:
                api_instance = pdbch.get_module_api_instance()
                api_instance.apimodule_delete(id)
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        else:
            eprint("Not implemented for action: {}".format(args.action))
            exit(1)
    elif args.group == "source-replicas":
        if args.action == "list" or args.action == None:
            try:
                api_instance = pdbch.get_sourcereplica_api_instance()
                res = api_instance.apisourcereplica_list()
                if res:
                    obj = [i.to_dict() for i in res]
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "get":
            try:
                id = int(args.id)
            except TypeError as e:
                eprint("Incorrect or missing ID")
                exit(1)
            try:
                api_instance = pdbch.get_sourcereplica_api_instance()
                obj = api_instance.apisourcereplica_read(id).to_dict()
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "create":
            if not args.input_file:
                eprint("Missing input file")
                exit(1)
            try:
                with open(args.input_file, "r") as f:
                    res_pre = yaml.safe_load(f)
            except (OSError, yaml.YAMLError) as e:
                eprint_exception(e, print_traceback=print_traceback)
                exit(1)
            sourcereplica_keys = ["name", "human_description", "machine_description", "is_main", "module"]
            res = {correct_key: res_pre[correct_key] for correct_key in sourcereplica_keys}
            data = progdbclient.SourceReplica(**res)
            try:
                api_instance = pdbch.get_sourcereplica_api_instance()
                obj = api_instance.apisourcereplica_create(data).to_dict()
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "update":
            if not args.input_file:
                eprint("Missing input file")
                exit(1)
            try:
                id = int(args.id)
            except TypeError as e:
                eprint("Incorrect or missing ID")
                exit(1)
            try:
                with open(args.input_file, "r") as f:
                    res_pre = yaml.safe_load(f)
            except (OSError, yaml.YAMLError) as e:
                eprint_exception(e, print_traceback=print_traceback)
                exit(1)
            sourcereplica_keys = ["name", "human_description", "machine_description", "is_main", "module"]
            res = {correct_key: res_pre[correct_key] for correct_key in sourcereplica_keys}
            data = progdbclient.Package(**res)
            try:
                api_instance = pdbch.get_sourcereplica_api_instance()
                obj = api_instance.apisourcereplica_update(id, data).to_dict()
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "delete":
            try:
                id = int(args.id)
            except TypeError as e:
                eprint("Incorrect or missing ID")
                exit(1)
            try:
                api_instance = pdbch.get_sourcereplica_api_instance()
                api_instance.apisourcereplica_update(id)
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        else:
            eprint("Not implemented for action: {}".format(args.action))
            exit(1)
    elif args.group == "fs-objects":
        if args.action == "list" or args.action == None:
            try:
                api_instance = pdbch.get_fsobject_api_instance()
                res = api_instance.apifsobject_list()
                if res:
                    obj = [i.to_dict() for i in res]
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "get":
            try:
                id = int(args.id)
            except TypeError as e:
                eprint("Incorrect or missing ID")
                exit(1)
            try:
                api_instance = pdbch.get_fsobject_api_instance()
                obj = api_instance.apifsobject_read(id).to_dict()
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "create":
            if not args.input_file:
                eprint("Missing input file")
                exit(1)
            try:
                with open(args.input_file, "r") as f:
                    res_pre = yaml.safe_load(f)
            except (OSError, yaml.YAMLError) as e:
                eprint_exception(e, print_traceback=print_traceback)
                exit(1)
            fsobject_keys = ["name", "human_description", "machine_description", "location", "module", "replica"]
            res = {correct_key: res_pre[correct_key] for correct_key in fsobject_keys}
            data = progdbclient.FSObject(**res)
            try:
                api_instance = pdbch.get_fsobject_api_instance()
                obj = api_instance.apifsobject_create(data).to_dict()
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "update":
            if not args.input_file:
                eprint("Missing input file")
                exit(1)
            try:
                id = int(args.id)
            except TypeError as e:
                eprint("Incorrect or missing ID")
                exit(1)
            try:
                with open(args.input_file, "r") as f:
                    res_pre = yaml.safe_load(f)
            except (OSError, yaml.YAMLError) as e:
                eprint_exception(e, print_traceback=print_traceback)
                exit(1)
            fsobject_keys = ["name", "human_description", "machine_description", "location", "module", "replica"]
            res = {correct_key: res_pre[correct_key] for correct_key in fsobject_keys}
            data = progdbclient.FSObject(**res)
            try:
                api_instance = pdbch.get_fsobject_api_instance()
                obj = api_instance.apifsobject_update(id, data).to_dict()
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "delete":
            try:
                id = int(args.id)
            except TypeError as e:
                eprint("Incorrect or missing ID")
                exit(1)
            try:
                api_instance = pdbch.get_fsobject_api_instance()
                api_instance.apifsobject_delete(id)
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        else:
            eprint("Not implemented for action: {}".format(args.action))
            exit(1)
    else:
        eprint("Not implemented for group: {}".format(args.group))
        exit(1)
    if print_result:
        yaml.dump(obj, sys.stdout, default_flow_style=False, allow_unicode=True)


if __name__ == "__main__":
    main()