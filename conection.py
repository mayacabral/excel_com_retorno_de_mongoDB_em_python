from pymongo import MongoClient
import csv


mongo_atlas = MongoClient("mongodb+srv://mayaragcabral:12345@cluster0.qpwswdk.mongodb.net/admin?retryWrites=true&loadBalanced=false&replicaSet=atlas-5o4v36-shard-0&readPreference=primary&srvServiceName=mongodb&connectTimeoutMS=10000&w=majority&authSource=admin&authMechanism=SCRAM-SHA-1&3t.uriVersion=3&3t.connection.name=atlas-5o4v36-shard-0&3t.databases=admin&3t.alwaysShowAuthDB=true&3t.alwaysShowDBFromUserRole=true&3t.sslTlsVersion=TLS")

sample_mflix = mongo_atlas["sample_mflix"]

movies = sample_mflix["movies"]


