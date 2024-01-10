from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

requires = ["Pillow>=9.0.0", "darkdetect>=0.8.0"]

setup(
    name="CustomTkinterTitlebar",
    version="1.0.8.1",
    author="littlewhitecloud",
    author_email="q1141926647@163.com",
    description="This is a 📚project can help you to have a custom titlebar! 这是一个可以创建自定义标题栏的📚项目",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/littlewhitecloud/CustomTkinterTitlebar",
    package="customtitlebar",
    license="MIT",
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
