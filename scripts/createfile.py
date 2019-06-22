file_path = "../_posts/2014-3-3-Hello-World.md"
file_content = open("../_posts/2014-3-3-Hello-World.md", "r").read()
import os
img_list = os.listdir("../images/poetry")
for img in img_list:
    new_content = file_content
    new_content = new_content.replace("title: You're up and running!", "title: poetrypost"+img.strip(".jpg").strip(".png")+"\ntags:\n  - poetry\n")
    new_content = new_content.replace("config.png", "poetry/"+img)
    fd = open("../_posts/"+"2014-6-24-poetrypost"+img.strip(".jpg").strip(".png")+".md", "w")
    fd.write(new_content)
    fd.close()
    print(new_content)
