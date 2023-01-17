import typer 
import os

app = typer.Typer()


@app.command()
def react_daisy(name: str = typer.Option(..., prompt=True)):
    typer.echo(f"Cloning")
    os.system(f"git clone https://github.com/DavidFX/vite-react-daisyui {name}")
    os.system(f"cd {name}")
    typer.echo(f"Installing")
    os.chdir(name)
    os.system("rmdir /s /q .git")
    os.system("pnpm install")
    os.system("code .")

    

if __name__ == "__main__":
    app()