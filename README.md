# Airbnb Clone

Welcome to the Airbnb Clone! This project is a basic implementation of an Airbnb-like web application using Python, Flask, and a relational database. The goal of this project is to provide a simple and easy-to-use interface for users to search, view, and book listings, as well as for hosts to create and manage their listings.

### Command Interpreter

To start the command interpreter, simply run the `start.sh` script in the root directory of the project. This will launch the command interpreter, where you can enter commands to interact with the application.

### Usage

To use the command interpreter, you can enter the following commands:

* `listings`: Displays a list of all listings in the database.
* `listings <location>`: Displays a list of all listings in the specified location.
* `listing <id>`: Displays information about a specific listing.
* `create-listing <title> <description> <price> <location>`: Creates a new listing with the specified title, description, price, and location.
* `update-listing <id> <title> <description> <price>`: Updates the specified listing with the new title, description, and price.
* `delete-listing <id>`: Deletes the specified listing.

### Examples

Here are some examples of how to use the command interpreter:

* To list all listings, enter `listings`.
* To list all listings in New York City, enter `listings New York City`.
* To view information about a specific listing, enter `listing 12345`.
* To create a new listing, enter `create-listing My Cool Listing Description $100 New York City`.
* To update a listing, enter `update-listing 12345 My New Listing Description $150`.
* To delete a listing, enter `delete-listing 12345`.

### Notes

* The command interpreter uses a simple syntax and does not support all the features of a full-fledged Airbnb application.
* The command interpreter is intended for development and testing purposes only, and should not be used in production.
* The command interpreter uses a sample database that is included in the project. You can modify the database to test different scenarios.

I hope this helps! Let me know if you have any questions or need further assistance.
