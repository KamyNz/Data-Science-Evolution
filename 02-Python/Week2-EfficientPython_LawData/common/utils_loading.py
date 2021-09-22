#!/opt/miniconda3/envs/ds-evolution/bin/python3.8
# -*- coding: utf-8 -*-

#Loading libraries
from bs4 import BeautifulSoup
import pandas as pd # will use to store the data from the webpage
import urllib3 # package required to interact with live webpage
import time


# Loading sheets from GoogleSheets in GoogleDrive
def f0_load_sheets_from_source(sheet_id,namesheet1,namesheet2):
  """Gets the positive result of a change in status of law processes

    Parameters
    ----------
    source_url : url address
        Link to GoogleSheets to parse as db_juzgados
    json_name : str
        Name of the JSON to be created
    destination : str
        PATH in which the created HTML is going to be saved

    Returns
    -------
    df_act_juzgados : str
        A message saying that process passed without issues

    df_act_subjuzgados : str
        A message saying that process passed without issues

    prints : Different prints
        Differents prints of the processing for loading sheets
  """
  #db_juzgados = gc.open_by_url(source_url)

  #configuring URL googlesheets
  url0='https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(sheet_id,namesheet2)
  url1='https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(sheet_id,namesheet1)
  #dftest=pd.read_csv(url)
  #print(dftest.head())

  #main_sheet = db_juzgados.worksheet(namesheet1)
  #juzgados_sheet = db_juzgados.worksheet(namesheet2)
  #df_act_juzgados = get_as_dataframe(main_sheet)

  df_act_juzgados = pd.read_csv(url1)
  df_act_juzgados = df_act_juzgados.loc[:,~df_act_juzgados.columns.str.match("Unnamed")]

  df_act_subjuzgados = pd.read_csv(url0)
  df_act_subjuzgados = df_act_subjuzgados.loc[:,~df_act_subjuzgados.columns.str.match("Unnamed")]

  #dict_df_query = {}
  #for tab in query_list:
  #  dict_df_query[tab] = pd.read_excel(io.BytesIO(io_query),sheet_name=tab)
  #return(dict_df_query)

  print(df_act_juzgados.dtypes)
  print("\n")
  print(df_act_juzgados.columns)
  print("\n")
  print(df_act_juzgados.shape)
  print("\n")
  print(type(df_act_juzgados))

  print(df_act_subjuzgados.dtypes)
  print("\n")
  print(df_act_subjuzgados.columns)
  print("\n")
  print(df_act_subjuzgados.shape)
  print("\n")
  print(type(df_act_subjuzgados))

  return(df_act_juzgados,df_act_subjuzgados)

f0_load_sheets_from_source(sheet_id,namesheet1,namesheet2)

def f4_generating_merge_subjuzgados_report(dfbyreport,user_name,destination):

  """Gets the positive result of a change in status of law processes

    Parameters
    ----------
    dfbyreport: dataframe
        Dataframe of all scrape juzgados sort by Fecha Actualizacion
    user_name : str
        Name of client
    destination : str
        PATH of folder in which file should be written in

    Returns
    -------
    df_act_juzgados : str
        A message saying that process passed without issues

    df_act_subjuzgados : str
        A message saying that process passed without issues

    prints : Different prints
        Differents prints of the processing for loading sheets
  """
  #LINK:https://thispointer.com/python-how-to-get-current-date-and-time-or-timestamp/

  # Import Drive API and authenticate.

  from datetime import date
  from datetime import datetime
  import time, os, fnmatch, shutil


  drive.mount("/content/drive",force_remount=True)
  root_dir = "/content/drive/My Drive/"

  date_execution_report_short= str(date.today())
  date_execution_report = datetime.now()
  timestampStr = date_execution_report.strftime("%d-%b-%Y-%H:%M:%S%f")
  csv_name = "reporte_"+user_name+"_"+timestampStr

  try:
    # Write the DataFrame to CSV file.
    #with open(destination+csv_name+".xlsx", 'w') as f:
    #  dfbyreport.to_excel(f)
    dfbyreport.to_excel(destination+csv_name+".xlsx",sheet_name = user_name+"_"+date_execution_report_short,index=False)
  except Exception as e:
    print(e)

def structuring_sending_options():
  pass

def f1_checking_scraping_status(url):

  """Gets status of scraping status for a URL

    Parameters
    ----------
    url : str
        The URL of the ramajudicial web page to be scraped
    Returns
    -------
    site_content: html
        Site content in .html to be scraped
    mssg: str
        A message saying that is ok to scrape or not
  """
  http = urllib3.PoolManager()
  urlTemp = url
  resp = http.request('GET',urlTemp)
  site_content = resp.data.decode('utf-8')


  if(resp.status==200):
    mssg = "It is ok to do scraping"
  else:
    mssg = "We may need another idea"
  return(site_content,mssg)

def f2_writing_html_being_scraped(site_content,html_name, destination):

  """Writes a html file from the webpag to be scraped

    Parameters
    ----------
    site_content : str
        HTML object to be scraped with BeatifulSoup
    html_name : str
        Name of the HTML to be created
    destination : str
        PATH in which the created HTML is going to be saved
    Returns
    -------
    mssg : str
    A message saying that process went smoothly"""
  try:
      with open(destination+html_name,"w") as f:
        f.write(destination + site_content)
  except Exception as e:
    print(e)

def f3aux_normalizing_href(hrefinput):

  href = hrefinput

  if(href.startswith("/documents/")):
    #print(hrefinput+" To normalize point1\n")
    href_normalize = "https://www.ramajudicial.gov.co"+str(href)
  else:
    href_normalize = str(href)

  #print(href_normalize+" To normalize point2\n")
  return(href_normalize)

def f3aux_generating_date_from_extracted_text(daytemp, monthtemp):
  #from unicodedata import normalize
  #normalize('NFKD', word)
  #import unicode
  from datetime import datetime
  from unicodedata import normalize

  # Making change in daytemp if apply
  #daytemp = normalize('NFKD',str(daytemp))
  daytemp = str(daytemp).strip()
  monthtemp = str(monthtemp).strip()
  yeartemp = str(datetime.today().year)
  #string_date = str(datetime.today().year)+"-"+str(month_number_temp).strip()+"-"+dayextracted
  date_string = yeartemp+"/"+monthtemp+"/"+daytemp
  date_transform_temp = datetime.strptime(date_string, "%Y/%m/%d")

  return(date_transform_temp,[daytemp,monthtemp,yeartemp])
  #dayextracted = str(atagitem.text).replace(u'\xa0', u' ')
        #string_date = str(datetime.today().year)+"-"+str(month_number_temp).strip()+"-"+dayextracted
        #print(type(atagitem.text),month_number_temp.strip(),type(str(datetime.today().year)))

