from flask import Flask
import logging

logging.basicConfig(
    filename="uneti.log",
    format='%(asctime)s %(message)s',
    filemode='w'
)

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

app = Flask(__name__)
@app.route('/')
def inicio():
    return "<b>Bienvenido</b> <i>al</i> <s>modulo de Codigo seguro</s>"

@app.route('/cal/sum/<int:val1>/<int:val2>')
def sum(val1,val2):
    rep = "La respuesta de la suma {} + {} = {}".format(val1, val2, val1+val2)
    logger.info(rep)
    return rep
    