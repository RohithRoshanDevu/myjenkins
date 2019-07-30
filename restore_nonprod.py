from email.mime.text import MIMEText as text
import argparse
import smtplib
from datetime import datetime, timedelta
import cStringIO
import subprocess
import csv
import sys
import os
# from gshell import GnanaShell

# -------------------------------------------------------------> RESTORE starts
def restore_func():
    print 'Entered into restore function'



# ---------------------------------------------------------------------------------> RESTORE ends <|


if __name__ == '__main__':
    # Parsing the commandline parameters
    parser = argparse.ArgumentParser(description="Copies only UIP data from a source server to destination",
                                     epilog="Happy Processing and Good Luck.")

    #----------------Forecast Arguments------------------------------
    parser.add_argument('--forecast', '-f',
                        type=bool, required=True, default="",
                        help='Uncheck if you dont want to restore in forecast')
    parser.add_argument('--forecast_url', '-furl',
                        type=str, required=False, default="",
                        help='Destination forcast url to restore.')
    parser.add_argument('--forecast_tenant','-ft',
                        type=str, required=True, default="",
                        help='Tenant name that you want to restore in forecast')
    parser.add_argument('--funame', '-fu',
                        type=str, required=False, default="",
                        help='Username to login as at Forecast Destination server.')
    parser.add_argument('--fkey', '-fk',
                        type=str, required=False, default="",
                        help='idrsa key for the user at Forecast Destination server.')
    parser.add_argument('--forecast_restore_type','-frt',
                        type=str, required=False,default="FULL",
                        help='tells what kind of restore full/partial')
    parser.add_argument('--csv_data','-csv_flag',
                        type=str, required=False,default="",
                        help='List of CSV data seperated by comma if you want to restore only specific csv')
    parser.add_argument('--f_dump_id','-fdid',
                        type=str, required=True, default="",
                        help='Forecast Dump Id')
    parser.add_argument('--f_passphrase','-fpp',
                        type=str, required=True, default="",
                        help='Forecast Dump\'s PassPhrase')
    parser.add_argument('--forecast_worker_pool', '-fw',
                        type=str, required=False, default='RESTORE',
                        help='source forecast server worker pool name')

    #----------------------ETL Arguments--------------------------------
    parser.add_argument('--etl', '-e',
                        type=bool, required=True, default="",
                        help='Uncheck if you dont want to restore in etl stack')
    parser.add_argument('--etl_url', '-eurl',
                        type=str, required=False, default="",
                        help='Destination etl url to restore.')
    parser.add_argument('--etl_tenant', '-et',
                        type=str, required=True, default="",
                        help='Tenant name that you want to restore in etl')
    parser.add_argument('--euname', '-eu',
                        type=str, required=False, default="",
                        help='Username to login as at etl Destination server.')
    parser.add_argument('--ekey', '-ek',
                        type=str, required=False, default="",
                        help='idrsa key for the user at ETL Destination server.')
    parser.add_argument('--etl_restore_type', '-ert',
                        type=str, required=False, default="FULL",
                        help='tells what kind of restore full/partial')
    parser.add_argument('--dataset_list', '-dlist',
                        type=str, required=False, default="",
                        help='List of datasets seperated by comma if you want to restore only specific data')
    parser.add_argument('--dataset_config_list', '-dclist',
                        type=str, required=False, default="",
                        help='List of datasets seperated by comma if you want to restore only specific dataset config')
    parser.add_argument('--e_dump_id', '-edid',
                        type=str, required=True, default="",
                        help='ETL Dump Id')
    parser.add_argument('--e_passphrase', '-epp',
                        type=str, required=True, default="",
                        help='ETL Dump\'s PassPhrase')
    parser.add_argument('--etl_worker_pool', '-ew',
                        type=str, required=False, default='',
                        help='source etl server worker pool name')

    # ----------------------GBM Arguments--------------------------------
    parser.add_argument('--gbm', '-g',
                        type=bool, required=True, default="",
                        help='Uncheck if you dont want to restore in gbm stack')
    parser.add_argument('--gbm_url', '-gurl',
                        type=str, required=False, default="",
                        help='Destination gbm url to restore.')
    parser.add_argument('--gbm_tenant', '-gt',
                        type=str, required=True, default="",
                        help='Tenant name that you want to restore in gbm')
    parser.add_argument('--guname', '-gu',
                        type=str, required=False, default="",
                        help='Username to login as at gbm Destination server.')
    parser.add_argument('--gkey', '-gk',
                        type=str, required=False, default="",
                        help='idrsa key for the user at gbm Destination server.')
    parser.add_argument('--gbm_restore_type', '-grt',
                        type=str, required=False, default="FULL",
                        help='tells what kind of restore full/partial')
    parser.add_argument('--gbm_dataset_config_list', '-gdclist',
                        type=str, required=False, default="",
                        help='List of datasets seperated by comma if you want to restore only specific dataset config')
    parser.add_argument('--gbm_model_list', '-gmlist',
                        type=str, required=False, default="",
                        help='List of models seperated by comma if you want to restore only specific models')
    parser.add_argument('--g_dump_id', '-gdid',
                        type=str, required=True, default="",
                        help='GBM Dump Id')
    parser.add_argument('--g_passphrase', '-gpp',
                        type=str, required=True, default="",
                        help='GBM Dump\'s PassPhrase')
    parser.add_argument('--gbm_worker_pool', '-gw',
                        type=str, required=False, default='',
                        help='source gbm server worker pool name')

    restore_func()