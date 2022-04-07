
import os
import shutil

def copyDir(src, dst):
    """拷贝文件时检查同名文件，并以较大的那个文件覆盖"""
    names = os.listdir(src)
    for name in names:
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        if os.path.exists(dstname):
            srcSize = os.stat(srcname).st_size
            dstSize = os.stat(dstname).st_size
            if srcSize > dstSize:
                os.remove(dstname)
                shutil.copy2(srcname, dstname)
        else:
            shutil.copy2(srcname, dstname)

