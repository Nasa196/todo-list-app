tasks = []

def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    tasks.append(task_name)
    print(f" Đã thêm công việc: {task_name}")


add_task("Làm bài Git")
print(tasks)
