import os
import json
from glob import glob
from itertools import chain
from collections import defaultdict

import pytest


DATASETS = ['CIFAR10', 'ImageNet', 'SQuAD']

files = defaultdict(dict)
for dataset in DATASETS:
    files[dataset]['train'] = glob('{}/train/*.json'.format(dataset))
    files[dataset]['infer'] = glob('{}/inference/*.json'.format(dataset))

files['train'] = chain.from_iterable(files[d]['train'] for d in DATASETS)
files['train'] = list(files['train'])
files['infer'] = chain.from_iterable(files[d]['infer'] for d in DATASETS)
files['infer'] = list(files['infer'])


@pytest.mark.parametrize(
    "path",
    files['train'],
    ids=[os.path.split(path)[1] for path in files['train']]
)
def test_train_file_is_valid_json(path):
    with open(path) as json_file:
        json.load(json_file)


@pytest.mark.parametrize(
    "path",
    files['infer'],
    ids=[os.path.split(path)[1] for path in files['infer']]
)
def test_infer_file_is_valid_json(path):
    with open(path) as json_file:
        json.load(json_file)
