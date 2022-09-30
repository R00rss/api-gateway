from pydantic import BaseModel
from typing import Union


class userToSearch(BaseModel):
    ci: Union[int, None] = None
    idCard: Union[int, None] = None
    names: Union[int, None] = None
