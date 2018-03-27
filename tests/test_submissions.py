import os
import json
from glob import glob
from datetime import datetime
from itertools import chain
from collections import defaultdict

import pytest
import pandas as pd


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


@pytest.mark.parametrize(
    "path",
    files['train'],
    ids=[os.path.split(path)[1] for path in files['train']]
)
def test_train_file_has_required_fields(path):
    with open(path) as json_file:
        record = json.load(json_file)

    required_fields = [
        'version', 'author', 'authorEmail', 'framework',
        'model', 'hardware', 'timestamp'
    ]

    for field in required_fields:
        assert field in record, "{} is a required field".format(field)

    # Enforce timestamp format
    datetime.strptime(record['timestamp'], '%Y-%m-%d')


@pytest.mark.parametrize(
    "path",
    files['infer'],
    ids=[os.path.split(path)[1] for path in files['infer']]
)
def test_infer_file_has_required_fields(path):
    with open(path) as json_file:
        record = json.load(json_file)

    required_fields = [
        'version', 'author', 'authorEmail', 'framework',
        'model', 'hardware', 'timestamp', 'latency'
    ]

    for field in required_fields:
        assert field in record, "{} is a required field".format(field)

    # Enforce timestamp format
    datetime.strptime(record['timestamp'], '%Y-%m-%d')


@pytest.mark.parametrize(
    "path",
    files['CIFAR10']['train'],
    ids=[os.path.split(path)[1] for path in files['CIFAR10']['train']]
)
def test_cifar10_train_file_has_valid_tsv(path):
    data_path = os.path.splitext(path)[0] + '.tsv'
    assert os.path.exists(data_path), "The TSV file doesn't exist"

    df = pd.read_csv(data_path, sep='\t')
    required_columns = ['epoch', 'hours', 'top1Accuracy']
    assert sorted(df.columns) == sorted(required_columns), "Incorrect columns"

    assert len(df) > 0, "The TSV file shouldn't be empty"


@pytest.mark.parametrize(
    "path",
    files['ImageNet']['train'],
    ids=[os.path.split(path)[1] for path in files['ImageNet']['train']]
)
def test_imagenet_train_file_has_valid_tsv(path):
    data_path = os.path.splitext(path)[0] + '.tsv'
    assert os.path.exists(data_path), "The TSV file doesn't exist"

    df = pd.read_csv(data_path, sep='\t')
    required_columns = ['epoch', 'hours', 'top1Accuracy', 'top5Accuracy']
    assert sorted(df.columns) == sorted(required_columns), "Incorrect columns"

    assert len(df) > 0, "The TSV file shouldn't be empty"


@pytest.mark.parametrize(
    "path",
    files['SQuAD']['train'],
    ids=[os.path.split(path)[1] for path in files['SQuAD']['train']]
)
def test_squad_train_file_has_valid_tsv(path):
    data_path = os.path.splitext(path)[0] + '.tsv'
    assert os.path.exists(data_path), "The TSV file doesn't exist"

    df = pd.read_csv(data_path, sep='\t')
    required_columns = ['epoch', 'hours', 'f1Score']
    assert sorted(df.columns) == sorted(required_columns)
