from __future__ import print_function

class BlinkM(object):

    commands = {
            # 'func': ['comand', input_args, return_values]
            "setRGB": ['n', 3, 0],
            "fadeToRGB": ['c', 3, 0],
            "fadeToHSV": ['h', 3, 0],
            "fadeToRandomRGB": ['C', 3, 0],
            "fadeToRandomHSV": ['C', 3, 0],
            "playScript": ['p', 3, 0],
            "stopScript": ['o', 0, 0],
            "setFadeSpeed": ['f', 1, 0],
            "setTimeAdjust": ['f', 1, 0],
            "getColor": ['g', 0, 3],
            "setAddress": ['A', 4, 0],
            "getAddress": ['a', 0, 1],
            "getVersion": ['Z', 0, 2],
            }

    def __init__(self, port, address):
        self.port = port
        self.address = address
        for k, v in BlinkM.commands.items():
            self.__getattr__(k)


    def __getattr__(self, name):
        if name in BlinkM.commands:
            cmd = BlinkM.commands[name]
            def commandHandler(*args):
                if name == 'setAddress':
                    na = args[0]
                    args = [na, 0xd0, 0x0d, na]
                if len(args) != cmd[1]:
                    raise AttributeError
                ret = self.__sendCommand(ord(cmd[0]),
                          args, cmd[2])
                return ret


            commandHandler.__name__ = name
            self.__dict__[name] = commandHandler
            return commandHandler
        else:
            raise AttributeError

    def __sendCommand(self, command, args=None, retBytes=0):
        args = args or []
        ic = [0x01, self.address, len(args) + 1, retBytes, command]
        ic.extend(args)
        self.port.write(ic)
        self.port.flush()
        ret = []
        for i in range(retBytes):
            ret.append(ord(self.port.read()))
        # just eat the rest if anything
        self.port.read(100)
        return ret
