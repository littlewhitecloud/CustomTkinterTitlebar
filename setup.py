from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()
        
setup(
    name="CustomTkinterTitlebar",
    version="1.0.7.9",
    description="This is a 📚project can help you to have a custom titlebar! 这是一个可以创建自定义标题栏的📚项目",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="littlewhitecloud",
    url="https://github.com/littlewhitecloud/CustomTkinterTitlebar",
    packages=["CustomTkinterTitlebar"],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    package_data={
        '':["*.dll"],
    },
    data_files=[
        ('CustomTkintertitlebar/asset/', ["*.ico", "CustomTkintertitlebar/asset/light/*", "CustomTkintertitlebar/asset/dark/*"]),
    ]
)
