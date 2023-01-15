import json
import tkinter as tk

def main():
    
    #List of user habits
    habits = []

    #Store user data in json file for persistence 
    try:
        with open("habits.json", "r") as file:
            habits = json.load(file)
    except FileNotFoundError:
        habits = []

    #Function that takes a text and writes it in habit json file
    def save_habit(event, habit_text, habits):
        habit = habit_text.get()
        habits.append(habit)
        habit_text.delete(0, 'end')

        with open("habits.json", "w") as file:
            json.dump(habits, file)

    def create_new_habit(habits):
        for widget in starting_frame.winfo_children():
            widget.destroy()

        label = tk.Label(starting_frame, text="You are creating a new habit")
        label.pack()

        habit_text = tk.Entry(starting_frame)
        habit_text.pack()
        habit_text.bind("<Return>", lambda event: save_habit(event, habit_text, habits))

        back_button = tk.Button(starting_frame, text="Back", command=starting_prompt)
        back_button.pack()

    def track_habit():
        for widget in starting_frame.winfo_children():
            widget.destroy()

        label = tk.Label(starting_frame, text="What habits would you like to track?")
        label.pack()

        for habit in habits:
            habit_frame = tk.Frame(starting_frame)
            habit_frame.pack()
            saved_habits = tk.Label(habit_frame, text=habit)
            saved_habits.pack(side='left')
            delete_button = tk.Button(habit_frame, text='Delete', command=lambda habit=habit: delete_habit(habit))
            delete_button.pack(side='right')

        back_button = tk.Button(starting_frame, text="Back", command=starting_prompt)
        back_button.pack()

    #Shows the 'home' page
    def starting_prompt():
        for widget in starting_frame.winfo_children():
            widget.destroy()

        label = tk.Label(starting_frame, text="Welcome to Dom's Habit Tracker!")
        label2 = tk.Label(starting_frame, text="What would you like to do today?")
        label.pack()
        label2.pack()

        new_habit_button = tk.Button(starting_frame, text="Create a new habit", command=lambda:create_new_habit(habits))
        new_habit_button.pack()


        track_habit_button = tk.Button(starting_frame, text="Track existing habit", command=track_habit)
        track_habit_button.pack()

    
    def delete_habit(habit):
        habits.remove(habit)
        with open("habits.json", "w") as file:
            json.dump(habits, file)
        track_habit()

    root = tk.Tk()
    starting_frame = tk.Frame(root)
    starting_frame.pack()

    starting_prompt()
    root.mainloop()

if __name__ == "__main__":
    main()