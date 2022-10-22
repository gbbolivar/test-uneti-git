from flask import Flask 
import logging
app = Flask(__name__) 

# Crear la configuracion del logger
logging.basicConfig(
    filename="taller.log",
    format='%(asctime)s %(message)s',
    filemode='w')
# Instanciar el objeto logger
logger = logging.getLogger()

# Configurar que debe notificar a partir de DEBUG 
logger.setLevel(logging.DEBUG)

@app.route("/") 
def inicio(): 
    return "<p>Bienvenido al módulo de Desarrollo Seguro</p>" 

@app.route("/cal/sum/<int:val1>/<int:val2>")
def cal_suma(val1, val2):
    resul = val1 + val2
    resp = "<p>El resultado de la suma es {}!</p>".format(resul)
    logger.info("Val1:{}, Val2:{}, {}".format(val1,val2,resp))
    return resp