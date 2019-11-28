from __future__ import absolute_import, unicode_literals

import time

from celery import shared_task
import requests
from django.contrib.auth.models import User
from django.db import transaction

from .models import TminMonthWise, Region, Units, TmaxMonthWise, TmeanMonthWise, SunshineMonthWise, RainfallMonthWise
from celery.contrib import rdb

def get_table(data_type):
    table = None
    if data_type == "Tmin":
        table = TminMonthWise

    elif data_type == "Tmax":
        table = TmaxMonthWise

    elif data_type == "Tmean":
        table = TmeanMonthWise

    elif data_type == "Sunshine":
        table = SunshineMonthWise

    elif data_type == "Rainfall":
        table = RainfallMonthWise

    return table

@shared_task
@transaction.atomic
def download_data(urls, username):

    def is_float(value):
        if value.isalpha():
            return False
        try:
            float(value)
            return True
        except ValueError:
            return False

    for url, data_type, region, unit in urls:
        unit = Units.objects.get(id=unit)
        region = Region.objects.get(id=region)
        data_list = []

        table = get_table(data_type)
        if not table:
            # this exception is not correct. I know, I'm just being lazy here
            # todo: raise proper exception
            raise NotImplementedError()
        response = requests.get(url, stream=True)
        # user context manager instead
        downloaded_file = open('/tmp/'+username+'-'+data_type+'.txt', "wb")
        for chunk in response.iter_content(chunk_size=256):
            if chunk:
                downloaded_file.write(chunk)
        downloaded_file.close()

        flag = False

        with open('/tmp/'+username+'-'+data_type+'.txt', 'r') as file:
            for each in file.readlines():
                if not flag:
                    if each.startswith("Year"):
                        flag = True
                else:
                    columns = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL",
                               "AUG", "SEP", "OCT", "NOV", "DEC"]
                    data = each.split("  ")
                    data = [value.strip() for value in data if is_float(value)]
                    print(data)
                    counter = 0
                    year = data[0]
                    data = data[1:]
                    for datum in data:
                        if counter < len(columns):
                            table_obj = table(region=region, year=year,
                                              month=columns[counter],
                                              unit=unit, value=datum)
                            #table_obj.save()
                            data_list.append(table_obj)
                        counter += 1

        # rdb.set_trace()
        table.objects.bulk_create(data_list)
        # TODO: check data duplication . :D

