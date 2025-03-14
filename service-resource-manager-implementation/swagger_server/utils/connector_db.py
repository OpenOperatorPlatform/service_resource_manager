import json
import string

import yaml
import pymongo
import logging
from bson import json_util
from typing import List

from os import environ

storage_url=environ.get("EMP_STORAGE_URI").strip()

mydb_mongo='pi-edge'

def insert_document_k8s_platform(document=None, _id=None):
    collection = "kubernetes_platforms"
    myclient = pymongo.MongoClient(storage_url)
    mydbmongo = myclient[mydb_mongo]
    mycol = mydbmongo[collection]

    myquery = {"name": document["kubernetes_platform_name"]}
    mydoc = mycol.find_one(myquery)
    # keeps the last record (contains registrationStatus)
    if mydoc is not None:
        raise Exception("Already Registered: Platform name", document["kubernetes_platform_name"])
    try:
        insert_doc={}
        insert_doc["name"]=document["kubernetes_platform_name"]
        insert_doc["auth_credentials"]=document["kubernetes_auth_credentials"]
        mycol.insert_one(insert_doc)
    except Exception as ce_:
        raise Exception("An exception occurred :", ce_)

def insert_document_deployed_service_function(document=None, _id=None):

    collection = "deployed_service_functions"
    myclient = pymongo.MongoClient(storage_url)
    mydbmongo = myclient[mydb_mongo]
    mycol = mydbmongo[collection]

    myquery = {"name": document["service_function_name"], "location": document["location"], "instance_name":document["instance_name"]}
    mydoc = mycol.find_one(myquery)
    # keeps the last record (contains registrationStatus)
    if mydoc is not None:
        return "Requested service function (with this name) already deployed and exists in deployed_apps database"
        #raise Exception("Already Registered: PaaS name", document["paas_name"])
    try:
        insert_doc = {}

        insert_doc["name"] = document["service_function_name"]
        #insert_doc["type"] = document["paas_type"]
        insert_doc["location"] = document["location"]
        insert_doc["instance_name"] = document["instance_name"]

        # if "env_parameters" in document:
        #     insert_doc["env_parameters"] = document["env_parameters"]

        mycol.insert_one(insert_doc)
        return "Deployed service function registered successfully"
    except Exception as ce_:
        raise Exception("An exception occurred :", ce_)


def delete_document_deployed_service_functions(document=None, _id=None):
    collection = "deployed_service_functions"
    myclient = pymongo.MongoClient(storage_url)
    mydbmongo = myclient[mydb_mongo]
    mycol = mydbmongo[collection]

    myquery = {"instance_name": document["instance_name"]}
    mydoc = mycol.find_one(myquery)

    # keeps the last record (contains registrationStatus)
    if mydoc is None:
        return "Deployed Service function not found in the database"
        #raise Exception("Not found: PaaS name", document["paas_name"])
    try:
        delete_doc = {}
        delete_doc["instance_name"] = document["instance_name"]
        mycol.delete_one(delete_doc)
        return "Deployed Service function deleted successfully"
    except Exception as ce_:
        raise Exception("An exception occurred :", ce_)


def insert_document_service_function(document=None, _id=None):
    #print(document)
    collection = "service_functions"
    myclient = pymongo.MongoClient(storage_url)
    mydbmongo = myclient[mydb_mongo]
    mycol = mydbmongo[collection]

    myquery = {"name": document["service_function_name"]}
    mydoc = mycol.find_one(myquery)

    if mydoc is not None:
        return "Service function already exists in the catalogue"
 
    insert_doc = {}
    insert_doc["name"] = document["service_function_name"]
    insert_doc["type"] = document["service_function_type"]
    insert_doc["image"] = document["service_function_image"]
    insert_doc["application_ports"] = document["application_ports"]

    if "required_volumes" in document:
        insert_doc["required_volumes"] = document["required_volumes"]

    insert_doc["required_env_parameters"] = document["required_env_parameters"]
    mycol.insert_one(insert_doc)
    return "Service function registered successfully"


def insert_document_paas(document=None, _id=None):

    collection = "paas_services"
    myclient = pymongo.MongoClient(storage_url)
    mydbmongo = myclient[mydb_mongo]
    mycol = mydbmongo[collection]

    myquery = {"name": document["name"]}
    mydoc = mycol.find_one(myquery)

    if mydoc is not None:
        return "PaaS Service already exists in the catalogue"
    try:
        mycol.insert_one(document)
        return "PaaS Service registered successfully"
    except Exception as ce_:
        raise Exception("An exception occurred :", ce_)

def delete_document_service_function(service_function_input_name=None, _id=None):


    collection = "service_functions"
    myclient = pymongo.MongoClient(storage_url)
    mydbmongo = myclient[mydb_mongo]
    mycol = mydbmongo[collection]

    myquery = {"name": service_function_input_name}
    mydoc = mycol.find_one(myquery)

    if mydoc is None:
        return "Service function not found in the database"
    try:
        delete_doc = {}
        delete_doc["name"] = service_function_input_name
        mycol.delete_one(delete_doc)
        return "Service function deregistered successfully"
    except Exception as ce_:
        raise Exception("An exception occurred :", ce_)

def get_documents_from_collection(collection_input, input_type=None, input_value=None) -> List[dict]:
    collection = collection_input
    myclient = pymongo.MongoClient(storage_url)
    mydbmongo = myclient[mydb_mongo]
    mycol = mydbmongo[collection]

    try:
        mydoc_=[]
        for x in mycol.find():
            x['_id']=str(x['_id'])
            if input_type is not None:
                if input_value==x[input_type]:
                    mydoc_.append(x)
                    break
            else:
                mydoc_.append(x)

        return mydoc_
    except Exception as ce_:
        raise Exception("An exception occurred :", ce_)
