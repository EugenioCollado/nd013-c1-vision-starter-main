import argparse
import glob
import os
import random
import shutil

import numpy as np

from utils import get_module_logger


def split(source, destination):
    """
    Create three splits from the processed records. The files should be moved to new folders in the
    same directory. This folder should be named train, val and test.

    args:
        - source [str]: source data directory, contains the processed tf records
        - destination [str]: destination data directory, contains 3 sub folders: train / val / test
    """
    list_files = os.listdir(source)

    random_list = random.sample(list_files, 100)
    for i , file in enumerate(random_list):
        if(i < 87):
            shutil.copy(source + "/" + file, destination + "/train")
        elif(i < 97):
            shutil.copy(source + "/" + file, destination + "/val")
        else:
            shutil.copy(source + "/" + file, destination + "/test")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--source', required=True,
                        help='source data directory')
    parser.add_argument('--destination', required=True,
                        help='destination data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.source, args.destination)
