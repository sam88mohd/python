class Repository:
    def __init__(self):
        self.package = {}

    def add_package(self, package):
        self.package[package.name] = package
        
    def total_size(self):
        result = 0
        for package in self.package.values():
            result += package.size
        return result

    def __str__(self):
        return "package in repository: {}".format(self.package)

class Package:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return "package name is {}".format(self.name)

game_repo = Repository()
super_mario = Package("super mario", 4096)
adobe = Package("adobe", 103456)
game_repo.add_package(super_mario)
game_repo.add_package(adobe)
print(game_repo.total_size())