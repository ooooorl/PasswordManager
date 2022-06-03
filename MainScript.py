import random
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


class PasswordManager:
    def __init__(self):
        self.website_entry = None
        self.email_entry = None
        self.password_entry = None
        self.letters = list("abcdefghijklmnopqrstuvwxyz")
        self.numbers = list("123456789")
        self.characters = list("!@#$%^&*()_+=")
        self.screen_configuration()

    def screen_configuration(self):
        """Responsible for the screen configuration."""
        screen = Tk()
        screen.title("Password Manager")
        screen.config(padx=50, pady=50)
        canvas = Canvas(height=200, width=200)
        logo_img = PhotoImage(file="logo.png")
        canvas.create_image(100, 100, image=logo_img)
        canvas.grid(row=0, column=0, columnspan=2)

        # Label of Screen Configuration
        website_label = Label(text="Website:")
        website_label.grid(row=1, column=0)
        email_label = Label(text="Email/Username:")
        email_label.grid(row=2, column=0)
        password_label = Label(text="Password:")
        password_label.grid(row=3, column=0)

        # Entries for each Label configuration
        self.website_entry = Entry(width=35)
        self.email_entry = Entry(width=35)
        self.password_entry = Entry(width=35)
        self.website_entry.focus()
        self.website_entry.grid(row=1, column=1, columnspan=2)
        self.email_entry.insert(0, "orly.plaza@hcdc.edu.ph")
        self.email_entry.grid(row=2, column=1, columnspan=2)
        self.password_entry.grid(row=3, column=1)

        # Buttons
        generate_password_buttons = Button(text="Generate Password", width=30,
                                           command=lambda: self.generate_random_password())
        generate_password_buttons.grid(row=4, column=1)
        add_button = Button(text="Add", width=30, command=lambda: self.save_information())
        add_button.grid(row=5, column=1)
        search_button = Button(text="search", width=30, command=lambda: self.search_password())
        search_button.grid(row=6, column=1)

        # Loop Infinitely the entire screen
        screen.mainloop()

    def save_information(self):
        website = self.website_entry.get().title()
        email = self.email_entry.get()
        password = self.password_entry.get()
        new_file = {
            website: {
                "email": email,
                "password": password
            }
        }

        if len(website) == 0 or len(email) == 0 or len(password) == 0:
            messagebox.showinfo(title="Ops", message="Please don't leave any fields empty!")

        else:
            if self.ask_o_cancel(website, email, password):
                # using JSON data file format to write, data is in dictionary format in order to dump
                try:
                    # trying to execute this first to check if it's exist
                    with open("data.json", "r") as data_file:
                        data = json.load(data_file)  # Take data out from the box
                        # The data file in is a dictionary data type now and ready
                        # to be updated by appending using the method (data.update()) new_file
                except FileNotFoundError:
                    # data.json doesn't exist then with this code it creates a new data called data.json
                    with open("data.json", "w") as data_file:
                        json.dump(new_file, data_file, indent=4)  # Saving the updated file

                else:
                    # this block of code will trigger when except doesn't thrown any error after try successfully executed
                    # At this point data is already loaded then ready to be updated and dump into a data_file
                    data.update(new_file)
                    with open("data.json", "w") as data_file:
                        json.dump(data, data_file, indent=4)

                finally:
                    self.website_entry.delete(0, END)
                    self.email_entry.delete(0, END)
                    self.password_entry.delete(0, END)

    def ask_o_cancel(self, website_name, email_used, password_used):
        """Return true if it's okay to save"""
        is_ok_to_save = messagebox.askokcancel(title=website_name, message=f"These are the details entered:\n"
                                                                           f"Email: {email_used}\n"
                                                                           f"Password: {password_used}\n"
                                                                           f"Do you wanna save it?")
        return is_ok_to_save

    def searched_info(self, fetched_website, fetched_email, fetched_password):
        """This method will return fetched data and display"""
        fetched_data = messagebox.showinfo(title=fetched_website, message=f"Email: {fetched_email}\n"
                                                                          f"Password: {fetched_password}")

    def search_not_found(self, website):
        not_found = messagebox.showinfo(title=website, message="No data file found!")

    def generate_random_password(self):
        """Return a random shuffled and mix generated_list password"""
        generated_list = []
        letters = random.randint(2, 6)
        numbers = random.randint(2, 6)
        characters = random.randint(2, 6)

        for i in range(letters):
            generated_list.append(random.choice(self.letters))

        for i in range(numbers):
            generated_list.append(random.choice(self.numbers))

        for i in range(characters):
            generated_list.append(random.choice(self.characters))

        shuffle(generated_list)
        # using "".join() method it allows us to convert list or iterable object into a single string
        password = "".join(generated_list)

        # This module is used for automatic copy and pasting
        pyperclip.copy(password)
        self.password_entry.insert(0, password)

    def search_password(self):
        """This methods will check if the entered email that trying to look exist then show the details
           if not then inform the user as well that the Website his/her trying to look for doesn't exist.
        """
        website_entry = self.website_entry.get().title()
        try:
            # Open the data.json in read mode as a data_file
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                fetched_data = data[website_entry]
        except KeyError and FileNotFoundError:
            # This will trigger when the website doesn't exist in the json file
            self.search_not_found(website_entry)
        else:
            # This will trigger after the tyr block code execute and when exception doesn't thrown any error
            self.searched_info(website_entry, fetched_data['email'], fetched_data['password'])
        finally:
            # Then no matter what happen this will be executed
            self.website_entry.delete(0, END)


windows = PasswordManager()
