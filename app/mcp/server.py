from fastmcp import FastMCP
from app.services import pet_service

mcp = FastMCP("Happy Paw 3")

# 1. Tool เดิมสำหรับดึงข้อมูลสัตว์เลี้ยงทั้งหมด
@mcp.tool()
def get_all_pets():
    """Retrieve all pets from MariaDB."""
    return pet_service.get_all_pets()

# 2. Tool ใหม่สำหรับดึงข้อมูลสัตว์เลี้ยงตาม ID
@mcp.tool()
def get_pet_by_id(pet_id: int):
    """Retrieve a single pet by its ID."""
    return pet_service.get_pet(pet_id)

# 3. Tool ใหม่สำหรับบันทึกการขาย / เปลี่ยนสถานะสัตว์เลี้ยง
@mcp.tool()
def sell_pet(pet_id: int, owner_name: str):
    """Sell a pet by updating its owner_name and marking it as sold in MariaDB."""
    # สมมติว่าใน pet_service มีฟังก์ชันสำหรับ update ข้อมูล
    updated_pet = pet_service.update_pet_owner(pet_id, owner_name)
    return f"Successfully sold pet ID {pet_id} to {owner_name}"

# 4. Tool สำหรับลบข้อมูลสัตว์เลี้ยง (ถ้าจำเป็น)
@mcp.tool()
def delete_pet(pet_id: int):
    """Delete a pet record from MariaDB."""
    pet_service.delete_pet(pet_id)
    return f"Pet ID {pet_id} has been deleted."

if __name__ == "__main__":
    mcp.run()