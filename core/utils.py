import jinja2

def snake_to_camel(value):
    words = value.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

jinja_env = jinja2.Environment()
jinja_env.filters['snake_to_camel'] = snake_to_camel

def render_jinja_from_file(file, **kwargs):
    tmp = open(file).read()
    return jinja_env.from_string(tmp).render(**kwargs)

TEMPLATE_OPTIONS = {
            'list_view': 'media/views/list.txt',
            'create_view': 'media/views/create.txt',
            'update_view': 'media/views/update.txt',
            'detail_view': 'media/views/detail.txt',
            'delete_view': 'media/views/delete.txt',
            'list_template': 'media/template/list.txt',
            'create_template': 'media/template/list.txt',
            'update_template': 'media/template/list.txt',
            'detail_template': 'media/template/list.txt',
            'delete_template': 'media/template/list.txt',
        }