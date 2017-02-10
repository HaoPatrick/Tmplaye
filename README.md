Tmplaye
======

[![Build Status](https://travis-ci.org/HaoPatrick/template_engine.svg?branch=master)](https://travis-ci.org/HaoPatrick/template_engine)
[![Coverage](https://codecov.io/github/HaoPatrick/template_engine/coverage.png)](https://codecov.io/github/HaoPatrick/template_engine)

Simple And Weak Template Engine

```Python
from Tmplaye import Tmplaye

templite = Tmplaye('''
	 
	 <h1>Hello {{name|upper}}!</h1>
     
	 {% for topic in topics %}
         <p>You are interested in {{topic}}.</p>
     {% endfor %}
     
	 {% if test %}
        <p>Test</p>
     {% elif aaa %}
        <p>aaa</p>
     {% else %}
        <p>else</p>
     {% endif %}
     ''',
     {'upper': str.upper},
)

text = templite.render({
    'name': "hao",
    'topics': ['Python', 'Javascript', 'C++'],
    'test': 'False',
    'aaa': 'aaa'
})

print(text)

```

Output:


```HTML
         <h1>Hello HAO!</h1>

         <p>You are interested in Python.</p>

         <p>You are interested in Javascript.</p>

         <p>You are interested in C++.</p>


        <p>Test</p>

```