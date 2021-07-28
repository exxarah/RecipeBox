from . import general_bp


@general_bp.route('/hello/')
def hello():
    return 'Hello World!'
