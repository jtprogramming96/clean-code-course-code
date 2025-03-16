from datetime import datetime

class BlogPost:
    def __init__(self, title, description, publihed_date):
        self.title = title
        self.description = description
        self.published_date = publihed_date

    def print(self):                                 # como particularmente imprime blog posts, convertimos la función a un método de clase.
        print('Title: ' + self.title)                # Además, ya no recibe ningún parámetros, ya que imprime los valores de sus atributos
        print('Description: ' + self.description)
        print('Published: ' + self.published_date)


title = 'El código limpio es genial!'
description = 'Ahora estoy escribiendo código limpio y es genial. Deberías intentarlo!'     # evitamos usar abreviaturas, ya que es más limpio description que desc
today = datetime.now()
formatted_date = today.strftime('%Y-%m-%d %H:%M')

post = BlogPost(title, description, formatted_date)

post.print()                                               # además, renombramos print_blog_post a simplemente print, aumentando la limpieza del código