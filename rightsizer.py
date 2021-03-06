"""
Script will collect AWS Instance Usage and suggest a better fit if the instance is under utilized
"""

import argparse
import datetime
from modules import classes

parser = argparse.ArgumentParser()
parser.add_argument(
    '-p', '--profile',
    dest='profile',
    help='AWS Credentials Profile',
    default='default',
    required=False
)
parser.add_argument(
    '-k', '--access-key',
    dest='accessKey',
    help='AWS Access Key Id',
    default=None,
    required=False
)
parser.add_argument(
    '-s', '--secret-key',
    dest='secretKey',
    help='AWS Secret Access Key',
    default=None,
    required=False
)
parser.add_argument(
    '-r', '--region',
    dest='region',
    help='AWS Region',
    default=None,
    required=False
)
parser.add_argument(
    '-t', '--threshold',
    nargs=2,
    dest='threshold',
    help='The Cloudwatch [average, max] CPU usage threshold',
    default=[5,30],
    required=False
)
parser.add_argument(
    '-q', '--query-config',
    dest='query',
    help='The amount of [days, period] to query Cloudwatch for',
    default=[30,1800],
    required=False
)
parser.add_argument(
    '-o', '--output',
    dest='output',
    help='The name/location of the csv file to output',
    default=f'report_{datetime.datetime.date(datetime.datetime.now())}.csv'
)
args = parser.parse_args()


if __name__ == "__main__":
    run = classes.Main()
    run.main()
