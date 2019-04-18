User Management System

To run this project follow this step by step guide:

    1. Install Python 3.6 in your system
    2. Download the repo in a secure place
    3. Open CLI in your system
    4. Install pip(python package)
    5. Activate virtual environment present inside project direcotry using `source venv/bin/activate` command. You can deactivate it anytime you want using "source venv/bin/deacvtivate"
    5. Go inside first directory of Project and install required python libraries using `pip install -r requirements.txt`
    6. Run command `python manage.py runserver` to start the python's wsgi server used for this application.
    7. Install "Postman" or any other similar tool to call rest api
    8. Run your operations for rest API using postman or similar

Other instructions:

1. By Default App will run on localhost using Port no 8000
2. You can change port using command 'python manage.py runserver <port_number>'
3. In case you want to use Admin pannel of Django to access Database or for any admin operations
   you can open url 'http://127.0.0.1:8000/admin'. Current id/password is `admin/admin `
4. You can create another superused for admin pannel as well using command `python manage.py createsuperuser`
5. **URL's:**

    GET
    - 
    - http://127.0.0.1:8000/users/
    - http://127.0.0.1:8000/users/<user_id>/
    - http://127.0.0.1:8000/users/\<page>/\<limit>/\<name>/\<sort>
        
        eg. http://127.0.0.1:8000/users/1/3/chhav/-age
    
    POST
    - 
    - http://127.0.0.1:8000/users/
        
       This should be passed with data in json format
        
       eg. 
            {
                "id": 1,
                "first_name": "Chhavnish",
                "last_name": "Mittal",
                "company_name": "Expedia Group",
                "age": 23,
                "city": "Gurgaon",
                "state": "Haryana",
                "zip_code": 122018,
                "email": "chhavnish@gmail.com",
                "web": null
            }
    
    DELETE
    - 
    - http://127.0.0.1:8000/users/<user_id>/
    
    PUT
    - 
    - http://127.0.0.1:8000/users/3/
        
        This should be passed with data in json format
        
       eg. 
            {
                "first_name": "Chhavnish",
                "last_name": "Mittal",
                "age": 23
            }

