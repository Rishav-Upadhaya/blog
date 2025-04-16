import time
import logging

logger = logging.getLogger(__name__)

class RequestTimerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()  # Start timer before the view is called
        
        response = self.get_response(request)  # Process the request
        
        duration = time.time() - start_time  # Calculate processing time
        logger.info(f"Request to {request.path} took {duration:.4f} seconds")
        
        return response
