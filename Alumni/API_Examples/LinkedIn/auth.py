from linkedin.linkedin import (LinkedInAuthentication, LinkedInApplication,
                               PERMISSIONS)
from linkedin import linkedin
from linkedin.models import LinkedInRecipient, LinkedInInvitation
from oauthlib import *


if __name__ == '__main__':
    CONSUMER_KEY = '77tjxxy966x02u'     # This is api_key
    CONSUMER_SECRET = 'DWsRum1AmZBiQaIx'   # This is secret_key

    USER_TOKEN = '0cb41c2d-b44b-48a8-9959-d386c9b81cf3'   # This is oauth_token
    USER_SECRET = 'ef5eb204-b59b-4cbf-8f49-5f7f63e906c7'   # This is oauth_secret
    RETURN_URL = 'http://localhost:8000'



    authentication = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET, 
                                                              USER_TOKEN, USER_SECRET, 
                                                                                                                        RETURN_URL,
                                                                                                                        linkedin.PERMISSIONS.enums.values())

    # Pass it in to the app...

    application = linkedin.LinkedInApplication(authentication)

    g = application.get_profile()
    s = application.get_profile(selectors=['id', 'first-name', 'last-name', 'location', 'distance', 'num-connections', 'skills', 'educations'])
    a = application.get_connections(selectors=['first-name', 'last-name'], params={'start':10, 'count':5})
    print a['values']
    print application.get_job(job_id=5174636)
    print application.search_profile(selectors=[{'people': ['first-name', 'last-name']}])
   

    

