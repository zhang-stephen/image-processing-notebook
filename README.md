# 数字图像处理学习笔记

### Preface

这个repo仅用于个人修读研究生学位中对数字图像处理技术的学习笔记整理。根据实验室的研究方向和导师的要求，我主要关注以下方面：

- 数字图像处理技术与FPGA相结合，
- 红外图像（灰度图像）和3D点云融合，
- 机器学习模型在图像处理中的应用
    - 机器学习模型在FPGA上部署
- 异构计算

不过该项目目前（2023.05）主要还是以一个初学者的角度出发，以Jupyter Notebook作为载体，使用python语言学习和实现数字图像处理的经典方法，包括但不限于图像增强，图像变换，以及特征提取和分析等。这些笔记经过进一步整理将会发布在[我的博客](https://blogs.stephen-zhang.cn)。

### Usage

如果要运行该repo中的代码，需要提前安装conda环境，Anaconda/Miniconda均可。然后使用命令创建虚拟环境`img`并激活：

```shell
$ conda env create --file environment.yml
$ conda activate img
```

然后需要在项目根目录下执行`pip install [-e] ./`，安装`imgtools/`供notebooks调用。最后在项目根目录下运行`jupyter notebook`或者`jupyter lab`打开项目即可。

为了更好的适应使用git管理Juptyer Notebook，所有提交到远端的Notebook中均使用[nbstripout](https://github.com/kynan/nbstripout)过滤掉输出数据，因此clone项目后需要重新运行以观察输出。

此外，由于Github LFS不友好的机制，所有的图片文件均使用图床[sm.ms](https://smms.app)进行管理。此部分代码见[ImageHosting](./imgtools/ImageHosting/)。

#### ImageHosting

`ImageHosting`对外提供了[sm.ms](https://smms.app)的管理对象`smms_app`和对应的类`SmmsApp`，并提供了一组易于使用的API用于加载图像到本地。要使用它们，参考以下示例：

```python
from imgtools.ImageHosting import smms_app
from pathlib import Path

img = smms_app('2uzYGhVDw1F6Nv5')
```

由于重载了`__call__`方法，所以可以像调用一个函数一样调用实例`smms_app`：

- 入参：图像在图床网站中的哈希值
- 返回：包含图像的类文件对象

此repo暂**不**接受任何PR。

#### bmp2png

由于[sm.ms](https://smms.app)不支持上传BMP格式的图片，因此需要一个工具将其转换为同样是无损压缩的PNG格式。见[bmp2png.py](./imgtools/utils/bmp2png.py)。

运行`python3 imgtools/utils/bmp2png.py /path/to/image.bmp`，即可在相同路径下生成PNG格式的图片。

### References

#### Python Programming

1. [Python 3.10 Documentations](https://docs.python.org/zh-cn/3.10/)
2. [Pillow Documentations](https://docs.python.org/zh-cn/3.10/): a fork of PIL(Python Image Library)

#### 图片素材来源
1. [images from *Digital Image Processing* 3rd edition](https://github.com/lionelee/DIP3E_images)
2. [《图像处理与图像分析技术（C/C++语言版）》随书课件](http://www.tup.tsinghua.edu.cn/booksCenter/book_08523801.html)

#### For Starter

1. *Digital Image Processing*, 4th Edition(Global), Rafael C. Gonsalez
2. [图像处理与图像分析基础（C/C++语言版）](http://www.tup.tsinghua.edu.cn/booksCenter/book_08523801.html), 任明武, 南京理工大学

<!-- EOF -->
