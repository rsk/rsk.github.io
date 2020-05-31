from os import walk

f = []
mypath = "./_posts"
photography = "./images/photography/"
new_posts = "./new_posts/"
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break
print(f.sort())
print(f)
fmax = [int(x.split('-')[-1].strip(".md").lstrip("post")) for x in f]
fmax.sort()
latest_post_no = max(fmax)
print(fmax)
print(latest_post_no)
new_post = latest_post_no + 1
fd = open("new_posts"+str(new_post)+".txt", "w")
fd.write(new_post)
fd.close()



