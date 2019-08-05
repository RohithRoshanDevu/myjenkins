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

# ------------------------------------> Login to destination server and Switch to destination tenant
def destin_tenant_switch(surl,tenant,uname,key):

    # destin_shell = GnanaShell()

    print   '\n##### Loging into destination server: ', surl,uname,key, ' #####'
    # try:
    #     destin_shell.server_info(surl)
    #     os.environ['USERNAME'] = uname
    #     destin_shell.signin(key=key)
    # except:
    #     print '\n##### Unable to singin into the destination server #####'
    #     exit(1)

    print  '\n ##### Switching to destination tenant: ',tenant,' #####'
    # try:
    #     destin_shell.switch_to(tenant)
    # except:
    #     print '\n ##### Unable to switch to destination tenant... #####'
    #     exit(1)

    # return destin_shell

# -------------------------------------------------------------------------> Login and Switch ends

# -----------------------------------------------------------------------> Forecast Restore Starts

def restore_in_forecast(surl,tenant,dump_id,passp,worker_pool,restore_type,quarter,csv_flag):
    print ' ##### Setting Forecast Restore Parameters #####'

    caches_flag = ['deals']

    if csv_flag in ['ALL','all','All']:
        csvd = 'ALL'
    else:
        csvd = csv_flag.split(',')

    if quarter in ['None','none','NONE']:
        quarter = None
    if restore_type in ['FULL','Full','full']:
        csvd = 'ALL'
        t_config = True

    elif restore_type == 'Only_Tenant_Config':
        csvd = []
        t_config = True
        caches_flag = []
    elif restore_type == 'Skip_Config':
        t_config = False
    elif restore_type == 'Specific_CSV_Data':
        t_config = False
        caches_flag = []
    elif restore_type == 'Only_Deals_Results':
        t_config = False
        csvd = []

    print 'Restore Begins ...'
    print 'shell.tenant(\'restore\',dump_id=\''+dump_id+'\',pass_phrase=\''+passp+'\',worker_pool=\''+worker_pool+\
            '\',csv_data=\''+csvd+'\',tenant_config='+str(t_config)+',caches='+str(caches_flag)+',quarter='+str(quarter)+\
             ',override_inprogress=True)'

    # destin_shell.tenant('restore',dump_id=dump_id,pass_phrase=passp,worker_pool=worker_pool,csv_data=csvd,
    #                     tenant_config=t_config,caches=caches_flag,quarter=quarter,override_inprogress=True)



# -------------------------------------------------------------------------> Forecast Restore Ends

# -----------------------------------------------------------------------> ETL Restore Starts

def restore_in_etl(surl,tenant,dump_id,passp,worker_pool,restore_type,datasets,datasets_config):
    print ' ##### Restore in etl starts #####'

# -------------------------------------------------------------------------> ETL Restore Ends

# -----------------------------------------------------------------------> GBM Restore Starts

def restore_in_gbm(surl,tenant,dump_id,passp,worker_pool,restore_type,quarter,datasets_config,models_list):
    print ' ##### Restore in gbm starts #####'

# -------------------------------------------------------------------------> GBM Restore Ends


# -------------------------------------------------------------> RESTORE starts
def restore_func(stack,surl,tenant,dump_id,passp,worker_pool,uname,key,restore_type,quarter,csv_flag,datasets,
                 datasets_config,models_list):
    print 'Entered into restore function'
    print stack,'\n',surl,'\n',tenant,'\n',dump_id,'\n',passp,'\n',worker_pool,'\n',uname,'\n',key,'\n',restore_type,\
          '\n',quarter,'\n',csv_flag,'\n',datasets,'\n',datasets_config,'\n',models_list,'\n'


    ##### Loging into destination server and switching into the destination tenant
    # dshell = destin_tenant_switch(surl,tenant,uname,key)
    destin_tenant_switch(surl, tenant, uname, key)


    ### Calling appropriate restore function
    if stack in ['FORECAST','forecast','Forecast']:
        restore_in_forecast(surl,tenant,dump_id,passp,worker_pool,restore_type,quarter,csv_flag)
    elif stack in ['ETL','Etl','etl']:
        restore_in_etl(surl,tenant,dump_id,passp,worker_pool,restore_type,datasets,datasets_config)
    elif stack in ['GBM','Gbm','gbm']:
        restore_in_gbm(surl,tenant,dump_id,passp,worker_pool,restore_type,quarter,datasets_config,models_list)



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
                        type=str, required=False, default=None,
                        help='Destination stack worker pool name')
    parser.add_argument('--uname', '-u',
                        type=str, required=True, default="",
                        help='Username to login into Destination server.')
    parser.add_argument('--key', '-k',
                        type=str, required=True, default="",
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