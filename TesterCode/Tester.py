import pyodide
def read_file(file_path):
    with open("inde x.html","r") as file:
        return file.read()
file_content=read_file("index.html")
pyodide.display(file_content)