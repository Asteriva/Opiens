
from luaparser import ast
from luaparser import astnodes

class Parser:
    """
    I have used lua-parser to parse the lua code.  https://github.com/boolangery/py-lua-parser
    The lua-parser is a python module that parses lua code and returns an ast tree.
    lua-parser is not like the figure i have in my head, but it gets the job done.
    So i have to create my own parser later.
    """
    
    def __init__(self, Source):
        self.Source = Source
        self.AstTree = {}
    
    def Parse(self):
        self.AstTree = ast.parse(self.Source)
        return self.AstTree

    def ReplaceNode(self, Node, NewNode):
        for i in range(len(self.AstTree.body.body)):
            pp = self.AstTree.body.body
            if pp[i] == Node:
                pp[i] = NewNode
                break

    def InsertNode(self, Node, Where):
        self.AstTree.body.body.insert(Where, Node)

    def GetAssigns(self):
        Ret = []
        for node in ast.walk(self.AstTree):
            if isinstance(node, astnodes.Assign):
                Ret.append(node)

        return Ret

    def GetLocalAssigns(self):
        Ret = []
        for node in ast.walk(self.AstTree):
            if isinstance(node, astnodes.LocalAssign):
                Ret.append(node)

        return Ret

    def GetAddOps(self):
        Ret = []
        for node in ast.walk(self.AstTree):
            if isinstance(node, astnodes.AddOp):
                Ret.append(node)

        return Ret

    def GetSubOps(self):
        Ret = []
        for node in ast.walk(self.AstTree):
            if isinstance(node, astnodes.SubOp):
                Ret.append(node)

        return Ret

    def GetMultOps(self):
        Ret = []
        for node in ast.walk(self.AstTree):
            if isinstance(node, astnodes.MultOp):
                Ret.append(node)

        return Ret

    def GetDivOps(self):
        Ret = []
        for node in ast.walk(self.AstTree):
            if isinstance(node, astnodes.FloatDivOp):
                Ret.append(node)

        return Ret

    def GetModOps(self):
        Ret = []
        for node in ast.walk(self.AstTree):
            if isinstance(node, astnodes.ModOp):
                Ret.append(node)

        return Ret

    def GetExpoOps(self):
        Ret = []
        for node in ast.walk(self.AstTree):
            if isinstance(node, astnodes.ExpoOp):
                Ret.append(node)

        return Ret

    def GetAstTree(self):
        return self.AstTree
