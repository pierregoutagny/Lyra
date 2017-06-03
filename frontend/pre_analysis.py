from collections import OrderedDict
import ast


class PreAnalyzer:
    """Analyzer for the AST to give some configurations before the type inference"""

    def __init__(self, prog_ast):
        """
        :param prog_ast: The AST for the python program  
        """

        # List all the nodes existing in the AST
        self.all_nodes = list(ast.walk(prog_ast))

    def maximum_function_args(self):
        """Get the maximum number of function arguments appearing in the AST"""
        func_defs = [node for node in self.all_nodes if isinstance(node, ast.FunctionDef)]
        return max([len(node.args.args) for node in func_defs] + [1])

    def maximum_tuple_length(self):
        """Get the maximum length of tuples appearing in the AST"""
        tuples = [node for node in self.all_nodes if isinstance(node, ast.Tuple)]
        return 0 if not tuples else max([len(node.elts) for node in tuples])

    def analyze_classes(self):
        """Pre-analyze and configure classes before the type inference
        
        Do the following:
            - Propagate methods from bases to subclasses.
            - Add __init__ function to classes if it doesn't exist.
            - Return a mapping from class names to their attributes and methods.
            - Return a mapping from class names to their base classes if they have any.
            
        """
        # TODO propagate attributes to subclasses.
        class_defs = [node for node in self.all_nodes if isinstance(node, ast.ClassDef)]

        propagate_attributes_to_subclasses(class_defs)

        class_to_attributes = OrderedDict()
        class_to_base = OrderedDict()

        for cls in class_defs:
            if len(cls.bases) > 1:
                raise NotImplementedError("Multiple inheritance is not supported yet.")
            elif cls.bases:
                class_to_base[cls.name] = cls.bases[0].id
            else:
                class_to_base[cls.name] = "object"

            add_init_if_not_existing(cls)

            attributes = set()
            class_to_attributes[cls.name] = attributes

            # Inspect all class-level statements
            for cls_stmt in cls.body:
                if isinstance(cls_stmt, ast.FunctionDef):
                    # Add function to class attributes and get attributes defined by self.some_attribute = value
                    attributes.add(cls_stmt.name)
                    if not cls_stmt.args.args:
                        continue
                    first_arg = cls_stmt.args.args[0].arg  # In most cases it will be 'self'

                    # Get attribute assignments where attribute value is the same as the first argument
                    func_nodes = ast.walk(cls_stmt)
                    assignments = [node for node in func_nodes if isinstance(node, ast.Assign)]

                    for assignment in assignments:
                        for target in assignment.targets:
                            if (isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name) and
                                    target.value.id == first_arg):
                                attributes.add(target.attr)
                elif isinstance(cls_stmt, ast.Assign):
                    # Get attributes defined as class-level assignment
                    for target in cls_stmt.targets:
                        if isinstance(target, ast.Name):
                            attributes.add(target.id)

        return class_to_attributes, class_to_base

    def get_all_configurations(self):
        config = Configuration()
        config.max_tuple_length = self.maximum_tuple_length()
        config.max_function_args = self.maximum_function_args()
        config.classes_to_attrs, config.class_to_base = self.analyze_classes()

        return config


class Configuration:
    """A class holding configurations given by the pre-analyzer"""
    def __init__(self):
        self.max_tuple_length = 0
        self.max_function_args = 1
        self.classes_to_attrs = OrderedDict()
        self.class_to_base = OrderedDict()


def propagate_attributes_to_subclasses(class_defs):
    """Start depth-first methods propagation from inheritance roots to subclasses"""
    inheritance_forest = get_inheritance_forest(class_defs)
    roots = get_forest_roots(inheritance_forest)
    name_to_node = class_name_to_node(class_defs)

    for root in roots:
        propagate(root, inheritance_forest, name_to_node)


def propagate(node, inheritance_forest, name_to_node):
    """Propagate methods to subclasses with depth first manner.
    
    :param node: The class node whose methods are to be propagated
    :param inheritance_forest: A data-structure containing the inheritance hierarchy
    :param name_to_node: A mapping from class names to their AST nodes 
    """
    for subclass in inheritance_forest[node]:
        base_node = name_to_node[node]
        sub_node = name_to_node[subclass]
        sub_funcs_names = [func.name for func in sub_node.body if isinstance(func, ast.FunctionDef)]

        # Select only functions that are not overridden in the subclasses.
        inherited_funcs = [func for func in base_node.body
                           if isinstance(func, ast.FunctionDef) and func.name not in sub_funcs_names]
        sub_node.body += inherited_funcs
        # Propagate to sub-subclasses..
        propagate(subclass, inheritance_forest, name_to_node)


def class_name_to_node(nodes):
    """Return a mapping for the class name to its AST node."""
    name_to_node = {}
    for node in nodes:
        name_to_node[node.name] = node
    return name_to_node


def get_forest_roots(forest):
    """Return list of classes that have no super-class (other than object)"""
    roots = list(forest.keys())
    for node in forest:
        for sub in forest[node]:
            if sub in roots:
                roots.remove(sub)
    return roots


def get_inheritance_forest(class_defs):
    """Return a forest of class nodes
    
    Each tree represents an inheritance hierarchy. There is a directed edge between class 'a' and class 'b'
    if 'b' extends 'a'.
    """
    tree = {}
    for cls in class_defs:
        tree[cls.name] = []
    for cls in class_defs:
        bases = cls.bases
        for base in bases:
            tree[base.id].append(cls.name)
    return tree


def add_init_if_not_existing(class_node):
    """Add a default empty __init__ function if it doesn't exist in the class node"""
    for stmt in class_node.body:
        if isinstance(stmt, ast.FunctionDef) and stmt.name == "__init__":
            return
    class_node.body.append(ast.FunctionDef(
        name="__init__",
        args=ast.arguments(args=[ast.arg(arg="self", annotation=None)]),
        body=[ast.Pass()],
        decorator_list=[],
        returns=None,
        lineno=class_node.lineno
    ))