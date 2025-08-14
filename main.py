import add
import show
import update
import delete

add_task_response = add.add_task("Sleep")
print(add_task_response)

show_tasks_response = show.show_tasks()
print(show_tasks_response)

update_task_response = update.update_task("Sleep", "Wake Up")
print(update_task_response)

delete_task_response = delete.delete_task("Wake Up")
print(delete_task_response)