import setuptools

setuptools.setup(
     name='devesay',  #nombre del paquete
     version='0.1', #versión
     scripts=['app.py'] , #nombre del ejecutable
     author="Javier Alfaro", #Incluir el README.md si lo has creado
     url="https://github.com/DubstepQba", #url donde se encuentra tu paquete en Github
     packages=setuptools.find_packages(), #buscamos todas las dependecias necesarias para que tu paquete funcione (por ejemplo numpy, scipy, etc.)
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 ) #aquí añadimos información sobre el lenguaje usado, el tipo de licencia, etc.
