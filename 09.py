from blog import Blog
from blogPost import BlogPost

my_blog = Blog()
print(my_blog.posts)  # []

cikk1 = BlogPost("EAP", "Cím", "content", "2020.04.24.")
my_blog.add(cikk1)
cikk2 = BlogPost("Jakab", "Clickbait", "szöveg", "2020.03.12.")
my_blog.add(cikk2)

my_blog.listBlogPosts()

my_blog.removeByIndex(0)  # törli cikk1-et
my_blog.listBlogPosts()

my_blog.updateByIndex(0, cikk1)  # cikk1-re a megmaradt cikk2-t
my_blog.listBlogPosts()
