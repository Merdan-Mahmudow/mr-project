from __future__ import annotations
from core.settings import Settings

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.app:root", reload=True, host="0.0.0.0", port=8000)
