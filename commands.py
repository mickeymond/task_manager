import db

def save_task(task):
    # Save task to database
    db.tasks.insert_one(task)
    # Return response
    return True

def delete_task(id):
    # Delete task from database
    db.tasks.delete_one({"_id": id})
    # Return response
    return True

def get_tasks():
    # Get all task from database
    all_tasks = db.tasks.find()
    # Return response
    return all_tasks

def update_task(id, update):
    # Update task in database
    db.tasks.update_one({"_id": id}, {"$set": update})
    # Return response
    return True