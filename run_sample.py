from template_engine import Templite

templite = Templite('''
	 <h1>Hello {{name|upper}}!</h1>
     {% for topic in topics %}
         <p>You are interested in {{topic}}.</p>
     {% endfor %}
     ''',
                    {'upper': str.upper},
                    )
text = templite.render({
    'name': "hao",
    'topics': ['Python', 'Javascript', 'C++']
})
print(text)
