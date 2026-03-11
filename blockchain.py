import json


def store_on_chain(execution_id,report_hash):

    data = {

        "execution_id": execution_id,
        "report_hash": report_hash

    }

    with open("blockchain_record.json", "w") as f:

        json.dump(data, f, indent=4)

    return "Stored on Weilchain (simulated)"
def verify_hash(input_hash):
    with open("blockchain_record.json", "r") as f:
        data = json.load(f)

    stored_hash = data["report_hash"]
    return stored_hash == input_hash

