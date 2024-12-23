# 读取目录生成对应html
import os

files_path = "./imgs/"
data_file = "./index.html"

labels = []
# Keep track of the directory names at the top level
top_dirs = []

# Traverse the directory
for i, (root, dirs, files) in enumerate(os.walk(files_path)):
    if i == 0:
        # Capture top-level directory names
        top_dirs = dirs
    else:
        # Find the directory name in `top_dirs` corresponding to the current directory
        label = []
        current_dir = os.path.basename(root)
        if current_dir in top_dirs:
            if len(files) > 0:
                label.append(current_dir)
        # Add all files in the current directory
        for name in files:
            label.append(os.path.join(root, name))
        labels.append(label)

# Write html file
with open(data_file, 'w', encoding='utf-8') as df:
	df.write("<html>\n")
	df.write("<head>\n")
	df.write("<meta charset=\"utf-8\">\n")
	df.write("<title>wu1015图床</title>\n")
	df.write("</head>\n")
	df.write("<div>\n")
	for label in labels:
		for i, img in enumerate(label):
			if i == 0:
				df.write("<hr/>")
				df.write(f"<h2 style=\"display:block;\">{img}</h2>")
				df.write("<div>")
			else:
				df.write(f"<img style=\"display:inline;width: 20%;margin:10px\" src=\"{img}\">")
		df.write("</div>")
	df.write("</div>")
	df.write("</html>")
	df.close()

