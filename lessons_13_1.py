import os


def create_folder_describe(folder="") -> dict:
    if not folder:
        folder_objects = os.listdir()
    else:
        folder_objects = os.listdir(folder)
    filenames = []
    subfolders = []
    for obj in folder_objects:

        obj_path = os.path.join(folder, obj)

        if os.path.isdir(obj_path):
            subfolders.append(obj)
        else:
        # elif os.path.isfile(obj_path):
            filenames.append(obj)
    return {'filenames': filenames, 'dirnames': subfolders}



class WorkWithFile:
    def __init__(self, folder_objects):
        self.folder_objects = folder_objects

    def sort_folder_objects(self, without_reverse=True):
        for key in self.folder_objects:
            self.folder_objects[key].sort(reverse=not without_reverse)
        return self.folder_objects

    def update_folder_objects(self, obj_name: str):
        key = "dirnames"
        if "." in obj_name:
            key = "filenames"

        self.folder_objects[key].append(obj_name)
        return self.folder_objects

    def compare_and_create_objects(self, dirname: str):
        folder_objects_real = create_folder_describe(dirname)

        for filename in set(self.folder_objects["filenames"]).difference(set(folder_objects_real["filenames"])):
            with open(os.path.join(dirname, filename), 'w') as file:
                file.write('')
        for folder in set(self.folder_objects["dirnames"]).difference(set(folder_objects_real["dirnames"])):
            os.makedirs(os.path.join(dirname, folder))


worker = WorkWithFile(create_folder_describe("homework"))
worker.sort_folder_objects()

#
# folder = create_folder_describe("homework")
# print(folder)
#
# sort_folder = sort_folder_objects(folder, False)
# print(sort_folder)
#
# new_fo = update_folder_objects(folder, "qwe.txt")
# new_fo = update_folder_objects(new_fo, "AAA")
#
# compare_and_create_objects(folder, 'alphabet')