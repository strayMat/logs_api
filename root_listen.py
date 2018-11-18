#import optparse
import os
from time import gmtime, strftime
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json 

my_ip = "0.0.0.0"
my_port ="5050"
logs_dir = "record/"
log_fname = "test.log"

if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)
# parser
#parser = optparse.OptionParser()
#parser.add_option('-p', '--path', default=logs_dir, help='path to the directory to save the file')
#parser.add_option('-n', '--logname', default='test.log', help='name of the log file')
#option, args = parser.parse_args()
#logs_dir = option.path
#path2logs = option.logname

# define the app
app = Flask(__name__)
CORS(app) # cross-domain requests, allow everything by default 

print('Listening on ip '+my_ip+' and port '+my_port)
print('Saving logs in the ' + logs_dir + " directory...")
print('Waiting for logs...')
#STATUS = 'live' # live/file

# API live demo route
# curl -X POST -F file=@file.log en_france.txt 'http://localhost:5000/listening
@app.route('/listening', methods=['POST'])
def api():
    path2logs = logs_dir + log_fname
    log_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    # getting data
    data = request.json
    input_msg = None
    input_usr = None
    if data == None:
        data = request.files
        input_msg = data["msg"].read().decode('utf-8')
        input_usr = data["usr"].read().decode('utf-8')
    # useless (just to send raw data but jsons are more practicall)
    #else:
    #    input_msg = data["msg"]
    #    input_usr = data["usr"]
    
    app.logger.info('incoming logs from user '+input_usr+": "+ str(input_msg))
    # response for the api
    response = jsonify(date=log_time, user = input_usr, message = input_msg)
    
    # json format of the log to write to a file
    json2write = {"date":log_time, "user":input_usr, "message":input_msg}
    with open(path2logs, 'a+') as f:
        json.dump(json2write, f)
        f.write('\n')
    return response
                
# default route
@app.route('/')
def index():
    return "Index API: listening on jupyterhub sessions!"

# Http errors handlers 
@app.errorhandler(404)
def url_error(e):
    return """
    WRONG URL! There is nothing here...
    <pre>{}<\pre>""".format(e), 404

@app.errorhandler(500)
def server_error(e):
    return """
    An internal error occured: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # used when running locally
    app.run(host=my_ip, port=my_port, debug = True)
