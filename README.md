
# Personal Task Manager

A command-line task manager implementing fundamental Data Structures and Algorithms (DSA) concepts for efficient task management.

## Advanced Data Structures & Algorithms Used

### 1. Priority Queue (Heap)
- Implementation: Binary heap for task prioritization
- **Time Complexity**:
  - Insert: O(log n)
  - Get highest priority: O(log n)
- Used for managing task priorities and due dates

### 2. Stack
- Implementation: Two stacks for undo/redo functionality
- **Time Complexity**: O(1) for push/pop operations
- Tracks task history and modifications

### 3. Queue
- Implementation: Deque for task notifications
- **Time Complexity**: O(1) for enqueue/dequeue
- Manages upcoming and overdue task notifications

### 4. List-based Storage
- Dynamic array implementation for task storage
- **Time Complexity**:
  - Access: O(1)
  - Append: O(1) amortized
  - Search: O(n)

### 5. JSON Serialization
- Persistent storage using JSON format
- **Space Complexity**: O(n)

## Performance Comparison

| Operation          | Basic Implementation | Enhanced Implementation |
|-------------------|---------------------|----------------------|
| Add Task          | O(n)               | O(log n)             |
| Get Next Task     | O(n)               | O(1)                 |
| Undo/Redo         | Not available      | O(1)                 |
| Task Notifications| Not available      | O(1)                 |

## Features

1. Add tasks with due dates
   - Time Complexity: O(1)
   - Space Complexity: O(1)

2. List all tasks
   - Time Complexity: O(n)
   - Space Complexity: O(1)

3. Complete tasks
   - Time Complexity: O(1)
   - Space Complexity: O(1)

4. Persistent storage
   - Uses JSON for data persistence
   - File I/O operations: O(n)

## Technical Requirements

- Python >= 3.13
- Dependencies: None (uses standard library)

## Installation

```bash
# Clone the repository
git clone https://github.com/AnuragDahal/task-manager.git

# Navigate to the project directory
cd task-manager

# Run the program
python main.py
```

## Usage

```python
python main.py
```

Follow the interactive menu:
1. Add new tasks (with description and due date)
2. List existing tasks
3. Mark tasks as complete
4. Exit

## Data Structure Details

### Task Object Structure
```python
{
    "description": str,    # Task description
    "due_date": str,      # Due date in YYYY-MM-DD format
    "completed": bool     # Task completion status
}
```

### Time Complexity Analysis

1. **Adding a Task**
   - List Append: O(1)
   - File Write: O(n)
   - Overall: O(n)

2. **Listing Tasks**
   - Iteration: O(n)
   - Memory usage: O(1)

3. **Completing a Task**
   - Access: O(1)
   - File Write: O(n)
   - Overall: O(n)
