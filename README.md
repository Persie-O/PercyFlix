## A humble note:
- The project is not yet over, as I am adding more features to it.

# PercyFlix (Netflix Clone App (Localhost) - Django)
### User registration page:
![Registration_page](https://github.com/Persie-O/PercyFlix/assets/112958325/122311c8-7c83-42b8-b8fa-e9725b8f438b)


### User login page:
![login_page](https://github.com/Persie-O/PercyFlix/assets/112958325/f7307821-a9ff-43c5-a307-dd7e8aa290b0)

### Regular user landing page:
![Regular_user](https://github.com/Persie-O/PercyFlix/assets/112958325/c48f4d23-26cf-49a3-b50b-449ac6b33c8e)
![Screenshot from 2023-09-04 10-30-06](https://github.com/Persie-O/PercyFlix/assets/112958325/85042863-9a23-48ad-9b09-506ccca0ec48)


### staff landing page
#### Staff dashboard for managing videos and uploading, respectively:
![staff1](https://github.com/Persie-O/PercyFlix/assets/112958325/17b265b9-d86e-4564-aee2-20a5995f498b)
![staff2](https://github.com/Persie-O/PercyFlix/assets/112958325/81bf3af1-19dc-4d84-80a6-61fcd4fd9102)


#### How staff will view the videos page:
![staff3](https://github.com/Persie-O/PercyFlix/assets/112958325/d5040b30-7c4a-4d01-9eb1-cc942c322575)
![staff4](https://github.com/Persie-O/PercyFlix/assets/112958325/e5ff8ebd-f675-4b9a-9889-063e47ec3b75)


## Table of Contents
- Description
- Features
- Requirements
- Installation
- Usage
- Contributing
- License

## Description
The PercyFlix (Netflix Clone App (Localhost)) is a web application built using Django that replicates some of the core functionality and design of the popular Netflix streaming service. This project serves as a learning exercise for Django developers interested in building modern web applications.

Note: This app is intended for educational purposes and should not be used for commercial or production purposes.

## Features
- User Registration and Authentication
- Browse a Catalog of Movies and TV Shows
- View Detailed Information for Each Title
- Play Trailer (if availabe)
- Responsive Design for Mobile and Desktop
- Admin Panel for Managing Titles

## Requirements:
- Before you begin, ensure you have met the following requirements:
  
`Python:` Ensure you have Python 3.x installed on your system.
`Django:` This project is built with Django. You can install it using `pip`:
      `pip install Django`
`Database:` You can use the default SQLite database for development purposes if you are beginer but if you want explore like me in my project you can go ahead and do so.

## Installation
1. Clone this repository to your local machine:

run on your terminal: `git clone https://github.com/Persie-O/PercyFlix.git`

2. Navigate to the project directory:

  cd PercyFlix
3. Activate your virtual environment (optional)
  
4. Install the required Python packages:

run on your terminal: `pip install -r requirements.txt`

5. Run database migrations to create the database schema:

 `python manage.py migrate`

6. Create a superuser account for accessing the admin panel:

`python manage.py createsuperuser`
 NOTE: Be very keen while using multiple databases during migrations and migrating models

## Usage
- Start the development server:

On the terminal, run this after you have done all the setup: `python manage.py runserver`

- Access the application in your web browser at http://localhost:8000/.

- To access the admin panel, go to http://localhost:8000/admin/ and log in with the superuser account you created earlier.

- You can explore now as you want on the app

## Contributing
- Contributions are welcome! If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test thoroughly.
4. Submit a pull request with a clear description of your changes and the problem they solve.
#### You can also reach out to me via WhatsApp for any inquiries and quick reply: `+254792424222`

## License
This project is not licensed as it is a personal project.

`Disclaimer:` This project is not affiliated with or endorsed by Netflix, Inc. It is solely an educational exercise. Netflix is a registered trademark of Netflix, Inc.
