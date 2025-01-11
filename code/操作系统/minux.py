# 这是 python 制作的一个操作系统
# 2025.1.11 开始 自制  minux 操作系统，使用 gpt生成真的快 !

import os

class Minux:
    def __init__(self):
        self.__path = os.getcwd()
        self.__files = os.listdir(self.__path)
        self.__file = None

    def shell(self):
        print('Welcome to Minux!')
        while True:
            command = input(self.__path + ' $ ')
            if command == 'exit':
                break
            elif command == 'help':
                print(self.help())
            elif command == 'ls':
                print(self.ls())
            elif command[:2] == 'cd':
                if not self.cd(command[3:]):
                    print('No such file or directory')
            elif command[:3] == 'cat':
                content = self.cat(command[4:])
                if content:
                    print(content)
                else:
                    print('No such file or directory')
            elif command[:4] == 'echo':
                if not self.echo(command[5:]):
                    print('No such file or directory')
            elif command[:2] == 'rm':
                if not self.rm(command[3:]):
                    print('No such file or directory')
            elif command[:5] == 'mkdir':
                if not self.mkdir(command[6:]):
                    print('File exists')
            elif command[:5] == 'rmdir':
                if not self.rmdir(command[6:]):
                    print('No such file or directory')
            elif command == 'pwd':
                print(self.pwd())
            else:
                print('Command not found')

    def ls(self):
        return self.__files

    def cd(self, path):
        if os.path.exists(path):
            self.__path = path
            self.__files = os.listdir(self.__path)
            return True
        else:
            return False

    def cat(self, file):
        if file in self.__files:
            self.__file = file
            with open(self.__path + '/' + file, 'r') as f:
                return f.read()
        else:
            return False

    def echo(self, content):
        with open(self.__path + '/' + self.__file, 'w') as f:
            f.write(content)
        return True

    def rm(self, file):
        if file in self.__files:
            os.remove(self.__path + '/' + file)
            self.__files = os.listdir(self.__path)
            return True
        else:
            return False

    def mkdir(self, dir):
        if dir not in self.__files:
            os.mkdir(self.__path + '/' + dir)
            self.__files = os.listdir(self.__path)
            return True
        else:
            return False

    def rmdir(self, dir):
        if dir in self.__files:
            os.rmdir(self.__path + '/' + dir)
            self.__files = os.listdir(self.__path)
            return True
        else:
            return False

    def pwd(self):
        return self.__path

    def help(self):
        return 'ls: list files\ncd: change directory\ncat: read file\necho: write file\nrm: remove file\nmkdir: make directory\nrmdir: remove directory\npwd: show current path\nhelp: show help'
    
if __name__ == '__main__':
        os = Minux()
        # print(os.help())
        # print(os.ls())
        # print(os.cd('..'))
        # print(os.ls())
        # print(os.cd('code'))
        # print(os.ls())
        # print(os.cat('os.py'))
        # print(os.echo('hello world'))
        # print(os.cat('os.py'))
        # print(os.rm('os.py'))
        # print(os.ls())
        # print(os.mkdir('test'))
        # print(os.ls())
        # print(os.rmdir('test'))
        # print(os.ls())
        # print(os.pwd())
        os.shell()