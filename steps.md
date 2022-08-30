# Python

## Pasos para la creacion de entornos Virtuales
- [*Virtualenv*](#virtualenv)
- [*Pipenv*](#pipenv)
### Steps to create a virtualenv and pipenv


**Virtualenv** & **pipenv** puedes instalarlas con [pip](https://pypi.org/project/pip/)

#### Instalacion
```bash
pip install virtualenv
pip install pipenv
```


# Virtualenv

Una buena practica en crear una carpeta de entornos virtuales, y no crear un entorno para cada proyecto, aunque es un poco a gusto del desarrollador.

Pero por ejemplo
```bash
pip install virtualenv

mkdir entornosVirtuales
cd entornosVirtuales

virtualenv develop 
virtualenv scrapping

source develop/bin/activate  # Activar venv
(develop)user@user:~/ pip install dependencies
(develop)user@user:~/ deactivate  # Desactivar venv
```
En el anterior ejemplo hemos creado dos entrons virtuales, en uno instalaremos dependencia, modulos de Python que necesitaremos para hacer webScrapping como por ejemplo **pandas**, en el otro **develop** instalaremos django y asi podemos entrar en **venv** o en otro dependiendo del proyecto que estemos elaborando.

# Pipenv

Con **Pipenv** el funcionamiento es distinto, por ejemplo creamos una carpeta llamada "Develop" entramos y una vez dentro inicializamos el venv e instalamos los modulos necesarios

```bash
mkdir develop
cd develop
pipenv # Muestra los comandos disponibles
pipenv shell  # Activa el venv con el nombre de la carpeta donde se encuentra
((develop))pipenv install pandas  # Activa el venv
((develop))pipenv graph  # Activa el venv
((develop))exit  # Desactiva el venv

```
