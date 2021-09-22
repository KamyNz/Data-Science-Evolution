import os
import sys
import time

ROOT_PATH = os.path.dirname(
    (os.sep).join(os.path.abspath(__file__).split(os.sep)[:-2]))
sys.path.insert(1, ROOT_PATH)

from common.utils_loading import f0_load_sheets_from_source
import root

class Scenario1():

  def __init__(self,config,sheet_id,namesheet1,namesheet2):
    self.config     = config, #using config to later use it in lambda in AW or Google Cloud
    self.sheet_id   = sheet_id,
    self.namesheet1 = namesheet1,
    self.namesheet2 = namesheet2

  def process(self):
    df_act_juzgados, df_act_subjuzgados = f0_load_sheets_from_source(sheet_id,namesheet1,namesheet2)
    return(df_act_juzgados)

if __name__ == '__main__':

  #Configuring parameters
  config = {
    'data_raw':root.DIR_DATA_RAW,
    'data_stage':root.DIR_DATA_STAGE,
    'datat_analytics':root.DIR_DATA_ANALYTICS
  }

  sheet_id='1MhVtLKsSr42jlesrTPa7nrN7Pn5wurxkjSKe77oiHvQ'
  namesheet1='00ActiveOrganismoJudicial'
  namesheet2='01ActiveJuzgados'

  #Start time to check
  start_time = time.time()

  scenario1 = Scenario1(config,sheet_id,namesheet1,namesheet2)
  scenario1.process()

  #End time to check
  end_time = time.time()

  print('******************* TIME *******************')
  print('seconds:', end_time - start_time)


## Other to check functions from colab

# import pandas as pd
# sheet_id='1MhVtLKsSr42jlesrTPa7nrN7Pn5wurxkjSKe77oiHvQ'
# sheet_name='00ActiveOrganismoJudicial'

# #URL = "https://docs.google.com/spreadsheets/d/1MhVtLKsSr42jlesrTPa7nrN7Pn5wurxkjSKe77oiHvQ/edit?usp=sharing"
# #df_act_juzgados, df_act_subjuzgados = f0_load_sheets_from_source(URL,'00ActiveOrganismoJudicial','01ActiveJuzgados')

# sheet_id='1MhVtLKsSr42jlesrTPa7nrN7Pn5wurxkjSKe77oiHvQ'
# namesheet1='00ActiveOrganismoJudicial'
# namesheet2='01ActiveJuzgados'








