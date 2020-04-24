def div(func):
    return lambda *args, **kwargs : f'<div>{func(*args, **kwargs)}</div>'

def article(func):
    return lambda *args, **kwargs : f'<article>{func(*args, **kwargs)}</article>'


def p(func):
    return lambda *args, **kwargs : f'<p>{func(*args, **kwargs)}</p>'


# Here you must apply the decorators, uncomment this later
# @div
# @article
# @p
def saludo(nombre):
    return f'¡Hola {nombre}, ¿Cómo estás?'


def run():
    print(saludo('Jorge'))


if __name__ == '__main__':
    run()

# We want to have three different outputs 👇🏼

# <div>¡Hola Jorge, ¿Cómo estás?'</div>
# <article>¡Hola Jorge, ¿Cómo estás?'</article>
# <p>¡Hola Jorge, ¿Cómo estás?'</p>
