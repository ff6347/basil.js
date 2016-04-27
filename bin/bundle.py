"""
compile the files. taken from
https://github.com/seblavoie/sublime-extendscript/blob/master/ExtendScript.py
"""
import sys
import os
import re

def process(line):
    """proces the includes"""
    output = line
    if re.match(r'.*#include', line):
        output = replace_includes(line)
    return output

def replace_includes(line):
    """load the files and replace the content"""
    path = re.sub(r'.*#include \"(.*)\";?', r'\1', line)
    current_path = os.path.dirname(os.path.abspath(__file__ + "/../"))
    # print path
    path = current_path + "/" + path
    # print path
    with open(os.path.abspath(path)) as include_file:
        file_content = include_file.read()
    return file_content

def compile_es_file(in_file, out_file):
    """compile the file"""
    file_handle = open(in_file, 'r')
    file_string = file_handle.read()
    file_handle.close()
    file_output = ''
    for line in file_string.splitlines():
        # print line
        file_output = file_output + '\n' + process(line)
    file_handle = open(out_file, 'w')
    file_handle.write(file_output)
    file_handle.close()

def main(argv):
    """main function"""
    print argv
    compile_es_file(argv[1], argv[2])
    # my code here

if __name__ == "__main__":
    main(sys.argv)
