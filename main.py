
import heapq
from dataclasses import dataclass
from typing import List, Tuple

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.prompt import IntPrompt, Prompt
from rich.table import Table

console = Console()


@dataclass
class Task:
    description: str
    priority: int
    completed: bool = False


class TaskManager:
    def __init__(self):
        self.tasks: List[Tuple[int, int, Task]] = []  # [(priority, id, task)]
        self.task_counter = 0

    def add_task(self, description: str, priority: int = 1) -> None:
        """Add a task with priority (1 is highest priority)"""
        task = Task(description=description, priority=priority)
        heapq.heappush(self.tasks, (priority, self.task_counter, task))
        self.task_counter += 1
        console.print(
            f"✨ Added task: [bold green]{description}[/] (Priority: [bold blue]{priority}[/])")

    def list_tasks(self, show_indices: bool = False) -> List[Tuple[int, int, Task]]:
        """List all tasks sorted by priority and return the sorted list"""
        if not self.tasks:
            console.print("[yellow]No tasks found.[/]")
            return []

        temp_tasks = self.tasks.copy()
        sorted_tasks = []

        while temp_tasks:
            task_tuple = heapq.heappop(temp_tasks)
            if not task_tuple[2].completed:
                sorted_tasks.append(task_tuple)

        # Create a rich table
        table = Table(
            show_header=True,
            header_style="bold magenta",
            box=box.ROUNDED,
            title="[bold cyan]Tasks by Priority[/]"
        )

        if show_indices:
            table.add_column("#", style="dim")
        table.add_column("Priority", style="cyan")
        table.add_column("Description", style="green")

        for idx, (priority, _, task) in enumerate(sorted_tasks, 1):
            row = []
            if show_indices:
                row.append(str(idx))
            row.extend([str(priority), task.description])
            table.add_row(*row)

        console.print(table)
        return sorted_tasks

    def complete_task(self, task_index: int, sorted_tasks: List[Tuple[int, int, Task]]) -> None:
        """Mark a task as complete and remove it using task index"""
        if 1 <= task_index <= len(sorted_tasks):
            selected_task = sorted_tasks[task_index - 1]
            for i, task in enumerate(self.tasks):
                if task == selected_task:
                    self.tasks.pop(i)
                    heapq.heapify(self.tasks)
                    console.print(
                        f"✅ Completed task: [bold green]{selected_task[2].description}[/]")
                    return
        console.print("[bold red]Invalid task number![/]")

    def update_priority(self, task_index: int, new_priority: int, sorted_tasks: List[Tuple[int, int, Task]]) -> None:
        """Update task priority using task index"""
        if 1 <= task_index <= len(sorted_tasks):
            selected_task = sorted_tasks[task_index - 1]
            for i, task in enumerate(self.tasks):
                if task == selected_task:
                    task_id = selected_task[1]
                    task_obj = selected_task[2]
                    task_obj.priority = new_priority
                    self.tasks.pop(i)
                    heapq.heappush(
                        self.tasks, (new_priority, task_id, task_obj))
                    console.print(
                        f"📝 Updated priority for task: [bold green]{task_obj.description}[/] to [bold blue]{new_priority}[/]")
                    return
        console.print("[bold red]Invalid task number![/]")


def display_menu():
    menu = Panel(
        """[cyan]1.[/] Add task
[cyan]2.[/] List tasks
[cyan]3.[/] Complete task
[cyan]4.[/] Update priority
[cyan]5.[/] Exit""",
        title="[bold cyan]Task Manager[/]",
        border_style="cyan",
        box=box.ROUNDED
    )
    console.print(menu)


def main():
    manager = TaskManager()

    while True:
        console.clear()
        display_menu()

        try:
            choice = Prompt.ask("\nEnter your choice", choices=[
                                "1", "2", "3", "4", "5"])

            if choice == "1":
                description = Prompt.ask("\nEnter task description")
                priority = IntPrompt.ask("Enter priority", default=1)
                manager.add_task(description, priority)

            elif choice == "2":
                manager.list_tasks()

            elif choice == "3":
                sorted_tasks = manager.list_tasks(show_indices=True)
                if sorted_tasks:
                    task_num = IntPrompt.ask("\nEnter task number to complete")
                    manager.complete_task(task_num, sorted_tasks)

            elif choice == "4":
                sorted_tasks = manager.list_tasks(show_indices=True)
                if sorted_tasks:
                    task_num = IntPrompt.ask("\nEnter task number to update")
                    new_priority = IntPrompt.ask("Enter new priority")
                    manager.update_priority(
                        task_num, new_priority, sorted_tasks)

            elif choice == "5":
                console.print("\n[bold green]Goodbye! 👋[/]")
                break

            if choice != "5":
                Prompt.ask("\nPress Enter to continue")

        except KeyboardInterrupt:
            console.print("\n[bold red]Program terminated by user[/]")
            break


if __name__ == "__main__":
    main()
