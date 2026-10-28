from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_grade(average):
    if average >= 90: return 'A'
    elif average >= 80: return 'B'
    elif average >= 70: return 'C'
    elif average >= 60: return 'D'
    else: return 'F'

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            # Expecting comma separated marks
            marks_raw = request.form.get('marks', '')
            marks = [float(m.strip()) for m in marks_raw.split(',') if m.strip()]
            
            if not marks:
                raise ValueError("No marks provided")
                
            total = sum(marks)
            average = total / len(marks)
            
            # --- PUSH 2 FEATURE ---
            grade = calculate_grade(average)
            
            result = {
                'total': total,
                'average': round(average, 2),
                'grade': grade # Added in Push 2
            }
        except Exception as e:
            result = {'error': str(e)}
            
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
