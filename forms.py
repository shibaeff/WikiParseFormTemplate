# pythonspot.com
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, RadioField
 
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class Query(Form):
    link = TextField('Link:', validators=[validators.required()])
    write_n = TextField('Generated length: ', validators=[validators.required()])
    
    describe = RadioField('Describe the entire article?', choices=[('Yes','Takes some time'),('No','ok')])
 
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = Query(request.form)
 
    print(form.errors)
    if request.method == 'POST':
        link=request.form['link']
        generated_text_length=request.form['write_n']
 
        if form.validate():
            # Save the comment here.
            flash('Thanks for querying!')
        else:
            flash('Error: All the form fields are required. ')
 
    return render_template('hello.html', form=form)
 
if __name__ == "__main__":
    app.run()
