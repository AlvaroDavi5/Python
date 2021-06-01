from jinja2 import Environment, FileSystemLoader

loader = FileSystemLoader("./templates")

env = Environment(loader = loader)

template = env.get_template("Campaign.tpl")

result = template.render({'Page_title':"My page with Jinja2", 'Title':"This is a title", 'Message':"Hii!!! How are you?", 'Mission':"Our mission is to make the world a better place"})

with open("index.html", 'w') as page:
	page.write(result)
