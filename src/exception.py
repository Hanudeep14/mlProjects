import sys


def error_message_detection(error, error_detail:sys):
    _,_, exc_tab  = error_detail.exc_info()
    file_name = exc_tab.tb_frame.f_code.co_filename
    err_msg = "The error occured in python script name [{0}] line number [{1}] error message".format(
        file_name, exc_tab.tb_lineno,str(error)
    )
    return err_msg
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detection(error_message,error_detail=error_detail)
    def __str__(self):
        return self.error_message
    
