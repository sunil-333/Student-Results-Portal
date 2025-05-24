import sys
sys.path.insert(0, '/home/fbr1a9vi50t9/public_html/svce.edu.in/results')

activate_this = '/home/fbr1a9vi50t9/virtualenv/public_html/svce.edu.in/results/3.7/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from app import app as application
