from typing import List
from core.security import decode_access_token, security
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials

async def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(security),
) -> dict:
    """Extract current user payload from incoming Bearer token."""
    token = credentials.credentials
    payload = decode_access_token(token)

    staff_id: int = payload.get("staff_id")
    role: str = payload.get("role")

    if not staff_id or not role:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload structure",
        )
    return {"staff_id": staff_id, "role":role}

def require_roles(allowed_roles: List[str]):
    """Role-Based Access Control (RBAC) Dependency."""

    def role_checker(current_user: dict = Depends(get_current_user)):
        if current_user["role"] not in allowed_roles:
            raise HTTPException(
                status_code = status.HTTP_403_FORBIDDEN,
                detail="Operation not permitted for your user role", 
            )
        return current_user

    return role_checker