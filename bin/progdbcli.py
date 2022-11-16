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
    epilog = '''\
available item-level cmds for bulk actions:
  c    create item
  u    update item
  d    delete item
  n    do nothing'''
    parent_parser = argparse.ArgumentParser(prog=self_name,
                                            description="Client for software database")
    subparsers = parent_parser.add_subparsers(help="Endpoint groups")
    subparsers.required = True
    subparsers.dest = "group"
    subparser_packages = subparsers.add_parser("packages", help="Utilities for work with Packages", formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)
    subparser_packages.add_argument("--action", type=str, help="Possible actions: list | create | get | update | delete | bulk-dump | bulk-upload")
    subparser_packages.add_argument("--profile", type=str, help="Config profile")
    subparser_packages.add_argument("--id", type=str, help="Entity ID")
    subparser_packages.add_argument("--input-file", type=str, help="Input file")
    subparser_packages.add_argument("--default-cmd", type=str, help="Default cmd for bulk actions")
    subparser_packagetags = subparsers.add_parser("packagetags", help="Utilities for work with PackageTags", formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)
    subparser_packagetags.add_argument("--action", type=str, help="Possible actions: list | create | get | update | delete | bulk-dump | bulk-upload")
    subparser_packagetags.add_argument("--profile", type=str, help="Config profile")
    subparser_packagetags.add_argument("--id", type=str, help="Entity ID")
    subparser_packagetags.add_argument("--input-file", type=str, help="Input file")
    subparser_packagetags.add_argument("--default-cmd", type=str, help="Default cmd for bulk actions")
    subparser_replicas = subparsers.add_parser("editions", help="Utilities for work with Replicas", formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)
    subparser_replicas.add_argument("--action", type=str, help="Possible actions: list | create | get | update | delete | bulk-dump | bulk-upload")
    subparser_replicas.add_argument("--profile", type=str, help="Config profile")
    subparser_replicas.add_argument("--id", type=str, help="Entity ID")
    subparser_replicas.add_argument("--input-file", type=str, help="Input file")
    subparser_replicas.add_argument("--default-cmd", type=str, help="Default cmd for bulk actions")
    subparser_modules = subparsers.add_parser("resources", help="Utilities for work with Modules", formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)
    subparser_modules.add_argument("--action", type=str, help="Possible actions: list | create | get | update | delete | bulk-dump | bulk-upload")
    subparser_modules.add_argument("--profile", type=str, help="Config profile")
    subparser_modules.add_argument("--id", type=str, help="Entity ID")
    subparser_modules.add_argument("--input-file", type=str, help="Input file")
    subparser_modules.add_argument("--default-cmd", type=str, help="Default cmd for bulk actions")
    return parent_parser.parse_args(sys.argv[1:])


def main():
    args = parse_args(sys.argv)
    pdbch = PDBCHelper(args)
    obj = None
    possible_cmds = ["c", "u", "d", "n"]
    if args.group == "packages":
        allowed_keys = list(progdbclient.Package.attribute_map.keys())
        while "id" in allowed_keys:
            allowed_keys.remove("id")
        if args.action == "list" or args.action == None:
            try:
                api_instance = pdbch.get_packages_api_instance()
                res = api_instance.apipackages_list()
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
                api_instance = pdbch.get_packages_api_instance()
                obj = api_instance.apipackages_read(id).to_dict()
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
            res = {correct_key: res_pre[correct_key] for correct_key in allowed_keys}
            data = progdbclient.Package(**res)
            try:
                api_instance = pdbch.get_packages_api_instance()
                obj = api_instance.apipackages_create(data).to_dict()
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
            res = {correct_key: res_pre[correct_key] for correct_key in allowed_keys}
            data = progdbclient.Package(**res)
            try:
                api_instance = pdbch.get_packages_api_instance()
                obj = api_instance.apipackages_update(id, data).to_dict()
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "delete":
            try:
                id = int(args.id)
            except TypeError as e:
                eprint("Incorrect or missing ID")
                exit(1)
            try:
                api_instance = pdbch.get_packages_api_instance()
                api_instance.apipackages_delete(id)
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "bulk-dump":
            default_cmd = ""
            if args.default_cmd not in possible_cmds + [None]:
                eprint("Unknown default cmd: {}, use one of the following {}".format(args.default_cmd, ", ".join(possible_cmds)))
                exit(1)
            if args.default_cmd is not None:
                default_cmd = args.default_cmd
            try:
                api_instance = pdbch.get_packages_api_instance()
                res = api_instance.apipackages_list()
                if res:
                    obj = []
                    for i in res:
                        new_item = i.to_dict()
                        new_item.update({"cmd": default_cmd})
                        obj.append(new_item)
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "bulk-upload":
            if not args.input_file:
                eprint("Missing input file")
                exit(1)
            default_cmd = ""
            if args.default_cmd not in possible_cmds + [None]:
                eprint("Unknown default cmd: {}, use one of the following {}".format(args.default_cmd, ", ".join(possible_cmds)))
                exit(1)
            if args.default_cmd is not None:
                default_cmd = args.default_cmd
            try:
                with open(args.input_file, "r") as f:
                    input_data = yaml.safe_load(f)
            except (OSError, yaml.YAMLError) as e:
                eprint_exception(e, print_traceback=print_traceback)
                exit(1)
            try:
                api_instance = pdbch.get_packages_api_instance()
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
            position = 1
            for i in input_data:
                if not isinstance(i, dict) or not "cmd" in i.keys() or not "id" in i.keys():
                    eprint("At position number {}: Input data element has unappropriated format".format(position))
                    continue
                if i["cmd"] not in possible_cmds + [""]:
                    eprint("At position number {}: Input data element contains an unknown command: {}".format(position, i["cmd"]))
                    continue
                cmd = i.pop("cmd")
                if cmd == "":
                    cmd = default_cmd
                if cmd == "c":
                    i_final = {correct_key: i[correct_key] for correct_key in allowed_keys}
                    data = progdbclient.Package(**i_final)
                    try:
                        api_instance.apipackages_create(data)
                    except ApiException as e:
                        eprint("At position number {}:".format(position))
                        eprint_exception(e, print_traceback=print_traceback)
                if cmd == "u":
                    id = i.pop("id")
                    i_final = {correct_key: i[correct_key] for correct_key in allowed_keys}
                    data = progdbclient.Package(**i_final)
                    try:
                        api_instance.apipackages_update(id, data)
                    except ApiException as e:
                        eprint("At position number {}:".format(position))
                        eprint_exception(e, print_traceback=print_traceback)
                if cmd == "d":
                    id = i.pop("id")
                    try:
                        api_instance.apipackages_delete(id)
                    except ApiException as e:
                        eprint_exception(e, print_traceback=print_traceback)
                position = position + 1
        else:
            eprint("Not implemented for action: {}".format(args.action))
            exit(1)
    elif args.group == "package-tags":
        allowed_keys = list(progdbclient.PackageTag.attribute_map.keys())
        while "id" in allowed_keys:
            allowed_keys.remove("id")
        if args.action == "list" or args.action == None:
            try:
                api_instance = pdbch.get_packagetags_api_instance()
                res = api_instance.apipackagetags_list()
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
                api_instance = pdbch.get_packagetags_api_instance()
                obj = api_instance.apipackagetags_read(id).to_dict()
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
            res = {correct_key: res_pre[correct_key] for correct_key in allowed_keys}
            data = progdbclient.PackageTag(**res)
            try:
                api_instance = pdbch.get_packagetags_api_instance()
                obj = api_instance.apipackagetags_create(data).to_dict()
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
            res = {correct_key: res_pre[correct_key] for correct_key in allowed_keys}
            data = progdbclient.PackageTag(**res)
            try:
                api_instance = pdbch.get_packagetags_api_instance()
                obj = api_instance.apipackagetags_update(id, data).to_dict()
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "delete":
            try:
                id = int(args.id)
            except TypeError as e:
                eprint("Incorrect or missing ID")
                exit(1)
            try:
                api_instance = pdbch.get_packagetags_api_instance()
                api_instance.apipackagetags_delete(id)
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "bulk-dump":
            default_cmd = ""
            if args.default_cmd not in possible_cmds + [None]:
                eprint("Unknown default cmd: {}, use one of the following {}".format(args.default_cmd, ", ".join(possible_cmds)))
                exit(1)
            if args.default_cmd is not None:
                default_cmd = args.default_cmd
            try:
                api_instance = pdbch.get_packagetags_api_instance()
                res = api_instance.apipackagetags_list()
                if res:
                    obj = []
                    for i in res:
                        new_item = i.to_dict()
                        new_item.update({"cmd": default_cmd})
                        obj.append(new_item)
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "bulk-upload":
            if not args.input_file:
                eprint("Missing input file")
                exit(1)
            default_cmd = ""
            if args.default_cmd not in possible_cmds + [None]:
                eprint("Unknown default cmd: {}, use one of the following {}".format(args.default_cmd, ", ".join(possible_cmds)))
                exit(1)
            if args.default_cmd is not None:
                default_cmd = args.default_cmd
            try:
                with open(args.input_file, "r") as f:
                    input_data = yaml.safe_load(f)
            except (OSError, yaml.YAMLError) as e:
                eprint_exception(e, print_traceback=print_traceback)
                exit(1)
            try:
                api_instance = pdbch.get_packagetags_api_instance()
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
            position = 1
            for i in input_data:
                if not isinstance(i, dict) or not "cmd" in i.keys() or not "id" in i.keys():
                    eprint("At position number {}: Input data element has unappropriated format".format(position))
                    continue
                if i["cmd"] not in possible_cmds + [""]:
                    eprint("At position number {}: Input data element contains an unknown command: {}".format(position, i["cmd"]))
                    continue
                cmd = i.pop("cmd")
                if cmd == "":
                    cmd = default_cmd
                if cmd == "c":
                    i_final = {correct_key: i[correct_key] for correct_key in allowed_keys}
                    data = progdbclient.PackageTag(**i_final)
                    try:
                        api_instance.apipackagetags_create(data)
                    except ApiException as e:
                        eprint("At position number {}:".format(position))
                        eprint_exception(e, print_traceback=print_traceback)
                if cmd == "u":
                    id = i.pop("id")
                    i_final = {correct_key: i[correct_key] for correct_key in allowed_keys}
                    data = progdbclient.PackageTag(**i_final)
                    try:
                        api_instance.apipackagetags_update(id, data)
                    except ApiException as e:
                        eprint("At position number {}:".format(position))
                        eprint_exception(e, print_traceback=print_traceback)
                if cmd == "d":
                    id = i.pop("id")
                    try:
                        api_instance.apipackagetags_delete(id)
                    except ApiException as e:
                        eprint_exception(e, print_traceback=print_traceback)
                position = position + 1
        else:
            eprint("Not implemented for action: {}".format(args.action))
            exit(1)
    elif args.group == "editions":
        allowed_keys = list(progdbclient.Edition.attribute_map.keys())
        while "id" in allowed_keys:
            allowed_keys.remove("id")
        if args.action == "list" or args.action == None:
            try:
                api_instance = pdbch.get_editions_api_instance()
                res = api_instance.apieditions_list()
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
                api_instance = pdbch.get_editions_api_instance()
                obj = api_instance.apieditions_read(id).to_dict()
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
            res = {correct_key: res_pre[correct_key] for correct_key in allowed_keys}
            data = progdbclient.Edition(**res)
            try:
                api_instance = pdbch.get_editions_api_instance()
                obj = api_instance.apieditions_create(data).to_dict()
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
            res = {correct_key: res_pre[correct_key] for correct_key in allowed_keys}
            data = progdbclient.Edition(**res)
            try:
                api_instance = pdbch.get_editions_api_instance()
                obj = api_instance.apieditions_update(id, data).to_dict()
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "delete":
            try:
                id = int(args.id)
            except TypeError:
                eprint("Incorrect or missing ID")
                exit(1)
            try:
                api_instance = pdbch.get_editions_api_instance()
                api_instance.apieditions_delete(id)
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "bulk-dump":
            default_cmd = ""
            if args.default_cmd not in possible_cmds + [None]:
                eprint("Unknown default cmd: {}, use one of the following {}".format(args.default_cmd, ", ".join(possible_cmds)))
                exit(1)
            if args.default_cmd is not None:
                default_cmd = args.default_cmd
            try:
                api_instance = pdbch.get_editions_api_instance()
                res = api_instance.apieditions_list()
                if res:
                    obj = []
                    for i in res:
                        new_item = i.to_dict()
                        new_item.update({"cmd": default_cmd})
                        obj.append(new_item)
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "bulk-upload":
            if not args.input_file:
                eprint("Missing input file")
                exit(1)
            default_cmd = ""
            if args.default_cmd not in possible_cmds + [None]:
                eprint("Unknown default cmd: {}, use one of the following {}".format(args.default_cmd, ", ".join(possible_cmds)))
                exit(1)
            if args.default_cmd is not None:
                default_cmd = args.default_cmd
            try:
                with open(args.input_file, "r") as f:
                    input_data = yaml.safe_load(f)
            except (OSError, yaml.YAMLError) as e:
                eprint_exception(e, print_traceback=print_traceback)
                exit(1)
            try:
                api_instance = pdbch.get_editions_api_instance()
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
            position = 1
            for i in input_data:
                if not isinstance(i, dict) or not "cmd" in i.keys() or not "id" in i.keys():
                    eprint("At position number {}: Input data element has unappropriated format".format(position))
                    continue
                if i["cmd"] not in possible_cmds + [""]:
                    eprint("At position number {}: Input data element contains an unknown command: {}".format(position, i["cmd"]))
                    continue
                cmd = i.pop("cmd")
                if cmd == "":
                    cmd = default_cmd
                if cmd == "c":
                    i_final = {correct_key: i[correct_key] for correct_key in allowed_keys}
                    data = progdbclient.Edition(**i_final)
                    try:
                        api_instance.apieditions_create(data)
                    except ApiException as e:
                        eprint("At position number {}:".format(position))
                        eprint_exception(e, print_traceback=print_traceback)
                if cmd == "u":
                    id = i.pop("id")
                    i_final = {correct_key: i[correct_key] for correct_key in allowed_keys}
                    data = progdbclient.Edition(**i_final)
                    try:
                        api_instance.apieditions_update(id, data)
                    except ApiException as e:
                        eprint("At position number {}:".format(position))
                        eprint_exception(e, print_traceback=print_traceback)
                if cmd == "d":
                    id = i.pop("id")
                    try:
                        api_instance.apieditions_delete(id)
                    except ApiException as e:
                        eprint_exception(e, print_traceback=print_traceback)
                position = position + 1
        else:
            eprint("Not implemented for action: {}".format(args.action))
            exit(1)
    elif args.group == "resources":
        allowed_keys = list(progdbclient.Resource.attribute_map.keys())
        while "id" in allowed_keys:
            allowed_keys.remove("id")
        if args.action == "list" or args.action == None:
            try:
                api_instance = pdbch.get_resources_api_instance()
                res = api_instance.apiresources_list()
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
                api_instance = pdbch.get_resources_api_instance()
                obj = api_instance.apiresources_read(id).to_dict()
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
            res = {correct_key: res_pre[correct_key] for correct_key in allowed_keys}
            data = progdbclient.Resource(**res)
            try:
                api_instance = pdbch.get_resources_api_instance()
                obj = api_instance.apiresources_create(data).to_dict()
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
            res = {correct_key: res_pre[correct_key] for correct_key in allowed_keys}
            data = progdbclient.Resource(**res)
            try:
                api_instance = pdbch.get_resources_api_instance()
                obj = api_instance.apiresources_update(id, data).to_dict()
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "delete":
            try:
                id = int(args.id)
            except TypeError as e:
                eprint("Incorrect or missing ID")
                exit(1)
            try:
                api_instance = pdbch.get_resources_api_instance()
                api_instance.apiresources_delete(id)
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "bulk-dump":
            default_cmd = ""
            if args.default_cmd not in possible_cmds + [None]:
                eprint("Unknown default cmd: {}, use one of the following {}".format(args.default_cmd, ", ".join(possible_cmds)))
                exit(1)
            if args.default_cmd is not None:
                default_cmd = args.default_cmd
            try:
                api_instance = pdbch.get_resources_api_instance()
                res = api_instance.apiresources_list()
                if res:
                    obj = []
                    for i in res:
                        new_item = i.to_dict()
                        new_item.update({"cmd": default_cmd})
                        obj.append(new_item)
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "bulk-upload":
            if not args.input_file:
                eprint("Missing input file")
                exit(1)
            default_cmd = ""
            if args.default_cmd not in possible_cmds + [None]:
                eprint("Unknown default cmd: {}, use one of the following {}".format(args.default_cmd, ", ".join(possible_cmds)))
                exit(1)
            if args.default_cmd is not None:
                default_cmd = args.default_cmd
            try:
                with open(args.input_file, "r") as f:
                    input_data = yaml.safe_load(f)
            except (OSError, yaml.YAMLError) as e:
                eprint_exception(e, print_traceback=print_traceback)
                exit(1)
            try:
                api_instance = pdbch.get_resources_api_instance()
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
            position = 1
            for i in input_data:
                if not isinstance(i, dict) or not "cmd" in i.keys() or not "id" in i.keys():
                    eprint("At position number {}: Input data element has unappropriated format".format(position))
                    continue
                if i["cmd"] not in possible_cmds + [""]:
                    eprint("At position number {}: Input data element contains an unknown command: {}".format(position, i["cmd"]))
                    continue
                cmd = i.pop("cmd")
                if cmd == "":
                    cmd = default_cmd
                if cmd == "c":
                    i_final = {correct_key: i[correct_key] for correct_key in allowed_keys}
                    data = progdbclient.Resource(**i_final)
                    try:
                        api_instance.apiresources_create(data)
                    except ApiException as e:
                        eprint("At position number {}:".format(position))
                        eprint_exception(e, print_traceback=print_traceback)
                if cmd == "u":
                    id = i.pop("id")
                    i_final = {correct_key: i[correct_key] for correct_key in allowed_keys}
                    data = progdbclient.Resource(**i_final)
                    try:
                        api_instance.apiresources_update(id, data)
                    except ApiException as e:
                        eprint("At position number {}:".format(position))
                        eprint_exception(e, print_traceback=print_traceback)
                if cmd == "d":
                    id = i.pop("id")
                    try:
                        api_instance.apiresources_delete(id)
                    except ApiException as e:
                        eprint_exception(e, print_traceback=print_traceback)
                position = position + 1
        else:
            eprint("Not implemented for action: {}".format(args.action))
            exit(1)
    else:
        eprint("Not implemented for group: {}".format(args.group))
        exit(1)
    if print_result and obj is not None:
        yaml.dump(obj, sys.stdout, default_flow_style=False, allow_unicode=True)


if __name__ == "__main__":
    main()