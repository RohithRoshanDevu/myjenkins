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
def restore_func(stack,surl,tenant,dump_id,passp,worker_pool,uname,key,restore_type,quarter,csv_flag,datasets,
                 datasets_config,models_list):
    print 'Entered into restore function'
    print stack,'\n',surl,'\n',tenant,'\n',dump_id,'\n',passp,'\n',worker_pool,'\n',uname,'\n',key,'\n',restore_type,\
          '\n',quarter,'\n',csv_flag,'\n',datasets,'\n',datasets_config,'\n',models_list



# ---------------------------------------------------------------------------------> RESTORE ends <|


if __name__ == '__main__':
    # Parsing the commandline parameters
    parser = argparse.ArgumentParser(description="Copies only UIP data from a source server to destination",
                                     epilog="Happy Processing and Good Luck.")

    #-------------------------------------Arguments---------------------------------------

    parser.add_argument('--stack', '-s',
                        type=str, required=True, default="",
                        help='Which stack you want to restore Forecast, Etl or Gbm')
    parser.add_argument('--stack_url', '-surl',
                        type=str, required=True, default="",
                        help='Destination url to restore.')
    parser.add_argument('--tenant', '-t',
                        type=str, required=True, default="",
                        help='Tenant name that you want to restore')
    parser.add_argument('--dump_id', '-did',
                        type=str, required=True, default="",
                        help='Id of the Dump that you want to restore')
    parser.add_argument('--passphrase', '-p',
                        type=str, required=True, default="",
                        help='PassPhrase related to the provided dump id')
    parser.add_argument('--worker_pool', '-w',
                        type=str, required=False, default='None',
                        help='Destination stack worker pool name')
    parser.add_argument('--uname', '-u',
                        type=str, required=True, default="",
                        help='Username to login into Destination server.')
    parser.add_argument('--key', '-k',
                        type=str, required=False, default="",
                        help='idrsa key for the user to authenticate Destination server.')
    parser.add_argument('--restore_type', '-r',
                        type=str, required=False, default="FULL",
                        help='tells what kind of restore full/partial')
    parser.add_argument('--quarter', '-q',
                        type=str, required=False, default="",
                        help='Which quarter to restore')
    parser.add_argument('--csv_flag', '-cf',
                        type=str, required=False, default="",
                        help='List of CSV data seperated by comma if you want to restore only specific csv')
    parser.add_argument('--dataset_list', '-d',
                        type=str, required=False, default="",
                        help='List of datasets seperated by comma if you want to restore only specific data')
    parser.add_argument('--dataset_config_list', '-dc',
                        type=str, required=False, default="",
                        help='List of datasets seperated by comma if you want to restore only specific dataset config')
    parser.add_argument('--model_list', '-m',
                        type=str, required=False, default="",
                        help='List of models seperated by comma if you want to restore only specific models')

    args = parser.parse_known_args(sys.argv[1:])
    other_args = args[1]
    args = args[0]

    print args

    restore_func(stack=args.stack,surl=args.stack_url,tenant=args.tenant,dump_id=args.dump_id,passp=args.passphrase,
                 worker_pool=args.worker_pool,uname=args.uname,key=args.key,restore_type=args.restore_type,
                 quarter=args.quarter,csv_flag=args.csv_flag,datasets=args.dataset_list,
                 datasets_config=args.dataset_config_list,models_list=args.model_list)