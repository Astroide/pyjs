import ast
def parse_ast(code):
  tree = ast.parse(code)
  return tree

def get_depth(node):
  print(dir(node))

class AstAnalyzer(ast.NodeVisitor):
  def __init__(self):
    self.data = {
      'import': 0,
      'from': 0
    }

  def generic_visit(self, node):
    print (type(node).__name__)
    get_depth(node)
    super().generic_visit(node)
