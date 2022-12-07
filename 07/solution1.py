from pathlib import Path
from typing import Union


class File:
    def __init__(self, path, name, size=None):
        self.path = path.resolve()
        self.name = name
        self.size = size

    def __repr__(self):
        return f'<{self.__class__.__name__:4} {str(self.path / self.name)} size={self.size}>'

    def is_dir(self):
        return False


class Dir(File):
    def __init__(self, path, name):
        super().__init__(path, name, 0)

    def is_dir(self):
        return True


class ParseTree:
    def __init__(self, filename):
        self.cwd = Path('/')
        self.flat_files: Dict[Path, Union[File, Dir]] = dict()
        self.add_file(Dir(Path('/'), '/'))

        self.is_executing_ls = False
        self.filename = filename

    def read_input(self):
        with open(self.filename) as fd:
            while True:
                line = fd.readline().strip()
                if line == '':
                    break

                parts = line.split(' ')

                if parts[0] == '$':
                    self.is_executing_ls = False
                    # command execution
                    command = parts[1]
                    if command == 'cd':
                        self.cwd /= parts[2]
                        continue
                    elif command == 'ls':
                        # $ ls
                        self.is_executing_ls = True
                        continue
                    else:
                        raise Exception(f'Unkown command {parts}')
                elif parts[0] == 'dir':
                    # dir - as content
                    file = Dir(self.cwd, parts[1])
                else:
                    # file - as content
                    file = File(self.cwd, parts[1], int(parts[0]))
                self.add_file(file)

    def add_file(self, file_inst):
        #print(f'{file_inst}')
        self.flat_files[file_inst.path / file_inst.name] = file_inst

    def get_parent_dir_from_path(self, path: Path):
        parent_path = path / '..'
        parent_path = parent_path.resolve()
        parent = self.flat_files[parent_path]
        return parent

    def get_parent_dir_of_file(self, file_inst):
        return self.get_parent_dir_from_path(file_inst.path / file_inst.name)

    def add_size(self, file_inst, size):
        # add to current path
        parent = self.get_parent_dir_of_file(file_inst)
        #print(f'Adding size {size} from {file_inst.path} to {parent}')
        parent.size += size

        if file_inst.path == Path('/'):
            return

        # go to parent
        self.add_size(parent, size)


if not True:
    tree = ParseTree('input.sample')
else:
    tree = ParseTree('input')


tree.read_input()

print('Walking down by the tree.')
i = 0
for path, file_inst in tree.flat_files.items():
    if file_inst.is_dir():
        continue

    #print(f'Adding size of file #{i}:', file_inst)
    tree.add_size(file_inst, file_inst.size)
    #print()
    i += 1


max_paths = []
total_sum = 0

dirs = []
for path, file_inst in tree.flat_files.items():
    if not file_inst.is_dir():
        continue

    dirs.append(file_inst)

    if file_inst.size < 100_000:
        total_sum += file_inst.size

    #print(file_inst)

print('Total sum smaller than limit is:', total_sum)
sorted_dirs = list(sorted(dirs, key=lambda x: x.size))

total_sum_root = tree.flat_files[Path('/')].size
total_capacity = 70_000_000
required_free = 30_000_000

#input: 32283214 is too high
#input: 13880430 is wrong

# required of free: 30_000_000
# total capacity:   70_000_000
# total used by /:  48_381_165
# free:             21_618_835

for i, item in enumerate(sorted_dirs):
    #print(f'{item.size/1_000_000}')
    used_after_del = total_sum_root - item.size
    free_after_del = total_capacity - used_after_del
    #print(f'current {item}, {free_after_del=} > {required_free=}')
    if free_after_del > required_free:
        print(f'smallest adept to delete is #{i}: {item}, {free_after_del} > {required_free}')
        break
