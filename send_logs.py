#import json
import requests
import getpass

TORCH_REST_API_URL = "http://localhost:5050/listening"

user = getpass.getuser()
log_input_example = "np.zeros(5)"
log_output_example = "[0,0,0,0,0]\n array(float)"

payload = {'usr':user,'msg':log_input_example}
# sendingpayload to the api
r = requests.post(TORCH_REST_API_URL, files = payload).json()