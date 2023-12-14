import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

class VirtualPet:  # Set up math behind happiness functions/task completion
    def __init__(self, name):
        self.name = name
        self.happiness = 50  # Initial happiness level
        self.coins = 0  # Initial coins

        # Load images based on happiness
        self.happiness_images = {
            "low": ImageTk.PhotoImage(Image.open("pet_image30.png")),
            "normal": ImageTk.PhotoImage(Image.open("pet_image.png")),
            "high": ImageTk.PhotoImage(Image.open("pet_image70.png"))
        }

    def get_happiness_image(self):
        if self.happiness <= 30:
            return self.happiness_images["low"]
        elif self.happiness >= 70:
            return self.happiness_images["high"]
        else:
            return self.happiness_images["normal"]

    def complete_task(self):
        self.coins += 1  # Increase coins by task completion
        self.happiness += random.randint(1, 5)  # Increase happiness for task complete
        if self.happiness > 100:
            self.happiness = 100  # Happiness level is capped at 100

    def feed_pet(self):  # Spend a coin to give pet a treat, increase happiness
        if self.coins >= 1:
            self.coins -= 1
            self.happiness += random.randint(5, 10)
            if self.happiness > 100:
                self.happiness = 100
            return True
        else:
            return False

    def water_pet(self):  # Spend a coin to give pet fresh water, increase happiness
        if self.coins >= 1:
            self.coins -= 1
            self.happiness += random.randint(5, 10)
            if self.happiness > 100:
                self.happiness = 100
            return True
        else:
            return False

    def play_with_pet(self): # Spend a coin to play with pet, increase happiness
        if self.coins >= 1:
            self.coins -= 1
            self.happiness += random.randint(8,12)
            if self.happiness > 100:
                self.happiness = 100
            return True
        else:
            return False

    def gradual_decrease(self, amount=1):  # Pet's happiness will gradually decrease for minutes passing
        self.happiness -= amount
        if self.happiness < 0:
            self.happiness = 0

    def display_info(self):
        return f"{self.name}'s Happiness Level: {self.happiness}\nCoins: {self.coins}"

class TaskTrackerApp:  # Set up Tkinter GUI
    def __init__(self, master):
        self.master = master
        self.master.title("Task Tracker with Virtual Pet")

        self.virtual_pet = None
        self.task_goals = []

        # First Page
        self.create_first_page()

    def create_first_page(self):  # The first page is a user entry page that sets up the second page
        self.first_page_frame = tk.Frame(self.master)
        self.first_page_frame.pack(pady=20)

        tk.Label(self.first_page_frame, text="Enter Pet's Name:").pack()
        self.pet_name_entry = tk.Entry(self.first_page_frame, width=30)
        self.pet_name_entry.pack(pady=5)

        tk.Label(self.first_page_frame, text="Enter Daily Task Goals (comma-separated):").pack()
        self.task_goals_entry = tk.Entry(self.first_page_frame, width=30)
        self.task_goals_entry.pack(pady=5)

        tk.Button(self.first_page_frame, text="Start", command=self.start_app).pack(pady=10)

    def start_app(self):  # This is the entry input functions with possible errors
        pet_name = self.pet_name_entry.get()
        task_goals_str = self.task_goals_entry.get()

        if pet_name and task_goals_str:
            self.virtual_pet = VirtualPet(name=pet_name)
            self.task_goals = task_goals_str.split(',')

            # Destroy first page
            self.first_page_frame.destroy()

            # Create second page
            self.create_second_page()

            # Start the timer to decrease happiness over time
            self.gradual_decrease_over_time()
        else:
            messagebox.showwarning("Incomplete Information", "Please enter both the pet's name and task goals.")

    def create_second_page(self):  # The second page displays happiness, coins, tasks, and the pet image
        self.second_page_frame = tk.Frame(self.master)
        self.second_page_frame.pack(pady=20)

        tk.Label(self.second_page_frame, text=self.virtual_pet.display_info()).pack(pady=10)

        # Display the pet image
        self.image_label = tk.Label(self.second_page_frame, image=self.virtual_pet.get_happiness_image())
        self.image_label.pack()

        self.task_checkboxes = []
        for task in self.task_goals:
            var = tk.IntVar()
            checkbox = tk.Checkbutton(self.second_page_frame, text=task.strip(), variable=var)
            checkbox.pack(anchor=tk.W)
            self.task_checkboxes.append((var, task.strip()))

        tk.Button(self.second_page_frame, text="Complete Selected Tasks", command=self.complete_selected_tasks).pack(pady=10)
        tk.Button(self.second_page_frame, text="Give Treat", command=self.feed_pet).pack(side=tk.LEFT, padx=5)
        tk.Button(self.second_page_frame, text="Fresh Water", command=self.water_pet).pack(side=tk.LEFT, padx=5)
        tk.Button(self.second_page_frame, text="Play", command=self.play_with_pet).pack(side=tk.LEFT, padx=5)

    def enter_new_tasks(self):  # Update Task List
        # Destroy the current second page
        self.second_page_frame.destroy()

        # Create a new second page with updated task goals
        self.create_second_page()

        # Show a message indicating that new tasks can be entered
        messagebox.showinfo("Enter New Tasks", "You can now enter a new set of tasks.")

    def gradual_decrease_over_time(self): # The pet's happiness with slowly decrease over time to emphasize that you need to complete tasks
        # Decrease happiness every minute
        self.virtual_pet.gradual_decrease(amount=1)

        # Update the displayed information
        info_text = self.virtual_pet.display_info()
        self.second_page_frame.winfo_children()[0].config(text=info_text)  # Update the text of the label

        # Force update
        self.second_page_frame.winfo_children()[0].update_idletasks()

        # Reset the function to run after another minute
        self.master.after(60000, self.gradual_decrease_over_time)

    def complete_selected_tasks(self):  # Pet response to completed task
        completed_tasks = [task for var, task in self.task_checkboxes if var.get() == 1]
        for var, task in self.task_checkboxes:
            if var.get() == 1:
                self.virtual_pet.complete_task()

            # Update the displayed information
        info_text = self.virtual_pet.display_info()
        self.second_page_frame.winfo_children()[0].config(text=info_text)

        # Show a positive response
        messagebox.showinfo("Tasks Completed", f"Good job! {self.virtual_pet.name} is happy.")

    def feed_pet(self):
        if self.virtual_pet.feed_pet():
            messagebox.showinfo("Feed Pet", f"{self.virtual_pet.name} is well-fed and happier.")
            self.task_checkboxes.clear()
            self.second_page_frame.destroy()
            self.create_second_page()
        else:
            messagebox.showwarning("Not Enough Coins", "You don't have enough coins to feed the pet.")

    def water_pet(self):
        if self.virtual_pet.water_pet():
            messagebox.showinfo("Water Pet", f"{self.virtual_pet.name} is hydrated and happier.")
            self.task_checkboxes.clear()
            self.second_page_frame.destroy()
            self.create_second_page()
        else:
            messagebox.showwarning("Not Enough Coins", "You don't have enough coins to give fresh water the pet.")

    def play_with_pet(self):
        if self.virtual_pet.play_with_pet():
            messagebox.showinfo("Play with Pet", f"{self.virtual_pet.name} is having fun and is happier.")
            self.task_checkboxes.clear()
            self.second_page_frame.destroy()
            self.create_second_page()
        else:
            messagebox.showwarning("Not Enough Coins", "You don't have enough coins to play with the pet.")

def main():
    root = tk.Tk()
    app = TaskTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()