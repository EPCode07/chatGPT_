import typer  # Importación de librería de modelado y color
import openai  # Importación de librería openai
import config
from rich import print  # Importación de librería de tablas 
from rich.table import Table

def main():
    # Definición de key
    total = 0
    openai.api_key = config.api_key #Key de openai
    title = "💬 [bold green]Asistente virtual en Python con ChatGP[/bold green] 💬"
    print(title.center(150 ," "))      #Cabecera de la tabla

    table = Table( " [blue] Comando [/blue]", "[blue] Descripción [/blue]".center(50))  #Parámetros para la tabla Columnas
    table.add_row("exit", "Salir de la aplicación") #Contenido de la tabla Filas
    table.add_row("new", "Crear una nueva conversación") #Contenido de la tabla Filas
    print(table)

    # Contexto del asistente virtual
    context = {"role": "system",
               "content": "Eres un asistente muy útil." "Ayudas a hacer textos."}
    messages = [context]

    while True:
        content = __prompt()

        if content == "new":
            print("🆕 Se a creado una nueva conversación")
            messages = [context]
            content = __prompt()

        messages.append({"role": "user", "content": content})
        response = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=messages)
        response_content = response.choices[0].message.content
        messages.append({"role": "assistant", "content": response_content})
        print(f"\n[bold green]💻 [/bold green] [blue]{response_content}[/blue]")


def __prompt() -> str:
    prompt = typer.prompt("\n📌 ¿Qué deseas preguntarme?")
    if prompt == "exit":
        exit = typer.confirm("\n    🛑 ¿Estás seguro?")
        if exit:
            print("\n👋 ¡Nos vemos después!\n")
            raise typer.Abort()
        return __prompt()
    return prompt

if __name__ == "__main__":
    typer.run(main)