from flask import Flask,request, jsonify
import json

app = Flask(__name__)

statuses = ["Not Started", "In Progress", "Completed"]
path = "/Users/juanmiguel.badilla/lyfter/m2_semana1/tasks.json"

def open_task_file(path):
    with open(path, 'r') as file:
        data = json.load(file)
        #print(data)
    return data

def validate_existing_id(new_id):
    filtered_tasks = open_task_file(path)

    for item_task in filtered_tasks:
        if item_task["Id"] == new_id:
            raise ValueError("ID already used")
    return True

def validate_status(new_status):
    if new_status.lower() not in [status.lower() for status in statuses]:
        raise ValueError("Status should be valid")
    else:
        return True

def task_to_update_by_id(task_id):
    filtered_tasks = open_task_file(path)

    task_found = None
    for task in filtered_tasks:
        if task["Id"] == int(task_id):
            task_found = task

    return task_found


@app.route("/tasks")
def getTasks():
    filtered_tasks = open_task_file(path)
    status_filter = request.args.get("Status")
    if status_filter:
        filtered_tasks = list(
            filter(lambda task: task["Status"] == status_filter, filtered_tasks)
        )

    return {"Tasks": filtered_tasks}


@app.route("/add-new-task", methods=["POST"])
def createNewTask():

    filtered_tasks = open_task_file(path)

    new_task_id = request.json['Id']
    new_task_title = request.json['Title'].strip()
    new_task_description = request.json['Description'].strip()
    new_task_status = request.json['Status'].strip()

    try:

        validate_existing_id(new_task_id)
        validate_status(new_task_status)

        if "Id" not in request.json:
            raise ValueError("Id missing from the body")
        if "Title" not in request.json or new_task_title=='':
            raise ValueError("Title missing from the body")
        if "Description" not in request.json or new_task_description=='':
            raise ValueError("Description missing from the body")
        if "Status" not in request.json:
            raise ValueError("Status missing from the body")

        new_task = {
        "Id" : new_task_id,
        "Title" : new_task_title,
        "Description" : new_task_description,
        "Status" : new_task_status,
        }

    # tasks.append(new_task)
        filtered_tasks.append(new_task)
        filtered_tasks_converted_to_json = json.dumps(filtered_tasks)

        with open (path, 'w') as file:
            file.writelines(filtered_tasks_converted_to_json)

        return (filtered_tasks_converted_to_json), 201
    except ValueError as ex:
        return jsonify(message=str(ex)), 400


@app.route("/update/<taskId>", methods=["PUT"])
def updateTask(taskId):

    filtered_tasks = open_task_file(path)

    task_to_update = task_to_update_by_id(int(taskId))

    new_task_id = request.json['Id']
    new_task_title = request.json['Title'].strip()
    new_task_description = request.json['Description'].strip()
    new_task_status = request.json['Status'].strip()

    try:

        validate_existing_id(new_task_id)
        validate_status(new_task_status)
        if task_to_update is None:
            raise ValueError("Task not found")
        if "Id" not in request.json:
            raise ValueError("Id missing from the body")
        if "Title" not in request.json or new_task_title=='':
            raise ValueError("Title missing from the body")
        if "Description" not in request.json or new_task_description=='':
            raise ValueError("Description missing from the body")
        if "Status" not in request.json:
            raise ValueError("Status missing from the body")

        task_to_update['Id'] = new_task_id
        task_to_update['Title'] = new_task_title
        task_to_update['Description'] = new_task_description
        task_to_update['Status'] = new_task_status

        for i, task in enumerate(filtered_tasks):
            print(task["Id"],'test',taskId)
            if task["Id"] == int(taskId):
                filtered_tasks[i] = task_to_update
                break

        with open(path, 'w') as file:
            json.dump(filtered_tasks, file, indent=4)

        return jsonify(filtered_tasks), 200

    except ValueError as ex:
        return jsonify(message=str(ex)), 400

@app.route("/delete/<taskId>", methods=["DELETE"])
def deleteTasks(taskId):

    filtered_tasks = open_task_file(path)

    task_to_delete = task_to_update_by_id(taskId)
    if not task_to_delete:
        return jsonify({"error": "No task found"}), 404

    tasks= [task for task in filtered_tasks if task["Id"] != int(taskId)]
    tasks_converted_to_json = json.dumps(tasks)

    with open (path, 'w') as file:
        file.writelines(tasks_converted_to_json)


    return jsonify({"message": "Task deleted successfully"}), 200


if __name__ == "__main__":
    app.run(host="localhost", debug=True)
