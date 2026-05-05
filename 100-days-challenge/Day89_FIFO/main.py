from collections import deque
import time

def create_task_queue():
    """
    Initializes a deque and populates it with system tasks.
    Demonstrates the 'Enqueue' operation in a FIFO Queue.
    """
    print("[*] Task Scheduler initializing...\n")
    
    # Initialize an empty double-ended queue
    task_queue = deque()
    
    # Enqueue tasks (appending to the right side)
    task_queue.append("Clear System Logs")
    task_queue.append("Backup Database")
    task_queue.append("Restart Server")
    
    print(f"[+] Current Queue Status: {task_queue}")
    return task_queue

def process_tasks(queue):
    """
    Processes tasks from the queue using FIFO logic.
    Demonstrates the 'Dequeue' operation using popleft().
    """
    print("\n[*] Task Scheduler is starting to process tasks...\n")
    
    # Continue processing as long as the queue is not empty
    while queue:
        # Dequeue the first task (removing from the left side with O(1) complexity)
        current_task = queue.popleft()
        
        print(f">>> Processing: {current_task}...")
        
        # Simulate processing time
        time.sleep(1)
        
    print("\n[+] All tasks completed successfully. Queue is completely empty.")


if __name__ == "__main__":
    # --- EXECUTION ---
    # 1. Create the queue and enqueue tasks
    active_queue = create_task_queue()
    
    # 2. Process tasks (Dequeue)
    process_tasks(active_queue)