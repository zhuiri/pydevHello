__author__ = 'luxeys2015-115'

from jinja2 import Environment, FileSystemLoader

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


def print_html_doc():
    j2_env = Environment(loader=FileSystemLoader(THIS_DIR),
                         trim_blocks=True)
    print j2_env.get_template('test_template.html').render(
        title='Hello Gist from Github'
    )

if __name__ == '__main__':
    print_html_doc()