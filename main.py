import sys
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def main(ia,programacion,infraestructura,analisis,diseno):

    # Los valores de los vectores representan importancia del proyecto en: 
    # [ia, programacion, infraestructura, analisis, diseño] 
    # (es a modo de ejemplo para ver si funciona)
    
    proyectos = {
        "BOTCIA":[5,5,2,2,2],
        "INFRAIT":[1,3,5,2,2],
        "TABI":[1,1,1,5,5]
    }

    proyectos_vectores = np.array(list(proyectos.values()))
    
    # Armo el array de los intereses del usuario, estos se van a comparar con el array 
    # de las necesidades del proyecto para poder recomendar el mejor proyecto
    intereses = [ia,programacion,infraestructura,analisis,diseno]
    postulante = np.array(intereses)
    
    # Comparo los arrays que representan las necesidades del proyecto y los intereses 
    # del usuario y obtengo el proyecto para el cual mas se asemejan
    similitudes = cosine_similarity(postulante.reshape(1,-1), proyectos_vectores)[0]
    proyecto_recomendado = list(proyectos.keys())[np.argmax(similitudes)]

    # Retorno el proyecto recomendado, esto es lo que va a recibir el servidor web 
    # para poder armar la respuesta al usuario
    print(proyecto_recomendado)

if __name__ == "__main__":
    ia = sys.argv[1]
    programacion = sys.argv[2]
    infraestructura = sys.argv[3]
    analisis = sys.argv[4]
    diseno = sys.argv[5]
    main(ia,programacion,infraestructura,analisis,diseno)