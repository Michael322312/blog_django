import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_django.settings")
django.setup()


from blog.models import Blog, Comment, Post

def add_blog(name):
    blog = Blog(name=name)
    blog.save()
    return blog


def add_post(blog_id, name, text):
    post = Post(
        blog=Blog.objects.get(id=blog_id),
        name=name,
        text=text
    )
    post.save()
    return post

def add_comment(post_id, text, author):
    comment = Comment(
        post=Post.objects.get(id=post_id),
        text=text,
        author=author
    )
    comment.save()
    return comment

def edit_post(post_id, name = None, text = None):
    post = Post.objects.get(id=post_id)
    if name:
        post.name = name
    if text:
        post.text = text
    post.save()
    return post


while True:
    choice = int(input("Create blog - 1\nCreate post - 2\nWrite comment - 3\nEdit post - 4\nBrowse - 5\nExit - 0\n\n"))

    match choice:
        case 1:
            name_blog = input("Enter name of blog:")
            print(f"Blog {add_blog(name_blog)} created sucsessfully!")
        case 2:
            blog_id = int(input("Enetr blog id:"))
            name = input("Enter name of post")
            text = input("Enter filling of post:")
            print(f"Post {add_post(blog_id, name, text)} created!")
        case 3:
            post_id = int(input("Enter post id:"))
            text = input("Enter text of comment:")
            author = input("Enter author of the author:")
            add_comment(post_id, text, author)
            print(f"You've sucsesfully wrote a comment!")
        case 4:
            post_id = int(input("Enter post id:"))
            name = input("Enter name of post (Press Enter to not edit this):")
            text = input("Enter filling of post (Press Enter to not edit this):")
            print(f"Post {edit_post(post_id, name, text)} has been sucsesfully edited!")
        case 5:
            while True:
                for i in Blog.objects.all():
                    print(f"{i.id}) {i.name} blog")
                ask = int(input("Enter blog id (Exit - 0):"))
                if ask == 0:
                    break
                try:
                    blog = Blog.objects.get(id=ask)
                    while True:
                        print(f"You're right know in blog {blog.name}")
                        for i in Post.objects.filter(blog=blog).all():
                            print(f"{i.id}) {i.name} Upload date:{i.date}")
                        ask2 = int(input("Enter post id (0 - exit):"))
                        if ask2 == 0:
                            break
                        try:
                            post = Post.objects.get(id=ask2)
                            while True:
                                print("You're right know in post", post.name)
                                for i in Comment.objects.filter(post=post).all():
                                    print(f"{i.id}) Author: '{i.author}' Upload Date: {i.date} Text: '{i.text}'")
                                ask3 = int(input("Enter 0 to exit"))
                                if ask3 == 0:
                                    break
                        except:
                            pass
                except:
                    pass
        case 0:
            break