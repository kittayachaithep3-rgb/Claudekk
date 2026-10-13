# 1. Import NiceGUI
from nicegui import ui
# 2. Import our Service Layer
from app.services import pet_service

# 3. Create the page heading
ui.label("Happy Paw 3 - Pet Hotel").classes("text-h4")

# 4. Create a short description
ui.label("Pet Management System")

# 5. Retrieve pets from our Service Layer
pets = pet_service.get_all_pets()

# 6. Display pets in a table
ui.table(
    columns=[
        {"name": "id", "label": "ID", "field": "id"},
        {"name": "name", "label": "Name", "field": "name"},
        {"name": "type", "label": "Type", "field": "type"},
        {"name": "breed", "label": "Breed", "field": "breed"},
        {"name": "age", "label": "Age", "field": "age"},
        {"name": "owner_name", "label": "Owner", "field": "owner_name"},
    ],
    rows=pets,
    row_key="id",
).classes("w-full")

# 7. Start NiceGUI
ui.run(port=8080, reload=False)