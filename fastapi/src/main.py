
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>My FastAPI Website</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f3f4f6;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
            }

            .container {
                background: white;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.1);
                text-align: center;
                width: 320px;
            }

            h1 {
                color: #333;
            }

            input {
                padding: 12px;
                width: 90%;
                margin: 15px 0;
                border: 1px solid #ddd;
                border-radius: 6px;
            }

            button {
                padding: 12px 24px;
                background: #2563eb;
                color: white;
                border: none;
                border-radius: 6px;
                cursor: pointer;
            }

            button:hover {
                background: #1d4ed8;
            }

            #result {
                margin-top: 20px;
                color: #2563eb;
                font-weight: bold;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>Welcome!</h1>
            <p>Мой первый сайт на FastAPI</p>

            <input id="name" type="text"
                   placeholder="Введите ваше имя">

            <button onclick="sayHello()">
                Поздороваться
            </button>

            <div id="result"></div>
        </div>

        <script>
            async function sayHello() {
                const name = document.getElementById("name").value;

                if (!name.trim()) {
                    document.getElementById("result").textContent =
                        "Введите имя";
                    return;
                }

                const response = await fetch(
                    "/api/hello/" + encodeURIComponent(name)
                );

                const data = await response.json();

                document.getElementById("result").textContent =
                    data.message;
            }
        </script>
    </body>
    </html>
    """


@app.get("/api/hello/{name}")
def hello(name: str):
    return {"message": f"Привет, {name}!"}
