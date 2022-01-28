from sys import argv
import os
from pyjs import parse_ast, AstAnalyzer
cwd = os.getcwd()
cli_args = argv[1:]
filename = ''
if len(cli_args) == 0:
  python_files = [x for x in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, x)) and os.path.splitext(x)[1] == '.py']
  filename = python_files[0]
  print(f'pyjs: no files provided, using first file found by os.listdir')
else:
  filename = cli_args[0]
print(f'pyjs: using {filename}')

with open(os.path.join(cwd, filename), mode='r') as file:
  contents = file.read()
  ast = parse_ast(contents)
  analyzer = AstAnalyzer()
  analyzer.visit(ast)
  print(analyzer.data)