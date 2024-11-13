from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from machine.machine_model import MachineModel

machine_blueprint = Blueprint("machine", __name__)

@machine_blueprint.route('', methods=['POST'])
@jwt_required()
def create_machine():
    data = request.json
    if not data or not all(key in data for key in ("machine_id", "timestamp", "data")):
        return jsonify({"msg": "Invalid data"}), 400
    machine_id = MachineModel.create_machine(data)
    return jsonify({"msg": "Machine data created", "id": machine_id}), 201

@machine_blueprint.route('', methods=['GET'])
@jwt_required()
def get_machines():
    machine_id = request.args.get("id")
    if machine_id:
        machine = MachineModel.get_machine_by_id(machine_id)
        if not machine:
            return jsonify({"msg": "Machine data not found"}), 404
        return jsonify(machine), 200
    else:
        machines = MachineModel.get_all_machines()
        return jsonify(machines), 200

@machine_blueprint.route('/<id>', methods=['PUT'])
@jwt_required()
def update_machine(id):
    data = request.json
    if not data:
        return jsonify({"msg": "Invalid data"}), 400
    updated = MachineModel.update_machine(id, data)
    if not updated:
        return jsonify({"msg": "Machine data not found"}), 404
    return jsonify({"msg": "Machine data updated"}), 200

@machine_blueprint.route('/<id>', methods=['DELETE'])
@jwt_required()
def delete_machine(id):
    deleted = MachineModel.delete_machine(id)
    if not deleted:
        return jsonify({"msg": "Machine data not found"}), 404
    return jsonify({"msg": "Machine data deleted"}), 200
