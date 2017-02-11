Tmplaye
======

[![Build Status](https://travis-ci.org/HaoPatrick/Tmplaye.svg?branch=master)](https://travis-ci.org/HaoPatrick/Tmplaye)
[![Coverage](https://codecov.io/github/HaoPatrick/Tmplaye/coverage.png)](https://codecov.io/github/HaoPatrick/Tmplaye)

Simple And Weak Template Engine

```Python
from Tmplaye import Tmplaye

templite = Tmplaye('''
	 
	 <h1>Hello {{name|upper}}!</h1>
     
	 {% for topic in topics %}
         <p>You are interested in {{topic}}.</p>
     {% endfor %}
     
	 {% include "more.html" %}
	 
	 {% for k, v in dict_content.items() %}
	    <p> {{k}}, {{v}}</p>
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
    'aaa': 'aaa',
    'dict_content':{"Hao":"1","HLH":"2"}
})

print(text)

```

Output:


```HTML
         <h1>Hello HAO!</h1>

         <p>You are interested in Python.</p>

         <p>You are interested in Javascript.</p>

         <p>You are interested in C++.</p>

		 Something from more.
		 
		 <p>Hao, 1</p>
		 
		 <p>HLH, 2</p>

        <p>Test</p>

```