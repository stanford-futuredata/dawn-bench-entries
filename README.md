# DAWNBench Submission Instructions

Thank you for the interest in DAWNBench!

To add your model to our leaderboard, open a Pull Request with title `<Model name> || <Task name> || <Author name>`
([example PR](https://github.com/stanford-futuredata/dawn-bench-entries/pull/1)), with JSON
(and TSV where applicable) result files in the format outlined below.  

## Tasks

  * [CIFAR10 Training](#cifar10-training)
  * [CIFAR10 Inference](#cifar10-inference)
  * [ImageNet Training](#imagenet-training)
  * [ImageNet Inference](#imagenet-inference)
  * [SQuAD Training](#squad-training)
  * [SQuAD Inference](#squad-inference)
  
## CIFAR10 Training

### Task Description

We evaluate image classification performance on the [CIFAR10 dataset](https://www.cs.toronto.edu/~kriz/cifar.html).

For training, we have two metrics:
- **Training Time:** Train an image classification model for the CIFAR10 dataset. Report the time needed to train
  a model with test set accuracy of at least 94%
- **Cost:** On public cloud infrastructure, compute the total time needed to reach a test set accuracy of
  94% or greater, as outlined above. Multiply the time taken (in hours) by the cost of the instance per hour, to obtain the
  total cost of training the model

Including cost is optional and will only be calculated if the `costPerHour` field is included in the JSON file.
Submissions that only aim for time aren't restricted to public cloud infrastructure.

### JSON Format

Results for the CIFAR10 training tasks can be reported using a JSON file with the following fields,

- `version`: DAWNBench competition version (currently v1.0)
- `author`: Author name
- `authorEmail`: Author email
- `framework`: Framework on which training / inference was performed
- `codeURL`: [Optional] URL pointing to code for model
- `model`: Model name
- `hardware`: A short description of the hardware on which model training was performed. If relevant,
  please specify Cloud provider and instance type to make results more reproducible
- `costPerHour`: [Optional] Reported in USD ($). Cost of instance per hour
- `timestamp`: Date of submission in format `yyyy-mm-dd`
- `logFilename`: [Optional] URL pointing to training logs
- `misc`: [Optional] JSON object of other miscellaneous notes, such as learning rate schedule, optimization algorithm,
  framework version, etc.

In addition, report training progress at the end of every epoch in a TSV with the following format,

```epoch\thours\ttop1Accuracy```

We will compute time to reach a test set accuracy of 94% by reading off the first entry in the above TSV
with a top-1 test set accuracy of at least 94%.

JSON and TSV files are named `[author name]_[model name]_[hardware tag]_[framework].json`, similar to
`dawn_resnet56_1k80-gc_tensorflow.[json|tsv]`. Put the JSON and TSV files in the `CIFAR10/train/` sub-directory.
  
### Example JSON and TSV


#### JSON

```JSON
{
    "version": "v1.0",
    "author": "Stanford DAWN",
    "authorEmail": "dawn-bench@cs.stanford.edu",
    "framework": "TensorFlow",
    "codeURL": "https://github.com/stanford-futuredata/dawn-benchmark/tree/master/tensorflow",
    "model": "ResNet 56",
    "hardware": "1 K80 / 30 GB / 8 CPU (Google Cloud)",
    "costPerHour": 0.90,
    "timestamp": "2017-08-14",
    "misc": {}
}
```

#### TSV

```TSV
epoch   hours top1Accuracy
1       0.07166666666666667     33.57
2       0.1461111111111111      52.51
3       0.21805555555555556     61.71
4       0.2902777777777778      69.46
5       0.3622222222222222      71.47
6       0.43416666666666665     69.64
7       0.5061111111111111      75.81
```

<br/>

## CIFAR10 Inference

### Task Description

We evaluate image classification performance on the [CIFAR10 dataset](https://www.cs.toronto.edu/~kriz/cifar.html).

For inference, we have two metrics:
- **Latency:** Use a model that has a test set accuracy of 94% or greater. Measure the total time needed to classify
  all 10,000 images in the CIFAR10 test set _one-at-a-time_, and then divide by 10,000
- **Cost:** Use a model that has a test set accuracy of 94% or greater. Measure the average per-image latency
  in the CIFAR10 test set, and then multiply by the cost of the instance per unit time

### JSON Format

Results for the CIFAR10 inference tasks can be reported using a JSON file with the following fields,

- `version`: DAWNBench competition version (currently v1.0)
- `author`: Author name
- `authorEmail`: Author email
- `framework`: Framework on which training / inference was performed
- `codeURL`: [Optional] URL pointing to code for model
- `model`: Model name
- `hardware`: A short description of the hardware on which model inference was performed. If relevant,
  please specify Cloud provider and instance type to make results more reproducible
- `latency`: Reported in milliseconds. Time needed to classify one image
- `cost`: Reported in USD ($). Cost of performing inference on a single image. Computed as `costPerHour * latency`
- `top1Accuracy`: Reported in percentage points from 0 to 100. Accuracy of model on CIFAR10 test dataset.
- `timestamp`: Date of submission in format `yyyy-mm-dd`
- `logFilename`: [Optional] URL pointing to training / inference logs
- `misc`: [Optional] JSON object of other miscellaneous notes, such as batch size, framework version,
  etc.
  
Note that it is only necessary to specify _one_ of the `latency` and `cost` fields outlined
above. However, it is encouraged to specify both (if available) in a single JSON result file.

JSON files are named `[author name]_[model name]_[hardware tag]_[framework].json`, similar to
`dawn_resnet56_1k80-gc_tensorflow.json`. Put the JSON file in the `CIFAR10/inference/` sub-directory.

### Example JSON

```JSON
{
    "version": "v1.0",
    "author": "Stanford DAWN",
    "authorEmail": "dawn-bench@cs.stanford.edu",
    "framework": "TensorFlow",
    "codeURL": "https://github.com/stanford-futuredata/dawn-benchmark/tree/master/tensorflow",
    "model": "ResNet 56",
    "hardware": "1 K80 / 30 GB / 8 CPU (Google Cloud)",
    "latency": 43.45,
    "cost": 1e-6,
    "accuracy": 94.45,
    "timestamp": "2017-08-14",
    "misc": {}
}
```

<br/>

## ImageNet Training

### Task Description

We evaluate image classification performance on the [ImageNet dataset](http://www.image-net.org/challenges/LSVRC/2012/).

For training, we have two metrics:
- **Training Time:** Train an image classification model for the ImageNet dataset. Report the time needed to train
  a model with top-5 validation accuracy of at least 93%
- **Cost:** On public cloud infrastructure, compute the total time needed to reach a validation accuracy of
  93% or greater, as outlined above. Multiply the time taken by the cost of the instance per hour, to obtain the
  total cost of training the model

Including cost is optional and will only be calculated if the `costPerHour` field is included in the JSON file.
Submissions that only aim for time aren't restricted to public cloud infrastructure.

### JSON Format

Results for the ImageNet training tasks can be reported using a JSON file with the following fields,

- `version`: DAWNBench competition version (currently v1.0)
- `author`: Author name
- `authorEmail`: Author email
- `framework`: Framework on which training / inference was performed
- `codeURL`: [Optional] URL pointing to code for model
- `model`: Model name
- `hardware`: A short description of the hardware on which model training was performed. If relevant,
  please specify Cloud provider and instance type to make results more reproducible
- `costPerHour`: [Optional] Reported in USD ($). Cost of instance per hour
- `timestamp`: Date of submission in format `yyyy-mm-dd`
- `logFilename`: [Optional] URL pointing to training logs
- `misc`: [Optional] JSON object of other miscellaneous notes, such as learning rate schedule, optimization algorithm,
  framework version, etc.
  
In addition, report training progress at the end of every epoch in a TSV with the following format,

```epoch\thours\ttop1Accuracy\ttop5Accuracy```

We will compute time to reach a top-5 validation accuracy of 93% by reading off the first entry in the above TSV
with a top-5 validation accuracy of at least 93%.

JSON and TSV files are named `[author name]_[model name]_[hardware tag]_[framework].json`, similar to
`dawn_resnet56_1k80-gc_tensorflow.[json|tsv]`. Put the JSON and TSV files in the `ImageNet/train/` sub-directory.
  
### Example JSON and TSV

#### JSON

```JSON
{
    "version": "v1.0",
    "author": "Stanford DAWN",
    "authorEmail": "dawn-bench@cs.stanford.edu",
    "framework": "TensorFlow",
    "codeURL": "https://github.com/stanford-futuredata/dawn-benchmark/tree/master/tensorflow",
    "model": "ResNet 50",
    "hardware": "1 K80 / 30 GB / 8 CPU (Google Cloud)",
    "costPerHour": 0.90,
    "timestamp": "2017-08-14",
    "misc": {}
}
```

#### TSV

```TSV
epoch   hours top1Accuracy top5Accuracy
1       0.07166666666666667     33.57     68.93
2       0.1461111111111111      52.51     72.48 
3       0.21805555555555556     61.71     81.46
4       0.2902777777777778      69.46     81.92
5       0.3622222222222222      71.47     82.17 
6       0.43416666666666665     69.64     83.68
7       0.5061111111111111      75.81     84.31 
```

<br/>

## ImageNet Inference

### Task Description

We evaluate image classification performance on the [ImageNet dataset](http://www.image-net.org/challenges/LSVRC/2012/).

For inference, we have two metrics:
- **Latency:** Use a model that has a top-5 validation accuracy of 93% or greater. Measure the total time needed to classify
  all 50,000 images in the ImageNet validation set _one-at-a-time_, and then divide by 50,000
- **Cost:** Use a model that has a top-5 validation accuracy of 93% or greater. Measure the average latency of performing
  inference on a single image (as described above), then multiply by cost of the instance per hour to get total time to
  perform inference

### JSON Format

Results for the ImageNet inference tasks can be reported using a JSON file with the following fields,

- `version`: DAWNBench competition version (currently v1.0)
- `author`: Author name
- `authorEmail`: Author email
- `framework`: Framework on which training / inference was performed
- `codeURL`: [Optional] URL pointing to code for model
- `model`: Model name
- `hardware`: A short description of the hardware on which model inference was performed. If relevant,
  please specify Cloud provider and instance type to make results more reproducible
- `latency`: Reported in milliseconds. Time needed to classify one image
- `cost`: Reported in USD ($). Cost of performing inference on a single image. Computed as `costPerHour * latency`
- `top5Accuracy`: Reported in percentage points from 0 to 100. Accuracy of model on ImageNet test dataset.
- `timestamp`: Date of submission in format `yyyy-mm-dd`
- `logFilename`: [Optional] URL pointing to training / inference logs
- `misc`: [Optional] JSON object of other miscellaneous notes, such as batch size, framework version,
  etc.
  
Note that it is only necessary to specify _one_ of the `latency` and `cost` fields outlined
above. However, it is encouraged to specify both (if available) in a single JSON result file.

JSON files are named `[author name]_[model name]_[hardware tag]_[framework].json`, similar to
`dawn_resnet56_1k80-gc_tensorflow.json`. Put the JSON file in the `ImageNet/inference/` sub-directory.

### Example JSON

```JSON
{
    "version": "v1.0",
    "author": "Stanford DAWN",
    "authorEmail": "dawn-bench@cs.stanford.edu",
    "framework": "TensorFlow",
    "codeURL": "https://github.com/stanford-futuredata/dawn-benchmark/tree/master/tensorflow",
    "model": "ResNet 50",
    "hardware": "1 K80 / 30 GB / 8 CPU (Google Cloud)",
    "latency": 43.45,
    "cost": 4.27e-6,
    "top5Accuracy": 93.45,
    "timestamp": "2017-08-14",
    "misc": {}
}
```

<br/>


## SQuAD Training

### Task Description

We evaluate question answering performance on the [SQuAD dataset](https://rajpurkar.github.io/SQuAD-explorer/).

For training, we have two metrics:
- **Training Time:** Train a question answering model for the SQuAD dataset. Report the time needed to train
  a model with a dev set F1 score of at least 0.73
- **Cost:** On public cloud infrastructure, compute the total time needed to reach a dev set F1 score of 0.73
  or greater, as outlined above. Multiply the time taken by the cost of the instance per hour, to obtain the
  total cost of training the model

Including cost is optional and will only be calculated if the `costPerHour` field is included in the JSON file.
Submissions that only aim for time aren't restricted to public cloud infrastructure.

### JSON Format

Results for the SQuAD training tasks can be reported using a JSON file with the following fields,

- `version`: DAWNBench competition version (currently v1.0)
- `author`: Author name
- `authorEmail`: Author email
- `framework`: Framework on which training / inference was performed
- `codeURL`: [Optional] URL pointing to code for model
- `model`: Model name
- `hardware`: A short description of the hardware on which model training was performed. If relevant,
  please specify Cloud provider and instance type to make results more reproducible
- `costPerHour`: [Optional] Reported in USD ($). Cost of instance per hour
- `timestamp`: Date of submission in format `yyyy-mm-dd`
- `logFilename`: [Optional] URL pointing to training / inference logs
- `misc`: [Optional] JSON object of other miscellaneous notes, such as learning rate schedule, optimization algorithm,
  framework version, etc.

In addition, report training progress at the end of every epoch in a TSV with the following format,

```epoch\thours\tf1Score```

We will compute time to reach a F1 score of 0.73 by reading off the first entry in the above TSV
with a F1 score of at least 0.73.

JSON and TSV files are named `[author name]_[model name]_[hardware tag]_[framework].json`, similar to
`dawn_bidaf_1k80-gc_tensorflow.[json|tsv]`. Put the JSON and TSV files in the `SQuAD/train/` sub-directory.

### Example JSON and TSV

#### JSON

```JSON
{
    "version": "v1.0",
    "author": "Stanford DAWN",
    "authorEmail": "dawn-bench@cs.stanford.edu",
    "framework": "TensorFlow",
    "codeURL": "https://github.com/stanford-futuredata/dawn-benchmark/tree/master/tensorflow_qa/bi-att-flow",
    "model": "BiDAF",
    "hardware": "1 K80 / 30 GB / 8 CPU (Google Cloud)",
    "costPerHour": 0.90,
    "timestamp": "2017-08-14",
    "misc": {}
}
```

#### TSV

```TSV
epoch   hours f1Score
1     0.7638888888888888      0.5369029640999999
2     1.5238381055555557      0.6606892943
3     2.2855751       0.700419426
4     3.0448481305555557      0.7229908705
5     3.806446388888889       0.731013
6     4.5750864       0.7370445132
7     5.346703258333334       0.7413719296
```

<br/>

## SQuAD Inference

### Task Description

We evaluate question answering performance on the [SQuAD dataset](https://rajpurkar.github.io/SQuAD-explorer/).

For inference, we have two metrics:
- **Latency:** Use a model that has a dev set F1 measure of 0.73 or greater. Measure the total time needed to answer
  all questions in the SQuAD dev set _one-at-a-time_, and then divide by the number of questions
- **Cost:** Use a model that has a dev set F1 measure of 0.73 or greater. Measure the average latency needed to
  perform inference on a single question, and then multiply by the cost of the instance

### JSON Format

Results for the SQuAD inference tasks can be reported using a JSON file with the following fields,

- `version`: DAWNBench competition version (currently v1.0)
- `author`: Author name
- `authorEmail`: Author email
- `framework`: Framework on which training / inference was performed
- `codeURL`: [Optional] URL pointing to code for model
- `model`: Model name
- `hardware`: A short description of the hardware on which model inference was performed. If relevant,
  please specify Cloud provider and instance type to make results more reproducible
- `latency`: Reported in milliseconds. Time needed to answer one question
- `cost`: Reported in USD ($). Cost of performing inference on a single question. Computed as `costPerHour * latency`
- `f1Score`: Reported in fraction from 0.0 to 1.0. F1 score of model on SQuAD development dataset
- `timestamp`: Date of submission in format `yyyy-mm-dd`
- `logFilename`: [Optional] URL pointing to training / inference logs
- `misc`: [Optional] JSON object of other miscellaneous notes, such as batch size, framework version,
  etc.

Note that it is only necessary to specify _one_ of the `latency` and `cost` fields outlined
above. However, it is encouraged to specify both (if available) in a single JSON result file.

JSON files are named `[author name]_[model name]_[hardware tag]_[framework].json`, similar to
`dawn_bidaf_1k80-gc_tensorflow.json`. Put the JSON file `SQuAD/inference/` sub-directory.

### Example JSON

```JSON
{
    "version": "v1.0",
    "author": "Stanford DAWN",
    "authorEmail": "dawn-bench@cs.stanford.edu",
    "framework": "TensorFlow",
    "codeURL": "https://github.com/stanford-futuredata/dawn-benchmark/tree/master/tensorflow_qa/bi-att-flow",
    "model": "BiDAF",
    "hardware": "1 K80 / 30 GB / 8 CPU (Google Cloud)",
    "latency": 590.0,
    "cost": 2e-6,
    "f1Score": 0.7524165510999999,
    "timestamp": "2017-08-14",
    "misc": {}
}
```

## FAQ
- **Can spot instances be used for cost metrics?** For submissions including cost, please use on-demand, i.e., non-preemptible, instance pricing. Spot pricing is too volatile for the current release the benchmark. We're open to suggestions on better ways to deal with pricing volatility, so if you have ideas, please pitch them on the [google group](https://groups.google.com/forum/#!forum/dawn-bench-community)
- **Is validation time included in training time?** No, you don't need to include the time required to calculate validation accuracy and save checkpoints.
-**What happens after I submit a pull request with a new result?** After you submit a PR, unit tests should automatically run to determine basic requirements. Assuming the unit tests pass, we review the code and the submission. If it is sufficiently similar to existing results or the difference is easily justified, we accept the submission without reproducing. If there issues with the code or someone questions the results, the process is a little more complicated and can vary from situation to situation. If the issues are small, it may be as simple as changing the JSON file.

*Disclosure: The Stanford DAWN research project is a five-year industrial affiliates program at Stanford University and is financially supported in part by founding members including Intel, Microsoft, NEC, Teradata, VMWare, and Google. For more information, including information regarding Stanford’s policies on openness in research and policies affecting industrial affiliates program membership, please see [DAWN's membership page](http://dawn.cs.stanford.edu/members/).*
