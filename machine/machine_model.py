from pymongo import MongoClient
from bson.objectid import ObjectId
from config import MONGO_URI, DB_NAME, COLLECTION_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

class MachineModel:

    @staticmethod
    def create_machine(data):
        result = collection.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    def get_machine_by_id(machine_id):
        machine = collection.find_one({"_id": ObjectId(machine_id)})
        if machine:
            machine["_id"] = str(machine["_id"])
        return machine

    @staticmethod
    def get_all_machines():
        machines = list(collection.find())
        for machine in machines:
            machine["_id"] = str(machine["_id"])
        return machines

    @staticmethod
    def update_machine(machine_id, data):
        result = collection.update_one({"_id": ObjectId(machine_id)}, {"$set": data})
        return result.matched_count > 0

    @staticmethod
    def delete_machine(machine_id):
        result = collection.delete_one({"_id": ObjectId(machine_id)})
        return result.deleted_count > 0
