import os
import django

EXT = 'rst'
ANNOTATE = 'source'
CHEAT_DIR = 'source/cheat'
CHEAT = 'cheat'

GIT = 'https://github.com/django/django/blob/stable/1.8.x'


def open_file(pkg_name):
    if not os.path.exists(ANNOTATE):
        os.mkdir(ANNOTATE)

    return open("{0}/{1}.{2}".format(ANNOTATE, pkg_name, EXT), "w")


def create_cheat(pkg_name):

    if not os.path.exists(CHEAT_DIR):
        os.makedirs(CHEAT_DIR)

    cheat = "{0}/{1}.{2}".format(CHEAT_DIR, pkg_name, EXT)

    if not os.path.isfile(cheat):
        with open(cheat, "w") as cheat_file:
            cheat_file.write('')
            cheat_file.close()


def title(out, name):
    out.write("=" * len(name) + "\n")
    out.write(name + "\n")
    out.write("=" * len(name) + "\n\n")


def contents(out):
    out.write(".. contents::\n")
    out.write("    :local:\n\n")


def h1(out, name):
    out.write(".. _%s:" % name + "\n")
    out.write("\n")
    out.write(name + "\n")
    out.write("=" * len(name) + "\n")


def meta(out, pkg_path, mod_name):
    # link  to the reposigory
    out.write("\n\n- `Source:{0}.{1} <{2}/{3}/{4}.py>`_ \n".format(
        pkg_path, mod_name,
        GIT, pkg_path.replace('.', '/'), mod_name))

    # include `cheat` memo
    mod_name = mod_name == '__init__' and '' or ''
    sep = mod_name and '.' or ''
    out.write("\n.. include:: {0}/{1}{2}{3}.{4}\n\n".format(
        CHEAT, pkg_path, sep, mod_name, EXT))


def automodule(out, pkg_path, mod_name):
    sep = mod_name and '.' or ''
    out.write(".. automodule:: {0}{1}{2}\n".format(pkg_path, sep, mod_name))
    out.write("    :members:\n")
    out.write("\n")


def sub_modules(out, pkg_name, subdirs):
    out.write("Sub Modules\n")
    out.write("=================\n\n")

    subdirs.sort()
    for subname in subdirs:
        if not os.path.isfile(
                pkg_name.replace('.', '/') + '/%s/__init__.py' % subname):
            continue

        out.write("- :doc:`{0}.{1}`\n\n".format(pkg_name, subname))


def module_title(out, pkg, mod_name):
    name = "{0}.{1}".format(pkg, mod_name)
    out.write("\n")
    out.write(".. _{0}:\n".format(name))
    out.write("" + "\n")
    out.write(name + "\n")
    out.write('-' * len(name) + "\n")


def module(out, package, modname, root):
    create_cheat(package + "." + modname)
    module_title(out, package, modname)
    meta(out, package, modname)
    automodule(out, package, modname)


def create_index(pkgs):
    index = "{0}/annotate_index.{1}".format(ANNOTATE, EXT)
    with open(index, "w") as index_file:
        title(index_file, "Django Annotation")
        contents(index_file)
        index_file.write('''
.. toctree::
    :maxdepth: 2

''')
        for pkg_name in pkgs:
            index_file.write("    {0}\n".format(pkg_name))
        index_file.close()


def main():
    top = os.path.dirname(django.__file__)
    pkgs = []

    for root, dirs, files in os.walk(top, topdown=True):
        if not os.path.isfile(root + '/__init__.py'):
            continue

        pkg_name = "django" + root.replace(top, '').replace('/', '.')

        pkgs.append(pkg_name)
        # index_file.write("    %s\n" % pkg_name)

        with open_file(pkg_name) as rstfile:

            title(rstfile, pkg_name)
            contents(rstfile)

            create_cheat(pkg_name)
            h1(rstfile, pkg_name)
            meta(rstfile, pkg_name, '__init__')
            automodule(rstfile, pkg_name, '')

            # sub modules
            if len(dirs) > 1:
                sub_modules(rstfile, pkg_name, dirs)

            # files
            files.sort()

            for name in files:
                mod_name, ext = os.path.splitext(name)
                if ext != '.py' or mod_name == '__init__':
                    continue

                module(rstfile, pkg_name, mod_name, root)

            rstfile.close()

    create_index(pkgs)

if __name__ == '__main__':
    main()
