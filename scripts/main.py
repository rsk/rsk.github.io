import os
from jinja2 import Template
MAIN_DIR = "../"

CATS = ['blog',
        'poetry',
        'photography',
        'drawings',
        'diary',
        'podcast',
        'updates',
        'readinglist',
        'about']

def get_latest_post_no():
    post_list = os.listdir(MAIN_DIR+"/_posts/")
    post_list = [ int(x.split('-')[-1].strip(".md").lstrip("post")) \
                  for x in post_list ]
    post_list.sort()
    return post_list[-1]

def render_post_template(latest_post_no,
                         title,
                         post_tags,
                         post_category,
                         post_image):
    """
    latest_post_no: number
    title: string
    post_tags: dictionary
    post_category: string
    """
    site = {"baseurl": "/"}
    print(latest_post_no)
    tf = open("./templates/post_template.j2", "r").read()
    t = Template(tf)
    tfs = t.render(latest_post_no=latest_post_no,
            title=title,
            post_tags=post_tags,
            post_category=post_category,
            site=site)
    tfo = open("output/post_out.txt", "w")
    tfo.write(tfs)
    tfo.close()
    print(title)
    print(post_tags)
    print(post_category)
    print(post_image)

    return None

glpn = get_latest_post_no()

render_post_template(glpn,
                     "dsa",
                     "dsa",
                     "dsa",
                     "dsa")
print(glpn)
