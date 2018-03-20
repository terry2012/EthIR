
class RBRRule:
    def __init__(self,blockId,typeBlock):
        self.blockId = blockId

        if typeBlock == "block":
            self.rule_name = "block"+str(blockId)
        else:
            self.rule_name = "jumpFrom"+str(blockId)

        self.arg_input = []
        self.arg_global = []
        self.arg_output = []
        self.guard=[]
        self.instr=[]
        self.rbr_type = typeBlock

    def get_guard(self):
        return self.guard

    def set_guard(self, guard):
        self.guard.append(guard)

    def get_Id(self):
        return self.blockId

    def set_Id(self, b_id):
        self.blockId = b_id

    def get_instructions(self):
        return self.instructions

    def set_instructions(self, instr):
        self.instr = instr

    def add_instr(self, instr):
        self.instr.append(instr)

    def get_type(self):
        return self.rbr_type

    def get_rule_name(self):
        return self.rule_name

    def write_rule(self, fd):
        pass
    
    def display(self):
        pass
    