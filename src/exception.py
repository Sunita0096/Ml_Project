#The code is a custom exception handling, designed to provide detailed error information

import sys
from logger import logging

# Function to capture detailed error information, such as file name, line number, and error message
def get_error_details(error, error_detail: sys):
    # Unpacking the traceback object from the error_detail
    _, _, traceback_obj = error_detail.exc_info()
    
    # Extract the name of the script where the error occurred
    script_name = traceback_obj.tb_frame.f_code.co_filename
    
    # Extract the line number where the error occurred
    line_number = traceback_obj.tb_lineno
    
    # Create a formatted error message with script name, line number, and the error message itself
    error_message = "Error occurred in script: [{0}] at line: [{1}] with message: [{2}]".format(
        script_name, line_number, str(error))
    
    # Return the detailed error message
    return error_message

# Custom exception class to extend Python's built-in Exception class
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # Call the base class constructor with the original error message
        super().__init__(error_message)
        
        # Generate a detailed error message using the get_error_details function
        self.error_message = get_error_details(error_message, error_detail)
    
    # Method to return the detailed error message when the exception is printed or logged
    def __str__(self):
        return self.error_message

def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise CustomException("Division by zero error", sys)

if __name__ =="__main__":
    
    # Test the function to trigger the exception
    try:
        result = divide_numbers(10, 0)
    except CustomException as ce:
        logging.info(f"An error occurred: {ce}")