
# SAW
SAW is a template for a Python Command Line Interface (CLI) application designed to execute various commands.


## Comandi di Esempio

| Comando | How To Run| Descrizione |
|---------|-|-------------|
| **dummy**|`python cli.py dummy` |  This command is just an example. |
| **env** | `python cli.py env --all` | This command prints all environment variables, the parameter is for demonstration purposes only. |
| **help** | `python cli.py -h` | All Commands |



### Configurazione

#### File di Configurazione
- `.env_defaults`:Contains default environment variables.
- `.env`: Contains user-specific environment variables.



# Development Environment
The project includes a configuration for Visual Studio Code and a `.devcontainer` file to set up the development environment in a Docker container.


#### Docker
Il progetto include un file `Dockerfile` per creare un'immagine Docker dell'applicazione.

```dockerfile
FROM python:3.9
RUN pip install pip --upgrade
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir .
CMD ["/bin/bash"]
```

#### Test
The project uses `unittest` for testing. Tests are run automatically when files are saved.


### Dipendenze
The project's dependencies are managed using `poetry` and are specified in the `pyproject.toml` file.

### Autori
- Alessandro Staniscia (Odyno - alessandro [at] staniscia.net)

### Licenza
Under MIT
