import os
import sys

import psutil

from monk.keras_prototype import prototype
from monk.compare_prototype import compare
from monk.pip_unit_tests.keras.common import print_start
from monk.pip_unit_tests.keras.common import print_status

import tensorflow as tf
if(tf.__version__[0] == '2'):
    import tensorflow.compat.v1 as tf
    tf.disable_v2_behavior()
import numpy as np


def test_block_inception_c(system_dict):
    forward = True;

    test = "test_block_inception_c";
    system_dict["total_tests"] += 1;
    print_start(test, system_dict["total_tests"])
    if(forward):
        try:
            gtf = prototype(verbose=0);
            gtf.Prototype("sample-project-1", "sample-experiment-1");


            network = [];
            network.append(gtf.inception_c_block(channels_7x7=3, pool_type="avg"));
            network.append(gtf.inception_c_block(channels_7x7=3, pool_type="max"));
            gtf.Compile_Network(network, data_shape=(1, 64, 64), use_gpu=False);

            x = tf.placeholder(tf.float32, shape=(1, 64, 64, 1))
            y = gtf.system_dict["local"]["model"](x);         

            system_dict["successful_tests"] += 1;
            print_status("Pass");

        except Exception as e:
            system_dict["failed_tests_exceptions"].append(e);
            system_dict["failed_tests_lists"].append(test);
            forward = False;
            print_status("Fail");
    else:
        system_dict["skipped_tests_lists"].append(test);
        print_status("Skipped");

    return system_dict
