from fastapi import APIRouter, status

from configs import SETTINGS

router = APIRouter()


@router.get(
    "",
    status_code=status.HTTP_200_OK,
)
async def get_system_info():
    """
    Description:
    - 取得系統資訊。

    """
    return {
        "app_name": SETTINGS.app_name,
    }
