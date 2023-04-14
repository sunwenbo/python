#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-
import requests
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

DBNAME = sys.argv[1]
TABLENAME = sys.argv[2].replace("-","_")


def create_clickhouse_table():
    url = "http://raptor-site-hj-dataplatform.int.yidian-inc.com/oak/clickhouse/table/save"
    headers = {
      'email': 'sre@yidian-inc.com',
      'Content-Type': 'application/json'
    }
    payload_dic = {'dbName': 'ops_sre_sunwenbo', 'tableName': 'sunwenbo_test', 'columns': [{'name': 'message', 'type': 'String', 'nullable': False, 'defaultValue': None}, {'name': 'host', 'type': 'String', 'nullable': False, 'defaultValue': None}, {'name': 'service', 'type': 'String', 'nullable': False, 'defaultValue': None}, {'name': 'time_local', 'type': 'DateTime', 'nullable': False, 'defaultValue': None}, {'name': 'log_type', 'type': 'String', 'nullable': False, 'defaultValue': None}], 'orderKey': ['time_local'], 'partitionKey': ['toDate(time_local)'], 'ttlColumn': 'toDate(time_local)', 'retention': 30, 'bitmap': False, 'bitmapColumns': [], 'nonBitmapColumns': []}
    payload_dic["dbName"] = DBNAME
    payload_dic["tableName"] = TABLENAME
    payload = json.dumps(payload_dic)

    database_api = "http://raptor-site-hj-dataplatform.int.yidian-inc.com/oak/clickhouse/database/list"
    dict1 = {}
    database_headers = {
        'email': 'sre@yidian-inc.com'
    }
    database_response = requests.request("POST", database_api, headers=database_headers, data=dict1)
    database_data = json.loads(database_response.text)

    try:
        for key in database_data["data"]:
            if key == DBNAME:
                response = requests.request("POST", url, headers=headers, data=payload)
                response_data = json.loads(response.text)
                if response_data["data"] == False:
                    print "in %s database, create table %s error.." % (DBNAME, payload_dic["tableName"])
                    sys.exit(1)
                else:
                    print "in %s database, create table %s Successful..." % (DBNAME, payload_dic["tableName"])
    except Exception as err:
        print err



def create_camel_data_sync():
    url = "http://camel-data-sync.inf.yidian-inc.com/ydflinkx/api/job/add"
    payload_dic = {
  "projectId": "279",
  "projectName": "运维k8s日志",
  "jobName": "ops_sre_ngconf2_test",
  "owner": "sunwenbo@yidian-inc.com",
  "description": None,
  "status": "finished",
  "statusName": "已结束",
  "reader": {
    "name": "kafkareader",
    "parameter": {
      "groupId": "ops_sre_sunwenbo",
      "channel": 3,
      "column": [
        "message",
        "host",
        "service",
        "time_local",
        "log_type"
      ],
      "topic": "ops_sre_ngconf2_test",
      "brokerList": "10.136.17.28:9092,10.136.17.29:9092,10.136.17.30:9092,10.136.13.9:9092,10.136.13.15:9092"
    }
  },
  "writer": {
    "name": "clickhousewriter",
    "parameter": {
      "postSql": [],
      "column": [
        "message",
        "host",
        "service",
        "time_local",
        "log_type"
      ],
      "writeMode": "insert",
      "batchTimeout": 10,
      "database": "ops_sre_sunwenbo",
      "password": "",
      "postSqlList": "",
      "longSql": "",
      "batchSize": 3072,
      "tablename": "ops_sre_ngconf2_test_local",
      "preSql": [],
      "username": "insert"
    }
  },
  "crontab": None,
  "scheduleType": None,
  "scheduleTime": None,
  "slaList": [
    {
      "user": "xuchuan",
      "type": [
        "mail",
        "sms"
      ]
    },
    {
      "user": "xiaoxiang",
      "type": [
        "mail",
        "sms"
      ]
    },
    {
      "user": "sunwenbo",
      "type": [
        "mail",
        "sms"
      ]
    }
  ],
  "lagThreshold": 0,
  "parallel": 1,
  "schedule": False,
  "overTime": 0,
  "retry": -1
}
    headers = {
        'email': 'sre@yidian-inc.com',
        'Content-Type': 'application/json'
    }
    payload_dic["jobName"] = TABLENAME
    payload_dic["reader"]["parameter"]["groupId"] = DBNAME
    payload_dic["reader"]["parameter"]["topic"] = TABLENAME
    payload_dic["writer"]["parameter"]["database"] = DBNAME
    payload_dic["writer"]["parameter"]["tablename"] = TABLENAME + "_local"
    payload_json = json.dumps(payload_dic)
    response_data = requests.request("POST", url, headers=headers, data=payload_json)
    response_json = (response_data.text)
    return response_json


def open_scheduling(response_json):
    url = "http://camel-data-sync.inf.yidian-inc.com/ydflinkx/api/job/start"
    headers = {
        'email': 'sre@yidian-inc.com',
        'Content-Type': 'application/json'
    }
    payload = {
        "jobId": 2300,
        "schedulePolicy": "ONCE",
        "scheduleTime": "2022-01-20 10:46:02"
    }
    response_data = json.loads(response_json)
    payload["jobId"] = response_data["data"]["id"]
    payload = json.dumps(payload)
    response = requests.request("POST", url, headers=headers, data=payload)
    print response.text


if __name__ == '__main__':
    create_clickhouse_table()
    #response_json = create_camel_data_sync()
    #open_scheduling(response_json)
