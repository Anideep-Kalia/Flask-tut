from flask import Flask, redirect, url_for, render_template, request

app=Flask(__name__)

@app.route('/')
def landing():
    return "hellow!!!"

# FLOW: submit -> res.html -> result
# FLOW: /score -> dasghborad -> index.html


# TOPIC: render_templar used for rendering HTML in flask all the html should be written indside templates folder
@app.route('/dashboard/dict')
def dsh():
    score = int(request.args.get('score'))
    res = request.args.get('res')
    return render_template('index.html',score=score,res=res)        

# TOPIC: dynamic routing 
@app.route('/pass/<int:score>')
def Passed(score):
    return "score is: "+str(score)

@app.route('/fail/<int:score>')
def Failed(score):
    return "score is: "+str(score)

# TOPIC: url_for and redirect
@app.route('/<int:score>')
def fxn(score):
    res=""
    if score >33:
        res="Passed"
    else:
        res="Failed"
    # url=url_for('first')          # URL for the mentioned function 
    # return redirect(url_for('dsh',res=res,score=score))  #-> could be used but better way below
    dict={'score':score,'res':res}
    return redirect(url_for('dsh', **dict)) 

# TOPIC: methods & requests
@app.route('/submit',methods=['POST','GET'])
def submit():
    return render_template('res.html')
    
@app.route('/result',methods=['POST','GET'])
def result():
    if request.method=='POST':
        return "welcome to result page: "+request.form['score']




if __name__ == '__main__':
    app.run(debug=True)   #for live rendering debug is set to true