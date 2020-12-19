import csv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def get_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def get_page(page_name=None):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()

            with open('database.csv', 'a', newline='') as db:
                email = data['email']
                subject = data['subject']
                message = data['message']

                csv_writer = csv.writer(db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow([email, subject, message])

            return redirect('/thankyou.html')
        except RuntimeError:
            return 'Something went wrong... please try again'
    else:
        return 'Something went wrong... please try again.'
