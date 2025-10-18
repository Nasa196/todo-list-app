# Danh sách để lưu các công việc
tasks = []

def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    task = {
        'name': task_name,
        'completed': False
    }
    tasks.append(task)
    print(f"Đã thêm công việc: '{task_name}'")

def list_tasks():
    """Liệt kê tất cả các công việc hiện có trong danh sách."""
    if not tasks:
        print("Danh sách công việc trống.")
    else:
        print("Danh sách các công việc:")
        for i, task in enumerate(tasks, start=1):
            status = "[x]" if task['completed'] else "[ ]"
            print(f"{i}. {status} {task['name']}")

def complete_task(task_index):
    """Đánh dấu công việc là hoàn thành dựa vào chỉ số (index)."""
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print(f"Đã đánh dấu hoàn thành: '{tasks[task_index]['name']}'")
    else:
        print("Chỉ số công việc không hợp lệ.")

def delete_task(task_index):
    """Xóa một công việc khỏi danh sách dựa trên chỉ số."""
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Đã xóa công việc: '{removed_task['name']}'")
    else:
        print("Chỉ số công việc không hợp lệ.")

# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")

    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    add_task("Ôn lại phần hàm trong Python")

    complete_task(0)
    list_tasks()

    print("\n--- Xóa công việc thứ 2 ---")
    delete_task(1)

    print("\n--- Danh sách sau khi xóa ---")
    list_tasks()