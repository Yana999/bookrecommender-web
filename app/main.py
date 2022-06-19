from typing import Any

from fastapi import APIRouter, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from loguru import logger

from app.api import api_router
from app.config import settings, setup_app_logging

# Setup logging as early as possible
setup_app_logging(config=settings)


app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

root_router = APIRouter()


@root_router.get("/")
def index(request: Request) -> Any:
    """Basic HTML response."""
    body = (
        "<html lang=\"en\">"
        "<head>"
        "  <meta charset=\"UTF-8\">"
        "  <meta name=\"viewport\" content=\"width=device-width,"
        "   initial-scale=1.0\">"
        "  <title>Title</title>"
        "</head>"
        "<body style=\"display: flex; justify-content:"
        "center; width: 100%; flex-direction: column;"
        "align-items: center; position: fixed;"
        "left: 0; top: 0; right: 0; bottom: 0; background-color: #d0cced\">"
        "<h1 style=\"margin: 0 auto 20px\">Welcome to the Book recommender model page"
        "</h1>"
        "	<form class=\"book-sent-form\""
        "    style=\"margin: 0 auto 20px; border: none; display: flex;"
        "	 flex-direction: column; width: 50%; row-gap: 10px\">"
        "    <label for=\"bookNameField\">"
        "    On which book should rely our recommendation?"
        "	 </label>"
        "    <input type=\"text\" id=\"bookNameField\" class=\"bookNameField\""
        "	placeholder=\"Book title\" value=\"16 Lighthouse Road\" />"
        "    <button class=\"searchButton\" type=\"submit\">Search!</button>"
        "  </form>"
        "  <p class=\"result\"></p>"
        "  </br>"
        "  <div>"
        "  Check the docs: <a href=\"/docs\">here</a>"
        "  </div>"
        "  <script>"
        "    async function sendRequest() {"
        "      const body = {"
        "        input: requestText.value"
        "      };"
        "      return await fetch("
        "	  \"https://bookrecwebapp.herokuapp.com/api/v1/predict\","
        "	  {"
        "        method: \"POST\","
        "        headers: {"
        "          Accept: \"application/json\","
        "          \"Content-Type\": \"application/json\""
        "        },"
        "        body: JSON.stringify(body),"
        "      });"
        "    }"
        "    const submitRequestButton = document.querySelector(\".searchButton\");"
        "    const resultText = document.querySelector(\".result\");"
        "    const requestText = document.querySelector(\".bookNameField\")"
        "    document.querySelector(\".book-sent-form\").addEventListener("
        "	\"submit\", "
        "	event => event.preventDefault());"
        "    submitRequestButton.addEventListener(\"submit\", event => {"
        "      event.preventDefault();"
        "    });"
        "    submitRequestButton.addEventListener(\"click\", () => {"
        "      sendRequest().then(response => response.json())"
        "        .then(response => {"
        "		  console.log(response);"
        "          resultText.innerText = '';"
        "		  if (response.length == 1) {"
        "		    resultText.innerText = response[0]"
        "		  }"
        "		  else {"
        "            for (let i = 1; i < response.length; ++i) {"
        "              resultText.innerText += response[i] + '\n';"
        "            }"
        "		  }"
        "        });"
        "    })"
        "  </script>"
        "</body>"
        "</html>"
    )
    return HTMLResponse(content=body)


app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


if __name__ == "__main__":
    # Use this for debugging purposes only
    logger.warning("Running in development mode. Do not run like this in production.")
    import uvicorn

    uvicorn.run(app, host="localhost", port=8002, log_level="debug")
