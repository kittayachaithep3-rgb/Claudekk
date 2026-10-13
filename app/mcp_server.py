# app/mcp_server.py
from fastmcp import FastMCP
from app.services import pet_service

mcp = FastMCP("Happy Paw 3")

@mcp.tool()
def get_all_pets():
    """Retrieve all pets from MariaDB database."""
    return pet_service.get_all_pets()

@mcp.tool()
def sell_pet(pet_id: int, owner_name: str) -> str:
    """Sell a pet or update its owner information in MariaDB.
    
    Args:
        pet_id: The ID of the pet to sell.
        owner_name: The name of the new owner.
    """
    result = pet_service.update_pet_owner(pet_id, owner_name)
    return f"Successfully processed sale for Pet ID {pet_id} to owner '{owner_name}'."

@mcp.tool()
def remove_pet(pet_id: int) -> str:
    """Delete a pet record from MariaDB by its ID."""
    pet_service.delete_pet(pet_id)
    return f"Pet ID {pet_id} deleted successfully."

if __name__ == "__main__":
    mcp.run()