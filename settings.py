class the:

    # initialize default values
    def __init__(self):
        self.eg = None
        self.dump = False
        self.file = "./test.csv"
        self.help = False
        self.nums = 512
        self.seed = 10019
        self.separator = ","
    
    def change_user_settings(self, arguments, arguments_values):

        for i in range(len(arguments)):
            if arguments[i] in ['-e', '--eg']:
                self.setEg(arguments_values[i])
            elif arguments[i] in ['-d', '--dump']:
                self.setDump(arguments_values[i])
            elif arguments[i] in ['-h', '--help']:
                self.showHelp()
            elif arguments[i] in ['-f', '--file']:
                self.setFile(arguments_values[i])
            elif arguments[i] in ['-n', '--nums']:
                self.setNums(arguments_values[i])
            else:
                self.setSeed(arguments_values[i])

    def setEg(self, val):
        self.eg = val
    
    def setDump(self, val):
        self.dump = val
    
    def setFile(self, val):
        self.file = val

    def setNums(self, val):
        self.nums = int(val)
    
    def setSeed(self, val):
        self.seed = int(val)

    def __repr__(self):
        return f"eg: {self.eg} \n" \
               f"dump: {self.dump}\n" \
               f"file: {self.file}\n" \
               f"help: {self.help}\n" \
               f"nums: {self.nums}\n" \
               f"seed: {self.seed}\n"
