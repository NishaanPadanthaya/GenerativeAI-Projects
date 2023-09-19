from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = 'yourapikey'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        key = request.form['keyword']
        prompt = f"Generate SEO keywords similar to '{key}'"
        
        response = openai.Completion.create(
            model='text-davinci-003',
            prompt=prompt,
            max_tokens=100,
            temperature=0.7
        )
        
        keywords = [choice['text'].strip() for choice in response.choices]
        return render_template('seo.html', keywords=keywords, generated=True, original_key=key)
    
    return render_template('seo.html', keywords=None, generated=False, original_key='')

if __name__ == '__main__':
    app.run(debug=True)
