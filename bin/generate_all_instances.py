import json
import math
import os
import sys
import unittest

import pandas as pd

import bischoff_and_ratcliff_1995 as br95

OUTPUT_FILE_PATH_JSON = "instances.json"

# input parameters
NUMBER_OF_INSTANCES_PER_BOX_TYPE = 100
CONTAINER_DIMENSIONS = {
    "length": 587,
    "width": 233,
    "height": 220,
}  # the dimensions in cm of a 20 ft ISO container in 1995.
NUMBER_OF_DIFFERENT_BOX_TYPES_LIST = [3, 5, 8, 10, 12, 15, 20] # n
BOX_DIMENSION_LOWER_LIMITS = [30, 25, 20]  # a_j, \forall j \in \{1, 2, 3\}
BOX_DIMENSION_UPPER_LIMITS = [120, 100, 80]  # b_j, \forall j \in \{1, 2, 3\}
BOX_STABILITY_LIMIT = 2  # L
random_seed_generator = lambda p: 2502505 + 100 * (p - 1)

out = {f"set_{instance_set_number+1}": [] for instance_set_number in range(len(NUMBER_OF_DIFFERENT_BOX_TYPES_LIST))}
for instance_number in range(1, NUMBER_OF_INSTANCES_PER_BOX_TYPE + 1):
    for instance_set_number, number_of_different_box_types in enumerate(NUMBER_OF_DIFFERENT_BOX_TYPES_LIST):
        instance = br95.Instance(
            C=CONTAINER_DIMENSIONS,
            n=number_of_different_box_types,
            a=BOX_DIMENSION_LOWER_LIMITS,
            b=BOX_DIMENSION_UPPER_LIMITS,
            L=BOX_STABILITY_LIMIT,
            s=random_seed_generator(instance_number)
        )
        out[f"set_{instance_set_number+1}"].append(instance.to_dict())

with open(OUTPUT_FILE_PATH_JSON, "w") as file:
    json.dump(out, file, indent=2)
