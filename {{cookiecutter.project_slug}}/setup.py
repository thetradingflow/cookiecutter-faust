from setuptools import find_packages, setup

requires = [
    {% if cookiecutter.include_rocksdb.lower() == "y" %}
    "faust[rocksdb]",{% else %}
    "faust",{% endif %}
    "mode",
    "robinhood-aiokafka",
    "simple-settings",{% if cookiecutter.include_codec_example.lower() == "y" %}
    "msgpack",{% endif %}{% if cookiecutter.include_schema_registry.lower() == "y" %}
    "python-schema-registry-client",{% endif %}
]

setup(
    name="{{cookiecutter.project_name}}",
    version="{{cookiecutter.version}}",
    description="{{cookiecutter.description}}",
    long_description="""{{cookiecutter.description}}""",
    classifiers=["Programming Language :: Python"],
    author="{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.author_email}}",
    url="",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=[],
    setup_requires=[],
    dependency_links=[],
    entry_points={
        "console_scripts": [
            "{{cookiecutter.project_slug}} = {{cookiecutter.project_slug}}.app:main"
        ],
        {% if cookiecutter.include_codec_example.lower() == "y" %}
        "faust.codecs": [
            "msgpack_codec = {{cookiecutter.project_slug}}.codecs.codec:msgpack_codec",
            # add entries here to add more custom codecs
        ],
        {% endif %}
    },
)
