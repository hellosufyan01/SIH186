# NeuroSentry

NeuroSentry is a Next.js dashboard backed by the FastAPI stress-risk inference service.

## Run locally

Open two terminals from the project directory.

### 1. Start the FastAPI backend

```powershell
python -m uvicorn app:app --host 127.0.0.1 --port 8000
```

### 2. Start the Next.js frontend

```powershell
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

The browser calls the same-origin Next.js route at `/api/v1/predict`. That route proxies requests to FastAPI, whose URL defaults to `http://127.0.0.1:8000`. To use another backend URL, copy `.env.example` to `.env.local` and set `BACKEND_API_URL`.

## Production frontend

```powershell
npm run build
npm run start
```

## Deploy the frontend to Vercel

The Next.js frontend can be deployed to Vercel, but the FastAPI service and
`stress_risk_model.joblib` must be hosted separately. Vercel only runs the
Next.js application in this setup.

1. Push this project to a GitHub repository. Do not commit `.env.local`,
   credentials, or private data.
2. Deploy the FastAPI service to a Python host such as Render, Railway, or
   Google Cloud Run. The repository now includes `requirements.txt` and the
   model-loading path is independent of the host working directory. The
   service must expose:
   - `POST /api/v1/predict`
   - `GET /health`
3. Make sure the Python host includes `stress_risk_model.joblib` and the Python
   dependencies used by `app.py`. For a generic Python host, use:

   ```text
   Build command: pip install -r requirements.txt
   Start command: uvicorn app:app --host 0.0.0.0 --port $PORT
   ```

   On hosts that do not provide `$PORT`, use the platform's port variable or
   `8000`.
4. Confirm the deployed backend works by opening its `/health` URL and sending a
   test request to `/api/v1/predict`.
5. In Vercel, select **Add New > Project**, import the GitHub repository, and
   keep the framework preset as **Next.js**.
6. Set the project root to the folder containing `package.json` (the repository
   root for this project).
7. Add this Vercel environment variable for **Production**, **Preview**, and
   **Development**:

   ```text
   BACKEND_API_URL=https://your-fastapi-service.example.com
   ```

   Do not add a trailing slash.
8. Deploy the project. Vercel will run `npm run build` automatically.
9. Open the deployed URL and test:
   - `/`
   - `/dashboard`
   - Routine profile assessment
   - Review profile assessment
10. If an assessment returns a `503`, check that `BACKEND_API_URL` is set in
    the environment used by the deployment and redeploy after changing it.
