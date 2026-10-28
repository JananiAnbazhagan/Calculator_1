from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate():
    total = None
    average = None
    grade = None   # Updated for Push 2
    
    if request.method == 'POST':
        m1 = float(request.form.get('m1', 0))
        m2 = float(request.form.get('m2', 0))
        m3 = float(request.form.get('m3', 0))
        
        total = m1 + m2 + m3
        average = total / 3.0
        
        # Grade Calculation Logic (Updated for Push 2)
        if average >= 80:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 40:
            grade = "C"
        else:
            grade = "Fail"
        
    return render_template('index.html', total=total, average=average, grade=grade) # Updated for Push 2

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)