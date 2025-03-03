# 拷贝
import os
import  sys

def copy_file(source,destination):
    """复制文件或目录"""
    try:
        if os.path.isdir(source):
            if not os.path.exists(destination):
                os.makedirs(destination)
            for file in os.listdir(source):
                copy_file(os.path.join(source,file),os.path.join(destination,file))
        elif os.path.isfile(source):
            with open(source,'rb') as f:
                with open(destination,'wb') as d:
                    d.write(f.read())
        else:
            print('源文件不存在')
            return False
    except Exception as e:
        print(e)
        return False

def main():
    if len(sys.argv) < 3:
        print('Usage: python cp.py source destination')
        sys.exit(1)        
    source = sys.argv[1]
    destination = sys.argv[2]

    copy_file(source,destination)

if __name__ == '__main__':
    main()

            
