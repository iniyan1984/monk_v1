import os
import sys
sys.path.append("../../../../monk_v1/");
sys.path.append("../../../monk/");
import psutil

from keras_prototype import prototype
from compare_prototype import compare
from common import print_start
from common import print_status

import tensorflow as tf
if(tf.__version__[0] == '2'):
    import tensorflow.compat.v1 as tf
    tf.enable_v2_behavior()


def test_optimizer_rmsprop(system_dict):
    forward = True;
    if(not os.path.isdir("datasets")):
        os.system("! wget --load-cookies /tmp/cookies.txt \"https://docs.google.com/uc?export=download&confirm=$(wget --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1rG-U1mS8hDU7_wM56a1kc-li_zHLtbq2' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1rG-U1mS8hDU7_wM56a1kc-li_zHLtbq2\" -O datasets.zip && rm -rf /tmp/cookies.txt")
        os.system("! unzip -qq datasets.zip")

    test = "test_optimizer_rmsprop";
    system_dict["total_tests"] += 1;
    print_start(test, system_dict["total_tests"])
    if(forward):
        try:
            gtf = prototype(verbose=0);
            gtf.Prototype("sample-project-1", "sample-experiment-1");
            gtf.Default(dataset_path="datasets/dataset_cats_dogs_train", 
                model_name="resnet50", freeze_base_network=True, num_epochs=2);
            gtf.optimizer_rmsprop(0.01, weight_decay=0.0001, decay_rate=0.9, 
                clipnorm=1.0, clipvalue=0.5);
            gtf.Train();
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
