Notification Service API Documentation
=========================================

.. image:: https://img.shields.io/badge/License-MIT-green.svg
   :target: https://opensource.org/licenses/MIT
   :alt: License: MIT

Introduction
------------

The Notification Service API is a web service that enables sending SMS and email notifications to customers. It provides endpoints for sending notifications to single users, bulk SMS, and combined email and SMS notifications. The API is built using the FastAPI framework, which offers high performance and asynchronous task handling capabilities.

Project Structure
-----------------

The project repository follows a structured organization to demonstrate clarity and maintainability.

1. `notify/` - Contains the main application codes.
2. `notify/routes` - All the API routes with the versioning as well.
3. `docs/` - Holds the project documentation and technical resources.
4. `requirements.txt` - Lists the project dependencies for easy installation.
5. `README.md` - Provides an overview of the project, installation instructions, and usage examples.
6. `.gitignore` - Specifies the files and directories to be ignored by Git.
7. `LICENSE` - Contains the license file (e.g., MIT License) for open-source distribution.

API Endpoints
-------------

1. Send Single User SMS Notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This endpoint allows sending an SMS notification to a single user.

- URL: `/sms/single`
- Method: `POST`
- Request Body:
  - `recipient`: The phone number of the recipient.
  - `message`: The content of the SMS notification.
- Response:
  - `200 OK` on successful notification submission.
  - `400 Bad Request` if the request body is invalid.
  - `500 Internal Server Error` if an error occurs during notification sending.

2. Send Bulk SMS Notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This endpoint enables sending SMS notifications to multiple users in bulk.

- URL: `/sms/bulk`
- Method: `POST`
- Request Body:
  - `recipients`: A list of phone numbers of the recipients.
  - `message`: The content of the SMS notification.
- Response:
  - `200 OK` on successful notification submission.
  - `400 Bad Request` if the request body is invalid.
  - `500 Internal Server Error` if an error occurs during notification sending.

3. Send Email Notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This endpoint allows sending an email notification to a single user.

- URL: `/email`
- Method: `POST`
- Request Body:
  - `recipient`: The email address of the recipient.
  - `subject`: The subject of the email notification.
  - `message`: The content of the email notification.
- Response:
  - `200 OK` on successful notification submission.
  - `400 Bad Request` if the request body is invalid.
  - `500 Internal Server Error` if an error occurs during notification sending.

Installation and Usage
--------------------------

Please refer to the project's `README.md` file for detailed instructions on installing and running the Notification Service API. The `README.md` file provides examples of API usage, including request/response payloads and code snippets.

Testing
-------

The project includes a suite of unit tests to verify the functionality and reliability of the API. The tests are located in the `tests/` directory. You can run the tests using a test runner such as `pytest`.

License
-------

The Notification Service API project is licensed under the MIT License. Please see the `LICENSE` file for more details.

Contributing
------------

Contributions to the project are welcome. If you find any issues or have suggestions for improvements, please submit a GitHub issue or create a pull request with your proposed changes.

Conclusion
----------

The Notification Service API demonstrates the thought process and implementation of a web service for sending SMS and email notifications. By leveraging FastAPI and its background task capabilities, the API provides efficient and asynchronous notification sending. The project structure, documentation, and tests aim to ensure clarity, maintainability, and reliability.

For detailed usage instructions and examples, please refer to the project's `README.md` file and API documentation.
