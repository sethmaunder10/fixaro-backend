
from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/repair")
async def handle_repair(
    image: UploadFile = None,
    make: str = Form(...),
    model: str = Form(...),
    issue: str = Form(...)
):
    # This is a placeholder for actual AI processing logic
    repair_steps = [
        "Step 1: Unplug the device.",
        "Step 2: Open the casing with a screwdriver.",
        "Step 3: Inspect internal components for visible damage.",
        "Step 4: Replace faulty component if found.",
        "Step 5: Reassemble and test the device."
    ]
    parts = ["Replacement fuse", "Screwdriver set"]
    return JSONResponse(content={
        "status": "success",
        "repair_steps": repair_steps,
        "suggested_parts": parts,
        "video_option_price": "0.99 GBP",
        "total_cost": "3.49 GBP + optional video"
    })
