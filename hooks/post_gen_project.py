#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import json
import os
import shutil

import yaml

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(filepath: str) -> None:
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir_if_empty(filepath: str) -> None:
    if len(os.listdir(filepath)) == 0:
        remove_dir(filepath)


if __name__ == "__main__":

    with open(".cookiecutter.yaml", "w") as f:
        context = r"""
        {{ cookiecutter | jsonify }}
        """
        config = json.loads(context)
        del_keys = []
        for key in config:
            if key.startswith("_"):
                del_keys.append(key)
        for key in del_keys:
            del config[key]
        default_config = {
            "default_context": config,
        }
        yaml.dump(default_config, f, encoding='utf-8', allow_unicode=True)
