import os

DIR_ROOT=os.path.dirname(os.path.abspath(__file__))
DIR_DATA="{0}{1}data{1}".format(DIR_ROOT,os.sep)
DIR_DATA_RAW="{0}{1}raw{1}".format(DIR_DATA,os.sep)
DIR_DATA_STAGE="{0}{1}stage{1}".format(DIR_DATA,os.sep)
DIR_DATA_ANALYTICS="{0}{1}analytics{1}".format(DIR_DATA,os.sep)
